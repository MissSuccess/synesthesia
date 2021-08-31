from pythonosc.udp_client import SimpleUDPClient

LANBOX_IP_ADDRESS = "192.168.1.77"
LANBOX_UDP_PORT = 4777

client = SimpleUDPClient(LANBOX_IP_ADDRESS, LANBOX_UDP_PORT)  # Create client

#trying to send message to layer D / layer 4. cuelist 302, cue step 2
try:
    client.send_message("/4", [302 , 2])  # Send message with int, float and string
except:
    print("Error has happened")
