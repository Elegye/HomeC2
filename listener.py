import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'FlightTrack')

while True:
    print("Receiving ...")
    topic = socket.recv_string()
    flight = socket.recv_pyobj()
    print(flight)
