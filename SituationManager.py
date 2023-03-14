from geopy import distance
import zmq

context = zmq.Context()

my_position = (48.82379745679102, 2.208597506686108)

#  Socket to talk to server
print("Connecting to FlightTrack topic ...")
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'FlightTrack')

pub = context.socket(zmq.PUB)
pub.bind("tcp://127.0.0.1:5556")

while True:
    topic = socket.recv_string()
    flight = socket.recv_pyobj()
    tactical_distance = distance.distance((flight.latitude, flight.longitude), my_position)
    if tactical_distance.kilometers < 5:
        pub.send_string("HueTrack", flags=zmq.SNDMORE)
        pub.send_string("Threat!")
        print("Sent")
