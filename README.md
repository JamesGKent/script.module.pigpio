# RPi2-kodi-pigpio
Add the pigpio library to kodi on the raspberry pi 2 for I/O purposes
the pigpio library is maintained separately here:
http://abyz.co.uk/rpi/pigpio/

on openelec the pigpio library should be started by creating an autostart file:
/storage/.config/autostart.sh

with the following contents:
(
 /storage/.kodi/addons/script.module.pigpio-master/lib/pigpiod -s 10
)

Where enclosing the command in brackets indicates that the shell should not wait for it to finish executing (as it's a system daemon it won't exit)
and the -s 10 indicates the sample rate, as it's most likely going to be used for low speed I/O a low sample rate is desirable to limit CPU usage.
at the time of writing the possible values are 1, 2, 4, 5, 8 and 10 in microseconds.

If the system daemon is not running when the library is imported it will try and start the system daemon.