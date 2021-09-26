# cfs2021_object_avoidance
This project is uses Jetson Nano and Jetson Inference for SSD implementation.
This program uses SSD (Single Shot Detector) to detect object then a proposed avoiding algorithm and needed angle is determined based on Image data.

## Files
- main.py : main file for running the program
- actuator.py : for moving the car throttling and steering
- detect.py : for obstacle detection using SSD
- controller.py : algorithms and condition to avoid obstacle
- writedata.py : for saving log and image files

## To run
A Jetson Nano with Jetson Inference installed.
Run the main.py to run the program.

In main.py:
- For checking, uses controller.py checkangle function
- For moving the car, uses controller.py move function