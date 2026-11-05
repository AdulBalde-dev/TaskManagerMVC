from services.tarefa_service import TarefaService
from models.tarefa import Tarefa
from models.prioridade import Prioridade
from models.categoria import Categoria
from datetime import datetime

class TarefaController:
    def __init__(self, service: TarefaService):
        self.service = service

    def adicionar_tarefa(
        self,
        titulo: str,
        descricao: str = "",
        prioridade: Prioridade = Prioridade.MEDIA,
        categoria: Categoria | None = None,
        data_limite: datetime | None = None) -> Tarefa:

        return self.service.adicionar(titulo=titulo, descricao=descricao, prioridade=prioridade, categoria=categoria, data_limite=data_limite)

    def listar_tarefas(self) -> list[Tarefa]:
        return self.service.listar_todas()

    def obter_tarefa(self, tarefa_id: int) -> Tarefa | None:
        return self.service.obter_por_id(tarefa_id)

    def atualizar_tarefa(self, tarefa_id: int, **dados) -> Tarefa:
        return self.service.atualizar(tarefa_id, **dados)

    def eliminar_tarefa(self, tarefa_id: int) -> None:
        self.service.eliminar(tarefa_id)

    def concluir_tarefa(self, tarefa_id: int) -> Tarefa:
        return self.service.concluir(tarefa_id)

    def reabrir_tarefa(self, tarefa_id: int) -> Tarefa:
        return self.service.reabrir(tarefa_id)

    def pesquisar_tarefas(self, titulo: str) -> list[Tarefa]:
        return self.service.pesquisar(titulo=titulo)

    def filtrar_tarefas(self, **filtros) -> list[Tarefa]:
        return self.service.filtrar(**filtros)