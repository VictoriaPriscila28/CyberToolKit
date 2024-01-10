import json
import os
import shutil

def save_results(data, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = os.path.join(folder, filename)

    # Verifica se 'data' é um caminho de arquivo válido
    if isinstance(data, str) and os.path.isfile(data):
        # Se 'data' é um caminho de arquivo, move o arquivo
        shutil.move(data, filepath)
    else:
        # Caso contrário, assume que 'data' é uma estrutura de dados e a salva como JSON
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Resultados salvos em: {filepath}")