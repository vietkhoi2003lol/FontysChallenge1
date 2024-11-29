// Import the library for the accelerometter
#include <Arduino_LSM9DS1.h>

// Initiate variables for different x axis, y axis, and z axis and variables to identify how much degree does the octahedron rotate in respects of 3 dimansional axes
float x, y, z;
int degreesX = 0;
int degreesY = 0;

// Basic configuration
void setup() {
  Serial.begin(9600);
  while (!Serial)
    ;
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1)
      ;
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println("Hz");
}

void loop() {
  // The accelrometer measures the the values of x, y, z
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
  }

  //  degreesX and degreesY are 0 when the arduino board lying on flat surface facing up
  // When x = 0, Arduino board lays flat on table, when x = 1, Arduino board tilts up (incline) at an angle of 90 degree relative to the table surface
  // 0 <= z <= 1 is the range of z to indicate arduino boards is tilting up in range of 0 to 90 degree
  if (x >= 0 && x <= 1 && z >= 0 && z <= 1) {
    x = 100 * x;                       // Initial x value is approximately from -1 to 1. Scaling up this value 100 times
    degreesX = map(x, 0, 100, 0, 90);  // Map the x axix to 0-90 degree. This convert x value to degree ranging from 0 to 90
  }

  // 0 >= z >= -1 is the approx range of z to indicate arduino boards is tilting up in range of 90 to 180 degree
  if (x >= 0 && z <= 0 && z >= -1.04) {
    x = 100 * x;
    degreesX = map(x, 0, 100, 180, 90);  // Map the x axes to 90-180 degree
  }
  if (x <= 0 && x >= -1 && z <= 0 && z >= -1.05) {
    x = 100 * x;
    degreesX = map(x, 0, -100, 180, 270);  // Map the x axes to 180-270 degree
  }
  if (x < 0 && z > 0) {
    x = 100 * x;
    degreesX = map(x, 0, -100, 360, 270);  // 4
  }




  if (y >= 0 && y <= 1 && z >= 0 && z <= 1) {
    y = 100 * y;
    degreesY = map(y, 0, 100, 0, 90);  //Map the y axes to 0-90 degree
  }
  if (y >= 0 && y <= 1 && z <= 0 && z >= -1.04) {
    y = 100 * y;
    degreesY = map(y, 0, 100, 180, 90);  //2
  }

  if (y <= 0 && y >= -1 && z <= 0 && z >= -1.04) {
    y = 100 * y;
    degreesY = map(y, 0, -100, 180, 270);  //3
  }

  if (y <= 0 && y >= -1 && z >= 0 && z <= 1) {
    y = 100 * y;
    degreesY = map(y, 0, -100, 360, 270);  //4
  }

  // Detect which side the octahedron is facing up
  // Deteck if the Break on octahedron is facing up (1)
  if ((degreesX >= 295 && degreesX <= 345) && (degreesY >= 60 && degreesY <= 85)) {
    Serial.println("Break");
  }

  // Detect if Challenge 1 on octahedron is facing up (2)
  if ((degreesX >= 115 && degreesX <= 165) && (degreesY >= 95 && degreesY <= 130)) {
    Serial.println("Challenge 1");
  }

  // Detect if DT is facing up (3)
  if ((degreesX >= 245 && degreesX <= 265) && (degreesY >= 150 && degreesY <= 210)) {
    Serial.println("DT");
  }

  // Detect if PPI is facing up (4)
  if ((degreesX >= 160 && degreesX <= 225) && (degreesY >= 165 && degreesY <= 210)) {
    Serial.println("PPI");
  }

  // Detect if DBW is facing up (5)
  if ((degreesX >= 120 && degreesX <= 175) && (degreesY >= 240 && degreesY <= 270)) {
    Serial.println("DBW");
  }

  // Detect if SE is facing up (6)
  if ((degreesX >= 340 || degreesX <= 30) && (degreesY >= 340 || degreesY <= 35)) {
    Serial.println("SE");
  }

  // Detect if PPR is facing up (7)
  if ((degreesX >= 285 && degreesX <= 340) && (degreesY >= 270 && degreesY <= 310)) {
    Serial.println("PBR");
  }

  //  Serial.print(degreesX);
  //  Serial.print(" - ");
  //  Serial.println(degreesY);
  delay(800);
}