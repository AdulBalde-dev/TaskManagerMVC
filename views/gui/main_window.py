# ==========================================
# 1. IMPORTAÇÕES
# ==========================================

import sys  # Permite aceder a argumentos e funcionalidades do sistema operativo.

# Importamos os componentes gráficos que vamos utilizar.
from PySide6.QtWidgets import (
    QApplication,  # Gere a aplicação gráfica e os seus eventos.
    QMainWindow,   # Cria a janela principal.
    QWidget,       # Cria um componente que pode servir de contentor.
    QLabel,        # Apresenta textos na interface.
    QPushButton,   # Cria botões clicáveis.
    QVBoxLayout,   # Organiza elementos verticalmente.
    QHBoxLayout,   # Organiza elementos horizontalmente.
    QFormLayout,   # Cria um layout de formulário.
    QLineEdit      # Cria campos de entrada de texto.
)

# Importamos Qt para controlar alinhamentos e outras propriedades.
from PySide6.QtCore import Qt


# ==========================================
# 2. JANELA PRINCIPAL
# ==========================================

class MainWindow(QMainWindow):

    # Construtor da nossa janela.
    def __init__(self):

        # Inicializa a classe-pai QMainWindow.
        super().__init__()
        # Define o título apresentado na barra da janela.
        self.setWindowTitle("TaskManagerMVC")
        # Define o tamanho inicial da janela: largura x altura.
        self.resize(1000, 650)


        # ==========================================
        # 3. WIDGET CENTRAL
        # ==========================================

        # Criamos um contentor para guardar os elementos da interface.
        self.container = QWidget()
        # Definimos esse contentor como a área central da janela.
        self.setCentralWidget(self.container)


        # ==========================================
        # 4. LAYOUT PRINCIPAL
        # ==========================================
        # Criamos um layout vertical.
        # Os elementos serão organizados de cima para baixo. em pé
        self.layout_principal = QVBoxLayout() 
        # Associamos o layout ao nosso contentor.
        self.container.setLayout(self.layout_principal)

        # Definimos as margens internas:
        # esquerda = 30, topo = 30, direita = 30, baixo = 30.
        self.layout_principal.setContentsMargins(30, 30, 30, 30)
        # Define o espaço entre os elementos deste layout.
        self.layout_principal.setSpacing(20)


        # ==========================================
        # 5. TÍTULO E TEXTOS
        # ==========================================

        # Criamos um texto de boas-vindas.
        self.titulo = QLabel("Bem-vindo ao TaskManagerMVC")
        # Criamos o subtítulo da aplicação.
        self.subtitulo = QLabel("Organize as suas tarefas e aumente a produtividade.")
        # Criamos um texto para a secção de tarefas.
        self.tarefas = QLabel("As suas tarefas começam aqui!")
        # Criamos um texto para o status das tarefas.
        self.status = QLabel("Status: Nenhuma tarefa adicionada.")

        # Adicionamos o título ao layout e centralizamos horizontalmente.
        self.layout_principal.addWidget(self.titulo, alignment=Qt.AlignmentFlag.AlignCenter)
        # Adicionamos o subtítulo ao layout principal.
        self.layout_principal.addWidget(self.subtitulo, alignment=Qt.AlignmentFlag.AlignRight)
        # Adicionamos esse texto ao layout principal.
        self.layout_principal.addWidget(self.tarefas)
        # Adicionamos o status das tarefas ao layout principal.
        self.layout_principal.addWidget(self.status)


        # ==========================================
        # 6. LAYOUT DOS BOTÕES
        # ==========================================

        # Criamos um layout horizontal. deitado, ou seja, os elementos ficam lado a lado.
        # Os botões ficarão organizados lado a lado.
        self.layout_botoes = QHBoxLayout()
        # Define o espaço entre os botões.
        self.layout_botoes.setSpacing(10)


        # ==========================================
        # 7. CRIAÇÃO DOS BOTÕES
        # ==========================================

        # Criamos o botão para adicionar tarefas.
        self.btn_adicionar = QPushButton("Adicionar tarefa")
        # Criamos o botão para listar tarefas.
        self.btn_listar = QPushButton("Listar tarefas")
        # Criamos o botão das configurações.
        self.btn_config = QPushButton("Configurações")


        # ==========================================
        # 8. LIGAÇÃO DOS BOTÕES ÀS FUNÇÕES
        # ==========================================

        # Quando o botão Adicionar for clicado,
        # executamos o método adicionar_tarefa().
        self.btn_adicionar.clicked.connect(self.adicionar_tarefa)
        # Quando o botão Listar for clicado,
        # executamos o método listar_tarefas().
        self.btn_listar.clicked.connect(self.listar_tarefas)
        # Quando o botão Configurações for clicado,
        # executamos o método configurar().
        self.btn_config.clicked.connect(self.configurar)


        # ==========================================
        # 9. ADICIONAR OS BOTÕES AO LAYOUT
        # ==========================================

        # Colocamos o primeiro botão no layout horizontal.
        self.layout_botoes.addWidget(self.btn_adicionar)
        # Colocamos o segundo botão no layout horizontal.
        self.layout_botoes.addWidget(self.btn_listar)
        # Colocamos o terceiro botão no layout horizontal.
        self.layout_botoes.addWidget(self.btn_config)

        # Adicionamos o layout horizontal dos botões
        # ao layout vertical principal.
        self.layout_principal.addLayout(self.layout_botoes)

        ######################################
        # 9.1. FORMULÁRIO DE ADIÇÃO DE TAREFAS
        ###############################
        # Criamos um formulário para adicionar tarefas.
        self.formulario = QFormLayout() # cria o layout de formulário
        
        self.formulario.setContentsMargins(0, 50, 500, 50) # define as margens do formulário (esquerda, cima, direita, baixo)
        self.formulario.setSpacing(50) # define o espaçamento entre os campos do formulário

        self.input_titulo = QLineEdit() # input para o título da tarefa
        self.input_descricao = QLineEdit() # input para a descrição da tarefa

        self.formulario.addRow("Título:", self.input_titulo) # adiciona o campo de título ao formulário
        self.formulario.addRow("Descrição:", self.input_descricao) # adiciona o campo de descrição ao formulário

        self.layout_principal.addLayout(self.formulario)

    # ==========================================
    # 10. FUNÇÕES DOS BOTÕES
    # ==========================================

    # Função executada quando clicamos em Adicionar tarefa.
    def adicionar_tarefa(self):
        print("O botão Adicionar tarefa foi clicado!")

    # Função executada quando clicamos em Listar tarefas.
    def listar_tarefas(self):
        print("O botão Listar tarefas foi clicado!")

    # Função executada quando clicamos em Configurações.
    def configurar(self):
        print("O botão Configurações foi clicado!")


# ==========================================
# 11. FUNÇÃO PRINCIPAL
# ==========================================

def main():

    # Criamos a aplicação gráfica.
    app = QApplication(sys.argv)

    # Criamos uma instância da nossa janela principal.
    window = MainWindow()

    # Tornamos a janela visível.
    window.show()

    # Iniciamos o ciclo de eventos da aplicação.
    # A aplicação permanece aberta até o utilizador a fechar.
    sys.exit(app.exec())


# ==========================================
# 12. PONTO DE ENTRADA
# ==========================================

# Verificamos se este ficheiro está a ser executado diretamente.
if __name__ == "__main__":

    # Se estiver, iniciamos a aplicação.
    main()