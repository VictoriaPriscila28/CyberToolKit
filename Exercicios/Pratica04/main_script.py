import warnings
warnings.filterwarnings("ignore")
import os
import netifaces
import pyfiglet
from dns_utils import capture_dns_queries
from port_scan_utils import scan_ports
from port_test_utils import test_open_ports_from_file
from use_tcpdump import use_tcpdump
from read_pcap_files import read_pcap_files
from analyze_sql_injection import analyze_sql_injection
from xss_analysis import test_xss
from brute_force import run_hydra
from read_ettercap import run_ettercap
from scan_active_ip import scan_active_ips
from network_attack_simulation import syn_flood
from metasploit import metasploit_scan

warnings.filterwarnings("ignore", category=RuntimeWarning, module="scapy.runtime")

def list_network_interfaces():
    interfaces = []
    for interface in netifaces.interfaces():
        addr = netifaces.ifaddresses(interface)
        # Verifica se a interface tem um endereço IPv4
        if netifaces.AF_INET in addr:
            interfaces.append(interface)
    return interfaces

def select_file_from_folder(folder):
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Pasta '{folder}' não encontrada.")
        return None

    print(f"\nArquivos disponíveis em {folder}:")
    for i, file in enumerate(files):
        print(f"{i + 1} - {file}")
    file_index = int(input(f"Escolha o número do arquivo de {folder}: ")) - 1

    if 0 <= file_index < len(files):
        return os.path.join(folder, files[file_index])
    else:
        print("Número de arquivo inválido.")
        return None

def main_menu():
    while True:
        header = pyfiglet.figlet_format("Cyber ToolKit")
        print(header)

        # Menu estilizado
        print("╔═══════════════════════════════╗")
        print("║ Escolha uma opção:            ║")
        print("║ 1. Consultas DNS              ║")
        print("║ 2. Consultas PORTAS           ║")
        print("║ 3. Consultas PORTAS ABERTAS   ║")
        print("║ 4. Consulta SQL Injection     ║")
        print("║ 5. XSS                        ║")
        print("║ 6. Brute Force                ║")
        print("║ 7. Consulta PACOTES           ║")
        print("║ 8. Ler arquivo .pcap          ║")
        print("║ 9. Usar Ettercap (ARP Poison) ║")
        print("║ 10. DoS Attack                ║")
        print("║ 11. Metasploit                ║")
        print("║ 12. Sair                      ║")
        print("╚═══════════════════════════════╝")

        choice = input("→ Digite sua escolha (1-12): ")

        if choice == "1":
            capture_dns_queries()
        elif choice == "2":
            scan_ports()
        if choice == "3":
            try:
                files = os.listdir("varredura_portas")
                print("\nArquivos disponíveis:")
                for i, file in enumerate(files):
                    print(f"{i + 1}. {file}")
                file_index = int(input("Escolha o número do arquivo: ")) - 1
                if 0 <= file_index < len(files):
                    test_open_ports_from_file(files[file_index])
                else:
                    print("Número de arquivo inválido.")
            except FileNotFoundError:
                print("Pasta 'varredura_portas' não encontrada.")
            except ValueError:
                print("Entrada inválida, por favor digite um número.")
        elif choice == "4":
            analyze_sql_injection()
        elif choice == "5":
            test_xss()
        elif choice == '6':
            password_file_path = select_file_from_folder("passwords")
            user_file_path = select_file_from_folder("users")
            if password_file_path and user_file_path:
                target_url = input('Digite a URL ou IP do alvo: ')
                service_module = input('Digite o módulo do serviço (ex: http-form-post): ')
                login_page = input('Digite a página de login (ex: /userinfo.php): ')
                params1 = input('Digite o primeiro parâmetro (ex: username): ')
                params2 = input('Digite o segundo parâmetro (ex: password): ')
                fail_condition = input('Digite a condição de falha (login page): ')
                print('\n')
                run_hydra(target_url, user_file_path, password_file_path, service_module, login_page, params1, params2, fail_condition)
            else:
                print("Erro ao selecionar os arquivos de usuário e senha.")
        if choice == "7":
            interfaces = list_network_interfaces()
            print("Interfaces de Rede Disponíveis:")
            for i, iface in enumerate(interfaces):
                print(f"{i + 1}. {iface}")

            iface_choice = int(input("Escolha a interface de rede (número): ")) - 1
            if 0 <= iface_choice < len(interfaces):
                interface = list(interfaces)[iface_choice]
                filter_expression = input("Digite a expressão de filtro (ex: 'port 80'): ")
                packet_count = int(input("Digite o número de pacotes a capturar: "))
                use_tcpdump(interface, filter_expression, packet_count)
            else:
                print("Escolha de interface inválida.")
        elif choice == "8":
            read_pcap_files()
        elif choice == "9":
            network = "192.168.1.0/24"
            active_ips = scan_active_ips(network)
            print("IPs Ativos na Rede:", active_ips)

            target_ip = input("Digite o endereço IP do alvo: ")
            gateway_ip = input("Digite o endereço IP do gateway: ")
            interfaces = list_network_interfaces()
            print("Interfaces de Rede Disponíveis:")
            for i, iface in enumerate(interfaces):
                print(f"{i + 1}. {iface}")

            iface_choice = int(input("Escolha a interface de rede (número): ")) - 1
            if 0 <= iface_choice < len(interfaces):
                interface = list(interfaces)[iface_choice]
                run_ettercap(target_ip, gateway_ip, interface)
            else:
                print("Escolha de interface inválida.")
        elif choice == "10":
            target_ip = input("Digite o IP do alvo: ")
            target_port = int(input("Digite a porta do alvo: "))
            duration = int(input("Digite a duração do ataque (em segundos): "))
            syn_flood(target_ip, target_port, duration)
        elif choice == "11":
            target_ip = input("Digite o IP do alvo para o pentest: ")
            metasploit_scan(target_ip)
        elif choice == "12":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, por favor, escolha novamente.")

if __name__ == "__main__":
    main_menu()