from subprocess import Popen, PIPE
from utils import save_results

def sanitize_filename(filename):
    return "".join(c if c.isalnum() else "_" for c in filename)

def run_command(command):
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

def analyze_sql_injection():
    url = input("Digite a URL para análise de SQL Injection: ")
    print("Executando análise de SQL Injection com sqlmap...")
    output, error = run_command(f'sqlmap -u "{url}" --batch')

    if error:
        print("Error:", error)
    else:
        print(output)
        save = input("Deseja salvar os resultados? (s/n): ")
        if save.lower() == 's':
            sanitized_url = sanitize_filename(url)
            data_to_save = {
                "url": url,
                "output": output
            }
            save_results(data_to_save, "sql_injection_results", f"sql_injection_{sanitized_url}.json")
            print(f"Resultados da análise de SQL Injection salvos.")