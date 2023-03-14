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
    flights = socket.recv_pyobj()
    planes_near_me = False
    for flight in flights:
        tactical_distance = distance.distance((flight.latitude, flight.longitude), my_position)
        if tactical_distance.kilometers < 10:
            planes_near_me = True
    if planes_near_me:
        pub.send_string("HueTrack", flags=zmq.SNDMORE)
        pub.send_string("Threat!")
        print("Planes near me")

