let capture;
let poseNet;
// let poses =[];
// let bodyPose;
// let connections;

function modelLoaded(){
    console.log("Model Loading Successful");
}

function setup() {
    createCanvas(1000, 600);
    
    capture = createCapture(VIDEO);
    capture.hide();
    
    poseNet = ml5.bodyPose(capture, modelLoaded);
    poseNet.detect(gotPoses);
    // poseNet.detectStart(capture, gotPoses);


    // bodyPose.detectStart(capture, gotPoses);
    // connections = bodyPose.getSkeleton();
    console.log("Fine till here");
}

function recPoses(pos){
    console.log("Got poses");
    
    console.log(pos)
}

function gotPoses(results) {
    // Save the output to the poses variable
    poses = results;
    console.log(results)
}

function draw(){
    image(capture, 0, 0, 1000, 600);

    // Skeleton connections
    // for(let i =0;i<poses.length; i++){
    //     let p = poses[i];
    //     for(let j = 0; j<connections.length; j++){
    //         let ptAIdx = connections[j][0];
    //         let ptBIdx = connections[j][1];
            
    //         let ptA = pose.keypoints[ptAIdx];
    //         let ptB = pose.keypoints[ptBIdx];

    //         // Drawing line if both points are confident enough
    //         if(ptA.confidence > 0.15 && ptB.confidence>0.15){
    //             stroke(0, 255, 0);
    //             stokeWeight(2);
    //             line(ptA.x, ptA.y, ptB.x, ptB.y);
    //         }
    //     }
    // }

    // Draw all poitns
    // for(let i = 0; i<poses.length; i++){
    //     let p = poses[i];
    //     for(let j = 0; j<p.keypoints.length; j++){
    //         let kp = pose.keypoints[j]

    //         if(kp.confidence>0.15){
    //             fill(0,255,0);
    //             noStroke();
    //             circle(keypoints.x, keypoints.y, 8);
    //         }
    //     }
    // }
}