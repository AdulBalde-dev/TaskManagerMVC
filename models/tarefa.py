from datetime import datetime
from models.prioridade import Prioridade
from models.categoria import Categoria

class Tarefa:
    def __init__(self, id: int, titulo: str, descricao: str = "", prioridade: Prioridade = Prioridade.MEDIA, categoria: Categoria | None = None):

        # Verifica se o título da tarefa é válido
        # o setter do título já fará a validação, então não precisamos validar aqui no construtor.
        # if not titulo or not titulo.strip():
        #     raise ValueError("O título da tarefa não pode ser vazio.")

        self.id = id
        self.titulo = titulo # Usa o setter para validar o título
        self.descricao = descricao
        self.prioridade = prioridade
        # Se a categoria for fornecida, usa-a; caso contrário, cria uma categoria padrão "Geral".
        self.categoria = categoria if categoria is not None else Categoria("Geral")
        self._concluida = False
        self.data_criacao = datetime.now()
        self.data_limite = None



    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo: str):
        if not isinstance(novo_titulo, str):
            raise TypeError("O título da tarefa deve ser uma string.")

        # Remove espaços em branco no início e no fim do título.
        novo_titulo = novo_titulo.strip()

        # Valida o novo título da tarefa antes de atribuí-lo.
        if not novo_titulo:
            raise ValueError("O título da tarefa não pode ser vazio.")
        
        self._titulo = novo_titulo


    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao: str):
        # Valida a nova descrição da tarefa antes de atribuí-la.
        if not isinstance(nova_descricao, str):
            raise TypeError("A descrição da tarefa deve ser uma string.")
        
        self._descricao = nova_descricao.strip()


    @property
    def prioridade(self) -> Prioridade:
        return self._prioridade

    @prioridade.setter
    def prioridade(self, nova_prioridade: Prioridade):
        if not isinstance(nova_prioridade, Prioridade):
            raise TypeError("A prioridade da tarefa deve ser uma instância de Prioridade.")
        # o self._prioridade é a prioridade atual da tarefa, que será atualizada com a nova prioridade.
        self._prioridade = nova_prioridade


    @property
    def categoria(self) -> Categoria | None:
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria: Categoria) -> None:
        # se a nova categoria não for uma instância de Categoria, lança um TypeError.
        if not isinstance(nova_categoria, Categoria):
            raise TypeError("A categoria da tarefa deve ser uma instância de Categoria.")
        self._categoria = nova_categoria


    # impedimos a modificação direta do status de conclusão da tarefa, forçando o uso dos métodos concluir e reabrir.
    @property   
    def concluida(self) -> bool:
        return self._concluida

    def concluir(self) -> None:
        if self._concluida:
            raise ValueError("A tarefa já está concluída.")
        self._concluida = True


    def reabrir(self) -> None:
        if not self._concluida:
            raise ValueError("A tarefa já está aberta.")
        self._concluida = False