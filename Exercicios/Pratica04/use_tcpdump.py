from scapy.all import sniff, wrpcap
import datetime
from utils import save_results


def use_tcpdump(interface, filter_expression, packet_count):
    captured_packets = []

    def packet_handler(packet):
        print(packet.show())
        captured_packets.append(packet)

    try:
        print(f"Iniciando a captura de pacotes na interface {interface}. Pressione CTRL+C para interromper.")
        sniff(iface=interface, filter=filter_expression, prn=packet_handler, count=packet_count, store=0)
    except Exception as e:
        print(f"Erro ao capturar pacotes: {e}")
    finally:
        save = input("Deseja salvar os resultados? (s/n): ")
        if save.lower() == 's':
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"captura_{interface}_{timestamp}.pcap"
            wrpcap(filename, captured_packets)
            save_results(filename, "captura_tcpdump", f"capturas_tcpdump_{timestamp}.pcap")
            print(
                f"Captura de pacotes finalizada. Pacotes salvos em: captura_tcpdump/capturas_tcpdump_{timestamp}.pcap")
            print(">>> Use a opção 8 para ler os arquivos .pcap gerados <<<")
