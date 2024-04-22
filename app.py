from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import cv2
import base64
import RPi.GPIO as GPIO

app = Flask(__name__)
socketio = SocketIO(app)

# Setup GPIO pins for motor control
GPIO.setmode(GPIO.BOARD)
motor1_pin1 = 11
motor1_pin2 = 12
motor2_pin1 = 13
motor2_pin2 = 15
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

# Function to control the robot's movement
def move(direction):
    if direction == 'forward':
        GPIO.output(motor1_pin1, GPIO.HIGH)
        GPIO.output(motor1_pin2, GPIO.LOW)
        GPIO.output(motor2_pin1, GPIO.HIGH)
        GPIO.output(motor2_pin2, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(motor1_pin1, GPIO.LOW)
        GPIO.output(motor1_pin2, GPIO.HIGH)
        GPIO.output(motor2_pin1, GPIO.LOW)
        GPIO.output(motor2_pin2, GPIO.HIGH)
    elif direction == 'left':
        GPIO.output(motor1_pin1, GPIO.HIGH)
        GPIO.output(motor1_pin2, GPIO.LOW)
        GPIO.output(motor2_pin1, GPIO.LOW)
        GPIO.output(motor2_pin2, GPIO.HIGH)

    elif direction == 'right':
        GPIO.output(motor1_pin1, GPIO.LOW)
        GPIO.output(motor1_pin2, GPIO.HIGH)
        GPIO.output(motor2_pin1, GPIO.HIGH)
        GPIO.output(motor2_pin2, GPIO.LOW)

    elif direction == 'stop':
        # Stop the motors
        GPIO.output(motor1_pin1, GPIO.LOW)
        GPIO.output(motor1_pin2, GPIO.LOW)
        GPIO.output(motor2_pin1, GPIO.LOW)
        GPIO.output(motor2_pin2, GPIO.LOW)

# Function to generate live camera feed
def gen_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for streaming live camera feed
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Socket.IO event handler for receiving commands from the webpage
@socketio.on('command')
def handle_command(command):
    print('received command: ' + str(command))
    if command == 'livecamera':
        pass  # Add logic to handle live camera command
    else:
        move(command)

if __name__ == '__main__':
    try:
        # Use 0.0.0.0 as the host to make the server accessible from any device on the network
        socketio.run(app, host='0.0.0.0')
    finally:
        # Cleanup GPIO pins
        GPIO.cleanup()
