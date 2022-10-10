import os

while True:
    hostname = "github.com"
    response = os.system(" ping -c 1 " + hostname)
    if response == 0:
        print(hostname, "UP")
    else:
        print(hostname, "DOWN")
    print("END\n")
