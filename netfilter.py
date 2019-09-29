
import netfilterqueue

def process_packet(packet):
	print(packet)
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
