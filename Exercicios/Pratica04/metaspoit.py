import time
from pymetasploit3.msfrpc import MsfRpcClient

def metasploit_scan(target_ip):
    client = MsfRpcClient('s3nh4@123', ssl=True)  # 'password' é a senha do servidor msfrpcd do Metasploit
    #client = MsfRpcClient('password', ssl=True)
    scanner = client.modules.use('auxiliary', 'scanner/portscan/tcp')
    scanner['RHOSTS'] = target_ip
    scanner['THREADS'] = 10

    scan_id = scanner.execute()
    job_id = scan_id['job_id']

    # Aguardar a conclusão do trabalho
    while client.jobs.list.get(job_id):
        print(f"Aguardando a conclusão da varredura... (Job ID: {job_id})")
        time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente

    print("Varredura concluída.")
    scan_result = client.sessions.list.get(job_id)
    print(scan_result)

    client.logout()