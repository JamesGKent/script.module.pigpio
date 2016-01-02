from .pigpio import *
import os, subprocess

pigpio_path = os.path.realpath(__file__).replace(os.path.join("pigpio",os.path.basename(__file__)), "")
daemon_file = os.path.join(pigpio_path, "pigpiod")

def check_if_running():
	args = "pidof pigpiod"
	p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
	output, err = p.communicate()
	pids = output.split("\n")
	for pid in pids:
		if pid != "":
			try:
				p = int(pid)
				return True
			except ValueError:
				pass
	return False

#def check_autostart():
#	return False

#def make_autostart():
#	pass

def start_now(): # start the system daemon if its not already running
	if not check_if_running():
		command = [daemon_file, "-s", "10"]
		subprocess.Popen(command, env=os.environ)

start_now()