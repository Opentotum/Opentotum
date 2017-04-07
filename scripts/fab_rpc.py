import socket
import time
import sys
import json
import threading

from ws4py.client.threadedclient import WebSocketClient


class WSClient(WebSocketClient):
    def __init__(self, *args, **kwargs):
        super(WSClient, self).__init__(*args, **kwargs)
        address = args[0]
        port_position = len(address)-address.find(":9001")
        self._prompt = "fab@%s>" % address[5:-port_position]
        
    def opened(self):
        print "Handshake successful"
        sys.stdout.write(self._prompt+" ")
        t = threading.Thread(target=self.push_message, args=(self,))
        t.start()

    @classmethod
    def push_message(_, cls):
        message = {
            "name": "serial",
            "data": {
                "func": "mdi",
                "feedrate": 10000,
                "step": 10,
                "z_step": 5,
                "extruderFeedrate": 3048.16,
                "value": "\r\n"
            }
        }

        while True:
            string = raw_input().strip()
            if string:
                message['data']['value'] = ("%s\r\n" % string)
                cls.send(json.dumps(message))

    def received_message(self, message):
        message = json.loads(str(message))
        if message["type"] == "serial":
            print message["data"]["response"]
            sys.stdout.write(self._prompt+" ")

    def closed(self, code, reason=None):
        print "Closed down", code, reason

if __name__ == '__main__':
    try:
        ip = raw_input("IP: ")
        ws = WSClient('ws://%s:9001/' % ip, protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
