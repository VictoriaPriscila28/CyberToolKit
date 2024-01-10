import os
from scapy.all import rdpcap

def read_pcap_file(filepath):
    try:
        # Carrega os pacotes do arquivo .pcap
        packets = rdpcap(filepath)

        # Itera sobre cada pacote e imprime suas informações
        for packet in packets:
            print(packet.summary())
            # Você pode adicionar mais detalhes aqui se necessário

    except FileNotFoundError:
        print(f"Arquivo {filepath} não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo .pcap: {e}")


def read_pcap_files():
    try:
        files = [f for f in os.listdir("captura_tcpdump") if f.endswith('.pcap')]
        if not files:
            print("Nenhum arquivo .pcap encontrado.")
            return

        print("\nArquivos .pcap disponíveis:")
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")

        file_choice = int(input("Escolha o número do arquivo para ler: ")) - 1

        if 0 <= file_choice < len(files):
            read_pcap_file(os.path.join("captura_tcpdump", files[file_choice]))
        else:
            print("Número de arquivo inválido.")

    except FileNotFoundError:
        print("Pasta 'captura_tcpdump' não encontrada.")
    except ValueError:
        print("Entrada inválida, por favor digite um número.")