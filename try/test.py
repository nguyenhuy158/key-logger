import socket

# Get the hostname of the current computer
hostname = socket.gethostname()

# Print the hostname
print("Current computer name:", hostname)
print("Current computer name:", socket.getsockname())