# -*- coding: utf-8 -*-
import socket
import os, os.path

usock_path = "/var/www/temp/task_usock"

if os.path.exists(usock_path):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(usock_path)
    print "Ready."
    print "Ctrl-C to quit."
    while True:
        try:
            x = raw_input("> ").strip()
            if x:
                print "SENT:", x
                client.send("%s\n" % x)
        except KeyboardInterrupt, k:
            print "Shutting down."
            break
    client.close()
else:
    print "Couldn't Connect!"
print "Done"
