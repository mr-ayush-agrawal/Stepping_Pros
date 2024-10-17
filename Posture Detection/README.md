# Posture Detection
Here we will be detecting the posture of the human in front of camera.

-> This is going to be an application level Implementation of the DL models.<br>
-> We are not training the model here, instered we are using pre-trained model called PoseNet.<br>

Important Blog Post for the same: https://blog.tensorflow.org/2018/05/real-time-human-pose-estimation-in.html

## Project 
This project we are building on JS. Here we are going to use 2 libraries of JS called
- [p5.js](https://p5js.org/tutorials/)
- [ML5.js](https://docs.ml5js.org/#/)

### P5.js - Things to remember
We have to create a script -> sketch.js, where we need to make 2 funcitons
1. *setup*: All the code run once
2. *draw*: This runs as in infinite loop

We capture the live photogae from WebCamera, using `createCapture(VIDEO)` in Setup fucntion and use `imgae(capture, x, y, w, h)` in the draw function which continiously show the image.

### ML5.js
This is the main library which allow us to use ML models in JS.

-> This library is based on TensorFlow.js (and no other external dependencies) which is the JS version of TensorFlow. This Library makes the task of using TF easier.

## PoseNET
We are using the PoseNET model present in the same library. This is a very popular model where we can detect the posture of the human being from a live video or preloaded video.


    
Leaving this project here -> Got some Internal issues may or maynot try this later. 

[Reference Video](https://www.youtube.com/watch?v=kRvIcdLhDtU&list=PLKnIA16_RmvY5eP91BGPa0vXUYmIdtfPQ&index=12)