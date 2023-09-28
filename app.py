from flask import Flask, render_template, Response
from flask_cors import CORS  # Import CORS
import cv2
import os

app = Flask(__name__)

CORS(app)  # Enable CORS for your Flask app

camera = cv2.VideoCapture(0) 

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# from flask import Flask, render_template, Response
# from flask_cors import CORS
# import cv2
# import os
# import numpy as np

# app = Flask(__name__)
# CORS(app)

# camera = cv2.VideoCapture(0)
# frame_width = int(camera.get(3))
# frame_height = int(camera.get(4))
# out = None
# frame_counter = 0

# def start_video_writer():
#     global out, frame_counter
#     frame_counter += 1
#     filename = f'output_{frame_counter}.mp4'
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(filename, fourcc, 20.0, (frame_width, frame_height))

# def gen_frames():
#     global out, frame_counter
#     start_time = cv2.getTickCount()
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             if out is None:
#                 start_video_writer()
#             if frame_counter > 0:
#                 frame_counter -= 1
#                 if out is not None:
#                     out.write(frame)
#                 ret, buffer = cv2.imencode('.jpg', frame)
#                 frame = buffer.tobytes()
#                 yield (b'--frame\r\n'
#                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#         elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
#         if elapsed_time >= 1.0:
#             if out is not None:
#                 out.release()
#                 out = None
#             start_time = cv2.getTickCount()

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')



# from flask import Flask, send_file
# from flask_cors import CORS
# import cv2
# import os

# app = Flask(__name__)
# CORS(app)

# # Capture and record the webcam feed as an .mp4 video file
# camera = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

# @app.route('/video')
# def get_video():
#     return send_file('output.mp4', mimetype='video/mp4')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

# import asyncio
# import websockets
# import cv2

# class VideoStreamer:
#   def __init__(self):
#     self.clients = []

#   async def run(self):
#     camera = cv2.VideoCapture(0)

#     while True:
#     #   success, frame = camera.read()
#         frame = camera.read()

#     #   if not success:
#     #     break

#     #   else:
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()

#         for client in self.clients:
#           await client.send(frame)

#   async def handle_client(self, websocket):
#     self.clients.append(websocket)

#     while True:
#       message = await websocket.recv()

#       if message is None:
#         break

#     self.clients.remove(websocket)

# if __name__ == '__main__':
#   streamer = VideoStreamer()

#   start_server = websockets.serve(streamer.handle_client, 'localhost', 8080)

#   asyncio.get_event_loop().run_until_complete(start_server)

#   asyncio.get_event_loop().run_until_complete(streamer.run())