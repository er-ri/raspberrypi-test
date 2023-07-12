"""Responder between Raspberry PI and PC
The module runs on native Raspberry PI environment.
Using the following command to launch the flask server:
    flask run --host=0.0.0.0
"""

import cv2 
import serial 
from flask import Flask, Response, render_template, request 

cam = cv2.VideoCapture(0)

serialPort = serial.Serial(
    port='/dev/ttyAMA1',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def gen_frames():
    while True:
        success, frame = cam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
            )

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/cmd", methods=["POST"])
def cmd():
    global serialPort
    # requestData = request.form["speed"]
    # print("Sending command to SPIKE: {}".format(requestData))
    requestData = 30
    if serialPort:
        serialPort.write(requestData)
    return "Success!"
 
@app.route("/stop", methods=["POST"])
def stop():
    global serialPort
    # requestData = request.form["speed"]
    # print("Sending command to SPIKE: {}".format(requestData))
    requestData = 0
    if serialPort:
        serialPort.write(requestData)
    return "Success!"

if __name__ == "__main__":
    app.run(debug=True)