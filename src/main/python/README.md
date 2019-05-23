This is an implementation of DIS 7 in Python3.

First, install the dis library from the src/main/python folder using:

```bash
sudo python3 setup.py install
```

or

```bash
python3 setup.py install --user
```

to install to your personal python installation area.

To run, cd to dis_network_example and run the receiver:

```bash
python3 dis_receiver.py
```

and in another terminal, run the sender:

```bash
python dis_udp.py
```

You should also see the traffic on the net in wireshark
on your localhost interface.
