import socket
import time
import wave

import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

player = pyaudio.PyAudio()


WAVE_OUTPUT_FILENAME = "output_2.wav"
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(player.get_sample_size(FORMAT))
wf.setframerate(RATE)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = "127.0.0.1"#socket.gethostbyname("samuel-p34v5")

# bind the socket to the port 23456, and connect
server_address = (ip_address, 2000)  
sock.connect(server_address)  
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

continuer = True

while continuer:
	try:
		#player.play(sock.recv(2048))
		wf.writeframes(sock.recv(2048))		
	except Exception as e:
		#print(e)
		continuer = False

sock.close()
wf.close()
