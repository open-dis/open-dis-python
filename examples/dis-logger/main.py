from scapy.all import sniff
import threading
from app import *

from opendis.dis7 import *
from opendis.RangeCoordinates import *
from opendis.PduFactory import createPdu

app = None
gps = GPS()
quitEvent = threading.Event()

class DISMessageInfo:
    def __init__(self, pdu, src_addr, dst_addr, src_port, dst_port):
        self.src_addr = src_addr
        self.dst_addr = dst_addr
        self.src_port = src_port
        self.dst_port = dst_port

        pduTypeName = pdu.__class__.__name__
        self.type = pduTypeName
        self.type_number = pdu.pduType

        # PduTypeDecoders.EntityStatePdu is type 1
        if pdu.pduType == 1:
            loc = (pdu.entityLocation.x, 
                pdu.entityLocation.y, 
                pdu.entityLocation.z,
                pdu.entityOrientation.psi,
                pdu.entityOrientation.theta,
                pdu.entityOrientation.phi
            )
            try:
                body = gps.ecef2llarpy(*loc)
            except:
                body = [0,0,0]

            self.latitude = rad2deg(body[0])
            self.longitude = rad2deg(body[1])
            self.altitude = body[2]

            marking_asci = list(pdu.marking.characters)
            marking_string = ""

            print(marking_asci)
            for i in marking_asci:
                try:
                    if i == 0:
                        break

                    marking_string += chr(i)
                except Exception:
                    break

            self.entityID = pdu.entityID.entityNumber
            self.marking = marking_string

    def __str__(self):
        if self.type_number == 1:
            return ("Received {}\n".format(self.type)
                + " Sending   Addr.  : {}\n".format(self.src_addr)
                + " Sending   Port   : {}\n".format(self.src_port)
                + " Destination Addr.: {}\n".format(self.dst_addr)
                + " Destination Port : {}\n".format(self.dst_port)
                + " Entity Id        : {}\n".format(self.entityID)
                + " Entity Marking   : {}\n".format(self.marking)
                + " Latitude         : {:.2f} degrees\n".format(self.latitude)
                + " Longitude        : {:.2f} degrees\n".format(self.longitude)
                + " Altitude         : {:.0f} meters\n".format(self.altitude)
            )
        else:
            return ""
        

def process_packet(packet):
    """ 
        function that takes in packet, processes it into a DIS UDP message, and prints out data if
        its of EntityStatePdu type.
    """

    # Check if packet contains UDP layer
    if packet.haslayer('UDP'):
        udp_layer = packet['UDP']
        src_port = udp_layer.sport
        dst_port = udp_layer.dport

        try:
            ip_layer = packet['IP']
            src_addr = ip_layer.src
            dst_addr = ip_layer.dst
        except:
            src_addr = "None"
            dst_addr = "None"
       
        # DIS traffic only on port 3000
        if dst_port == 3000:
            data = bytes(udp_layer.payload)

            pdu = createPdu(data)
            message_info = DISMessageInfo(pdu, src_addr, dst_addr, src_port, dst_port)
            if app != None:
                app.add_entry(message_info)
            print(message_info)


def stop_sniffing(x):
    return quitEvent.is_set()


def sniff_for_traffic():
    print("Listening for DIS traffic...")
    sniff(filter="udp and multicast", prn=process_packet, stop_filter=stop_sniffing)


def main():
    global app
    sniff_thread = threading.Thread(target=sniff_for_traffic)
    sniff_thread.start()
    
    try:
        app = App()
        app.mainloop()
    except:
        quitEvent.set()

    quitEvent.set()
    sniff_thread.join()

if __name__=="__main__":
    main()