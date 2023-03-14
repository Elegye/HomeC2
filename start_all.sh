source env/bin/activate
(trap 'kill 0' SIGINT; python3 FlightManager.py  & python3 SituationManager.py & python3 HueManager.py)