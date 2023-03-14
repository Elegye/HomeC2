import zmq
from phue import Bridge
import time

b = Bridge('192.168.1.16')
context = zmq.Context()

print("Connecting to HueTrack topic ...")
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5556")
socket.setsockopt(zmq.SUBSCRIBE, b'HueTrack')

while True:
    topic = socket.recv_string()
    print(topic)
    data = socket.recv_string()
    print(data)
    print(b.set_light(5, 'bri', 1))
    time.sleep(2)
    print(b.set_light(5, 'bri', 254))
    time.sleep(1)


