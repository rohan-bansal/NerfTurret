#include <VarSpeedServo.h>

VarSpeedServo servo_yaw;
VarSpeedServo servo_pitch;
VarSpeedServo servo_shoot;

servoSequencePoint shoot_seq[] = {{110, 255},{90, 255}};

signed int x;
signed int y;

unsigned int pos;

void correctError() {

  if(x < 2) {
    servo_yaw.write(8, 5, false);
  } else if(x > 2) {
    servo_yaw.write(170, 5, false);
  } else {
//    servo_yaw.write(90);
    servo_yaw.stop();
  }

  if(y < -2) {
    servo_pitch.write(160, 5, false);
  } else if(y > 2) {
    servo_pitch.write(50, 5, false);
  } else {
//    servo_pitch.write(90);
    servo_yaw.stop();
  }
}

void shoot() {
  servo_shoot.write(125, 255);
  servo_shoot.wait();
  servo_shoot.write(90, 255);
}


void setup() {
  Serial.begin(115200);

  servo_yaw.attach(9);
  servo_pitch.attach(10);
  servo_shoot.attach(11);

  servo_yaw.write(90);
  servo_pitch.write(100);
  servo_shoot.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    x = Serial.readStringUntil('X').toInt();
    y = Serial.readStringUntil('Y').toInt();

    if(x == 1000.0) {
      shoot();
    } else {
      correctError();
    }
  }
}