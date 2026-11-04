import json
from pathlib import Path
from models.tarefa import Tarefa


class TarefaRepository:

    def __init__(self, caminho: str = "data/tarefas.json"):
        self.caminho = Path(caminho)
        
        self._garantir_arquivo_existente()


    def carregar(self) -> list[Tarefa]:
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                # Lê os dados do arquivo JSON e retorna como lista de tarefas.
                dados = json.load(arquivo)
                tarefas = [Tarefa.from_dict(dado) for dado in dados]
                return tarefas
        except FileNotFoundError:
            print(f"O arquivo {self.caminho} não foi encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo {self.caminho}.")
            return []
        
    def _garantir_arquivo_existente(self) -> None:
        # parents=True: cria também as pastas intermédias, se necessário.
        # exist_ok=True: não provoca erro se a pasta já existir.
        self.caminho.parent.mkdir(parents=True, exist_ok=True)
        # Verifica se o ficheiro ainda não existe.
        if not self.caminho.exists():
            with open(self.caminho, "w", encoding="utf-8") as arquivo:
                json.dump([], arquivo, indent=4, ensure_ascii=False)
                print(f"Arquivo {self.caminho} criado com sucesso.")


    def guardar(self, tarefas: list[Tarefa]) -> None:
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            dados = [tarefa.to_dict() for tarefa in tarefas]
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"Arquivo {self.caminho} salvo com sucesso.")