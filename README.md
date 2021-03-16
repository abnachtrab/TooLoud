# TooLoud
This is a simple python script that presses ALT+F4 whenever the input from the mic reaches a certain threshold.
I personally use it for my brother, who's voice can be loud enough that it is heard by neighbors.
You can automate the script through many ways, if you want to you can look up "How to run a python file at startup" or "How to run a python file in the background."

## Requirements
- numpy
- pynput
- sounddevice

## Setup
1. Install [python](https://www.python.org/downloads/) if you have not already
2. Open command prompt and type `pip install numpy`, `pip install pynput`, and `pip install sounddevice`
3. Run the script using `python TooLoud.py` when in the directory you have the file in

## Tweaking the File
You really only should change the "limit" variable, but feel free to change other things.
I've found that the average conversation at a normal volume is anywhere from 0-150 (but feel free to change it as you see fit).
