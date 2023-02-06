# Face Tracking Nerf Turret

![don't let it see u](pics/thumb.jpg)


## What exactly is that?

It's a disassembled foam dart shooter mounted to a 3d printed turret, controlled by three servos, with a webcam on top. On command it will go sentry mode, and track the nearest humanoid face to launch missiles at.

## How does it work?

Two servos control the turret's yaw and pitch, and one is placed at the back of the gun to shoot the dart. All three are wired up to an Arduino microcontroller, which is in turn accepting commands from a Python script on my laptop. The script handles the vision system, relaying an error margin between the camera and the victim to the Arduino. The Arduino uses that error in a control loop to track and terrify the victim by rotating the servos.

Should the victim make the critical mistake of aligning perfectly with the turret's line of sight, the Arduino will be instructed to fire the third servo at the back of the turret, launching the dart with terrific accuracy.

## What's it made of?

It's 40% 3d printed material and 60% hot glue.
