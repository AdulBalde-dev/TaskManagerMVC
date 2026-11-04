from datetime import datetime
from models.prioridade import Prioridade
from models.categoria import Categoria

class Tarefa:
    # = None caso não seja fornecido o valor padrão sera None.
    def __init__(self, id: int, titulo: str, descricao: str = "", prioridade: Prioridade = Prioridade.MEDIA, categoria: Categoria | None = None, data_limite: datetime | None = None):

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
        self.data_limite = data_limite



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
    def categoria(self) -> Categoria:
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

    @property
    def data_limite(self) -> datetime | None:
        return self._data_limite


    @data_limite.setter
    def data_limite(self, nova_data_limite: datetime | None) -> None:
        # se se tivermos uma nova data limite e ela não for uma instância de datetime, lança um TypeError.
        if nova_data_limite is not None and not isinstance(nova_data_limite, datetime):
            raise TypeError("A data limite da tarefa deve ser uma instância de datetime ou None.")
        self._data_limite = nova_data_limite

    def esta_atrasada(self) -> bool:
        if self.data_limite is None:
            return False

        # Se a tarefa já foi concluída, não a consideramos atrasada.
        if self.concluida:
            return False

        # se a data de hoje for maior que a data limite, a tarefa está atrasada.
        data_hoje = datetime.now()
        return data_hoje > self.data_limite

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, novo_id: int) -> None:
        # or isinstance(novo_id, bool) no python, pois bool é subtipo de int, e nao queremos aceitar booleanos como ID.
        if not isinstance(novo_id, int) or isinstance(novo_id, bool):
            raise TypeError("O ID da tarefa deve ser um inteiro.")


        if novo_id <= 0:
            raise ValueError("O ID da tarefa deve ser um número positivo.")

        self._id = novo_id

    def to_dict(self) -> dict:
        # isoformat é usado para converter objetos datetime em strings no formato ISO 8601. pq JSON não suporta diretamente objetos datetime.
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade.value,
            "categoria": {
                "nome": self.categoria.nome,
                "descricao": self.categoria.descricao
            },
            "concluida": self.concluida,
            "data_limite": self.data_limite.isoformat() if self.data_limite else None,
            "data_criacao": self.data_criacao.isoformat()
        }

    @classmethod
    def from_dict(cls, dados: dict):
        tarefa = cls(
            id=dados["id"],
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            prioridade=Prioridade(dados["prioridade"]),
            categoria=Categoria(
                nome=dados["categoria"]["nome"],
                descricao=dados["categoria"]["descricao"]
            ),

            data_limite=datetime.fromisoformat(dados["data_limite"]) if dados["data_limite"] else None)
        tarefa._concluida = dados.get("concluida", False)
        tarefa.data_criacao = datetime.fromisoformat(dados["data_criacao"])
        
        return tarefa
