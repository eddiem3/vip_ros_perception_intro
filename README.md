# VIP ROS Perception Intro Task
## Setup
Login to your VIP machine

```
<username>@auatl-ros001.ssh.xtriage.com
```
## Install 
```
sudo apt install tmux
```

### Download the starter code and videos
```
git clone https://github.com/eddiem3/vip_ros_perception_intro.git
cd vip_ros_perception_intro
git lfs pull
source /opt/ros/jazzy/setup.bash
python3 ros2_video_reader.py
```
This node should read video data from one of the videos in the same directory and publish the data to topic called /video_frames. You'll want to update the code to select one of the videos in the folder. It's default is "input_video.avi" which does not exist.

## Tasks 

### Task 1: Detect the lines.
Make a ROS2 node that subscribes to /video_frames and uses edge detection to find the lines of tape on the ground in the video file 'follow_lines.avi' The simplest way to do this is to filter out the tape by color. 
Review this OpenCV tutorial for guidance: https://www.geeksforgeeks.org/filter-color-with-opencv/

### Task 2: Detect Objects
Make a ROS2 node that subscribes to /video_frames and uses YOLO object detector to draw bounding boxes around objects in the video stream in the video file 'segment_sidewalk,avi'. Refer to YOLO tutorial here:
https://docs.ultralytics.com/modes/predict/#how-can-i-visualize-and-save-the-results-of-yolov8-predictions

## Bonus Tasks

### Bonus Task 1:Segment The Scenes 
Semantic segmantation is a critical task autonomous vehicles perform to differntiate between driveable pahts. Perform semantic segmantation on the video steam from the file 'segment_sidewalk.avi' Use the library Pixellib
for off-the-shelf semantic segmentation models to segment the scene: https://github.com/ayoolaolafenwa/PixelLib

### Bonus Task 2: Segment Poles from the frames without training a new model
Meta, revolutionized semantic segmentation when the launched SAM (Segment Anything Model). Recently SAM2 has been expanded to work with both images and videos. Using SAM or SAM2, segment out the poles in the video 'poles.avi.' 
You'll need to give SAM or SAM2 cut out of a pole so that it can find it in the future. This is known as prompting the model. Here's a link to SAM2: https://github.com/facebookresearch/segment-anything-2
