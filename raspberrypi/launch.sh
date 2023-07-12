#!/bin/bash
flask run --host=0.0.0.0
python pyboard.py --device /dev/ttyACM0 controller.py
