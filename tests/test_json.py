import json

dados = {
    "nome": "Alai",
    "idade": 25
}

# Guardas dados em um arquivo JSON
with open("teste.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print("Dados salvos no arquivo teste.json")


# Lê os dados do arquivo JSON
try:
    with open("teste.json", "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)
        print("Dados lidos do arquivo teste.json:")
        print(dados_lidos)
except FileNotFoundError:
    print("O arquivo teste.json não foi encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON.")


# Quero que compreendas estas diferenças
# - "w": abre o ficheiro para escrita. Se já existir, substitui o conteúdo.
# - "r": abre o ficheiro para leitura.
# - encoding="utf-8": permite trabalhar corretamente com caracteres especiais.
# - with: garante que o ficheiro é fechado automaticamente.
# - json.dump(): escreve no ficheiro.
# - json.load(): lê do ficheiro.