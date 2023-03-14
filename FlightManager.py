from FlightRadar24.api import FlightRadar24API, Flight
import time
import zmq

fr_api = FlightRadar24API()

zones = fr_api.get_zones()
print(zones['europe']['subzones']['france'])

zone = zones['europe']['subzones']['france']
bounds = fr_api.get_bounds(zone)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555")

while True:
    flights = fr_api.get_flights(bounds=bounds)

    socket.send_string("FlightTrack", flags=zmq.SNDMORE)
    socket.send_pyobj(flights)
    print("Flights sent")

    time.sleep(10)