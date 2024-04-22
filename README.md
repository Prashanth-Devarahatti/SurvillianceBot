# Survilliance Bot Webmiever (KATTAPPA)

Webmiwer is a web-based robot control system that allows you to control a Raspberry Pi-based robot remotely through a web interface. You can stream live camera feed from the robot and send movement commands using buttons on the web page.

## Dependencies:

- Python 3.x
- Flask (`flask`)
- Flask-SocketIO (`flask_socketio`)
- OpenCV (`cv2`)
- RPi.GPIO (`RPi.GPIO`)

Ensure that you have installed the required Python libraries in your Raspberry Pi environment before proceeding.

## Hardware Setup:

1. Connect the motors to the GPIO pins of the Raspberry Pi for LM298N Motor driver for controlling the motors direction responsible for robot's movement.
2. Connect a camera module to the Raspberry Pi for streaming live video feed.

## Software Setup:

1. Configure the GPIO pins for motor control and setup the Flask application with Socket.IO for real-time communication.
2. Implement functions to control the robot's movement and generate live camera feed using OpenCV.
3. Create an HTML template (`index.html`) for the web interface with buttons for controlling the robot and displaying the video feed.
4. Serve the web interface using Flask and handle WebSocket events for sending movement commands.

## Usage:

1. Launch the Flask server on your Raspberry Pi by running the provided Python script.
2. Access the web interface by navigating to the Raspberry Pi's IP address followed by port 5000 in a web browser.
3. Use the provided buttons on the web page to control the robot's movement (forward, backward, left, right, stop).
4. Click the "Live Camera" button to stream live video feed from the robot's camera.
5. Explore additional functionalities and customize the system according to your requirements.

## Code Structure:

- **Python Script (`app.py`)**: Contains the Flask application setup, GPIO configuration, motor control functions, camera feed generation, and WebSocket event handling.

- **HTML Template (`index.html`)**: Provides the web interface layout with buttons for controlling the robot and displaying the live video feed.

## Notes:

- Ensure that you have correctly wired the motors and camera module to the Raspberry Pi.
- Make sure to replace `"YOUR_PI_IP_ADDRESS"` in the HTML script with the actual IP address of your Raspberry Pi.
- Customize the GPIO pin numbers and motor control logic according to your hardware setup.
- You may need to install additional libraries or packages depending on your specific Raspberry Pi configuration.

## Contributors:

- Prashanth Devarahatti
---
Feel free to customize the README further with additional sections or details as needed!
