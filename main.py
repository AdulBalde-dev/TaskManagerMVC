from repositories.tarefa_repository import TarefaRepository
from services.tarefa_service import TarefaService
from controllers.tarefa_controller import TarefaController
from views.cli.tarefa_view import TarefaView


def main() -> None:
    # 1. Criar o Repository indicando o arquivo JSON de armazenamento
    repositorio = TarefaRepository("data/tarefas.json")

    # 2. Criar o Service indicando o Repository criado acima
    service = TarefaService(repositorio)

    # 3. Criar o Controller indicando o Service criado acima
    controller = TarefaController(service)

    # 4. Criar a View indicando o Controller criado acima
    view = TarefaView(controller)

    # 5. Iniciar a aplicação
    view.executar()


if __name__ == "__main__":
    main()
