from repositories.tarefa_repository import TarefaRepository
from services.tarefa_service import TarefaService
from controllers.tarefa_controller import TarefaController
from views.tarefa_view import TarefaView


def main() -> None:
    # 1. Criar o Repository
    repositorio = TarefaRepository("data/tarefas.json")

    # 2. Criar o Service
    service = TarefaService(repositorio)

    # 3. Criar o Controller
    controller = TarefaController(service)

    # 4. Criar a View
    view = TarefaView(controller)

    # 5. Iniciar a aplicação
    view.executar()


if __name__ == "__main__":
    main()
