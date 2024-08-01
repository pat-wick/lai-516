let angle; // Current angle of the pendulum
let angVelocity; // Current angular velocity
let angAcceleration; // Angular acceleration
let length; // Length of the pendulum arm
let originX, originY; // The origin point of the pendulum
let degrees; // Initial pendulum angle in degrees

function setup() {
  createCanvas(600, 600);
  degrees = 15;
  angle = degrees * PI / 180; // Initial angle
  angVelocity = 0.0;
  angAcceleration = 0.0;
  length = 300; // Length of the pendulum arm
  mountX = width / 2; // Set the attach point at the center top of the canvas
  mountY = 0;
  background('white');
}

function draw() {
  background('white');

  // Calculate the position of the pendulum bob
  let x = mountX + length * sin(angle);
  let y = mountY + length * cos(angle);

  // Draw the pendulum
  stroke('black');
  strokeWeight(2);
  line(mountX, mountY, x, y);
  fill(0);
  ellipse(x, y, 10, 10); // Draw the pendulum bob

  // Compute the angular acceleration
  let gravity = 9.81; // Acceleration due to gravity
  angAcceleration = (-gravity / length) * sin(angle);

  // Update the angular velocity and angle
  angVelocity += angAcceleration;
  angle += angVelocity;
}
