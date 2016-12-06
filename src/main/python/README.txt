This is an implementation of DIS 7 in Python. Not terribly
well tested or anything, but the basics of at least the
ESPDU are present.

To run, cd to dis_network_example and run the sender:

./dis_udp.py

and the receiver:

./dis_receiver.py

You should also see the traffic on the net in wireshark.

You'll probably have to change the destination address
in the sender:

UDP_PORT = 3000
DESTINATION_ADDRESS = "172.20.159.255"

and in the receiver:

UDP_PORT = 3001
DESTINATION_ADDRESS = "172.20.159.255"
LOCAL_IP = "172.20.152.34"

