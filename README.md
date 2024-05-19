## Introduction
This is a project created for StormHacks 2024

## Inspiration

Thanks to Major Leauge Hacking, our team were able to borrowed a Leap motion during the hackathon. Therefore, we decided to learn how to use these leap motion and this is what our team has came up with: Drawing using your hand motion. LeapDoodle :)

## What it does
Have you ever used Microsoft Paint? Have you ever experince the non-usefulness of not able to draw correctly using your mouse? I am horner to present you LeapDoodle, A drawing app using your hand :)

Here is our LeapDoodle's feature that we are pround of.

- ✅ Black Canvas
- ✅ Super complex ways to draw something on the canvas depend on how you move your hand.
- ✅ If you are someone who seek hardship in the creation of art, this is for you :)

## How we built it
- The Leap motion I used for this hackathon used Ultra Leap, which use C as the backend. we used their API [leapc-python-bindings](https://github.com/ultraleap/leapc-python-bindings) to calls the backend. Then, we run a pygame window which display the logic when user interact with the app. This was run on python 3.11


## What we learned
- Using Leap motion controller to record the hand motion
- The struggle when working with hardware. There is a lot going under the hood to make every works perfectly the way it is. Through this project, We feel more like we still have things to learn if we want to work with hardware in the future.

## Challenges we ran into
- One of the biggest challenges in this hackathon is time. We must deliver a funtional product within a 24-hour period. There is so much more that I want to implement for the app, but I must work on a functioning product first. If I have time in the future, I want to implement more so it can function like a full Microsoft Paint.

## Accomplishments that we're proud of
- Connect to a Leap motion controller and record data
- Learn about API from UltraLeap

## Build Instructions
- Since this is my first time working with actual hardware, I realize that a lot have to factors in to be able to make the program run smoothly, so please forgive my really long build instruction.
- You will also need a leap-motion controller

1. Clone our git repository: https://github.com/qvd808/stormhack-2024
2. Run
```
cd leapc-python-bindings
```
3. Make sure you have a python environment set ups (It is good if you have a virtual environment). Then, run
```
pip install -r requirements.txt
python -m build leapc-cffi
pip install leapc-cffi/dist/leapc_cffi-0.0.1.tar.gz
pip install -e leapc-python-api
```
4. Run
```
python main.py
```

## How to draw
- Use your right hand to draw. If you pinch your right hand, the circle will get smaller, and the line you draw will have a smaller width. If your index finger is far from your thumb, the circle will get bigger.
- To start drawing, pinch your index finger and thumb together. To enter erase mode, pinch your index, middle finger, and thumb together. The radius of the circle will increase based on how you pinch with your right hand.
