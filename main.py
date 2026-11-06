from pathlib import Path

from PySide6.QtWidgets import QApplication
from repositories.tarefa_repository import TarefaRepository
from services.tarefa_service import TarefaService
from controllers.tarefa_controller import TarefaController
from views.gui.main_window import MainWindow
import sys

def main() -> None:

    # Diretório principal do projeto
    BASE_DIR = Path(__file__).resolve().parent

    # Caminho do ficheiro JSON
    DATA_FILE = BASE_DIR / "data" / "tarefas.json"

    # Inicializar o backend
    repositorio = TarefaRepository(str(DATA_FILE))

    service = TarefaService(repositorio)

    controller = TarefaController(service)

    # Inicializar a aplicação gráfica
    app = QApplication(sys.argv)

    # Criar a janela principal e entregar-lhe o Controller
    window = MainWindow(controller)

    # Mostrar a janela
    window.show()

    # Iniciar o ciclo de eventos
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

