# Memo




* Start video streaming.
```bash
/usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 10 -r 1280x720" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8085 -w /usr/local/share/mjpg-streamer/www"
```


    sudo shutdown now
    
http://192.168.100.22:8085/stream_simple.html


python pyboard.py --device /dev/ttyACM0 spike_CarControl.py

flask run --host=0.0.0.0

screen /dev/ttyACM0 115200
help(hub.port.D)

pkill screen

https://docs.micropython.org/en/latest/reference/pyboard.py.html#running-a-command-on-the-device

https://raspberrypi-guide.github.io/programming/install-opencv


sudo raspi-config
