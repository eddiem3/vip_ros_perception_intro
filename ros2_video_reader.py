#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class VideoReaderNode(Node):
    def __init__(self):
        # Initialize the ROS2 node
        super().__init__('video_reader_node')

        # Parameters
        self.declare_parameter('video_file', 'follow_lines.avi')
        self.declare_parameter('fps', 30.0)

        # Get the video file path and FPS from parameters
        self.video_file = self.get_parameter('video_file').get_parameter_value().string_value
        self.fps = self.get_parameter('fps').get_parameter_value().double_value

        # Open the video file using OpenCV
        self.cap = cv2.VideoCapture(self.video_file)
        if not self.cap.isOpened():
            self.get_logger().error(f"Cannot open video file: {self.video_file}")
            return

        # CvBridge for converting OpenCV images to ROS2 messages
        self.bridge = CvBridge()

        # Publisher for publishing video frames
        self.publisher_ = self.create_publisher(Image, 'video_frames', 10)

        # Timer to control the publishing rate based on FPS
        self.timer_period = 1.0 / self.fps
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.get_logger().info("Video Reader Node started.")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert OpenCV frame (BGR8) to ROS2 Image message
            image_message = self.bridge.cv2_to_imgmsg(frame, "bgr8")

            # Publish the image message
            self.publisher_.publish(image_message)

        else:
            # If no more frames, stop the node
            self.get_logger().info("End of video file reached.")
            self.cap.release()
            rclpy.shutdown()

    def cleanup(self):
        # Release the video capture object when shutting down
        if self.cap.isOpened():
            self.cap.release()


def main(args=None):
    rclpy.init(args=args)
    video_reader_node = VideoReaderNode()

    try:
        rclpy.spin(video_reader_node)
    except KeyboardInterrupt:
        video_reader_node.get_logger().info("Node stopped via KeyboardInterrupt")
    finally:
        video_reader_node.cleanup()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

