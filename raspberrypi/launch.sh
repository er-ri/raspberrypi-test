#!/bin/bash
python pyboard.py --device /dev/ttyACM0 controller.py ; flask run --host=0.0.0.0

