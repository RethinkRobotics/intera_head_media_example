import socket
import sys

#Default settings
start_delimiter = ";" # Sawyer signal start delimiter
DEFAULT_SAWYER_IP = "172.20.30.188"
DEFAULT_SAWYER_PORT =  "4000"
DEFAULT_SERVER_IP = "172.20.30.90"
DEFAULT_SERVER_PORT = "3007"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)   # 5 seconds

print ("This is a TCP/IP media sender script for sawyer")
print ("Please type the following details or press enter to use default value")
SAWYER_IP = input("Enter Sawyer IP Address: [Default: " + DEFAULT_SAWYER_IP + "]") or DEFAULT_SAWYER_IP
SAWYER_PORT = input("Enter Sawyer Device Port Number: [Default: " + DEFAULT_SAWYER_PORT + "]") or DEFAULT_SAWYER_PORT
SERVER_IP = input("Enter Media Server IP Address: [Default: " + DEFAULT_SERVER_IP + "]") or DEFAULT_SERVER_IP
SERVER_PORT = input("Enter Media Server Port Number: [Default: " + DEFAULT_SERVER_PORT + "]") or DEFAULT_SERVER_PORT

server_address = (SAWYER_IP, int(SAWYER_PORT))
print('Connecting to the sawyer @ {} on port {}'.format(*server_address))
try:
    # Connect the socket to the port where the sawywer is listening
    sock.connect(server_address)
except socket.error as msg:
    print ("Caught exception Socket Error: %s" % msg)
    print ("Error when connecting to the sawyer. Exiting this script")
    exit()
    
print("Connection succeded! (press Ctrl+C anytime to quit)")
print("")
print("")

while True:
    filename = input("Enter filename (for example \"4.mp4\"): ")
    message = start_delimiter + 'http://' +  SERVER_IP + ":" + SERVER_PORT + "/" + filename
    print('sending {!r}'.format(message))
    sock.send(bytes(message, "utf8"))
