from utils import save_result
import subprocess
def run_command(command):
    process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    return  stdout.decode("utf-8"), stderr.decode("utf-8")

def analyze_sql_injection():
    url = input("digite a url a ser analizada")
    print(f"analizando... {url}")
    output, error = run_command("sqlmap -u '{url}'--batch --dbs")

    if error:
        print(f'o erro: {error}')
    else:
        print(output)
        save = input("Deseja salvar o resultado? (s/n) ")
        if save == "s":
            organized = organized_output(url)
            date_to_save ={
                'url': url,
                "output": output
            }
            save_result(date_to_save, 'sql_injection', f"sql_injection_{organized}.json")

    pass: