from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QDateEdit,
    QPushButton,
    QFormLayout,
    QVBoxLayout
)
from PySide6.QtCore import Qt

from PySide6.QtCore import QDate


class TaskDialog(QDialog):

    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.setWindowTitle("Adicionar tarefa")
        self.resize(450, 400)

        # Layout principal
        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        # Título do formulário
        self.titulo = QLabel("Criar nova tarefa")
        self.layout_principal.addWidget(self.titulo, alignment=Qt.AlignmentFlag.AlignCenter)

        #################################
        # Formulário de criação de tarefa
        #################################
        self.formulario = QFormLayout()

        # Campo do título
        self.input_titulo = QLineEdit(placeholderText="teste")
        self.formulario.addRow("Título:", self.input_titulo)

        # Campo da descrição
        self.input_descricao = QTextEdit()
        self.formulario.addRow("Descrição:", self.input_descricao)

        # Campo da prioridade
        self.input_prioridade = QComboBox()
        self.input_prioridade.addItems(["Baixa", "Média", "Alta", "Urgente"])

        self.formulario.addRow("Prioridade:", self.input_prioridade)
        # Campo da categoria
        self.input_categoria = QLineEdit()
        self.formulario.addRow("Categoria:", self.input_categoria)

        # Campo da data limite
        self.input_data = QDateEdit()
        # permitir seleção de data pelo calendário
        self.input_data.setCalendarPopup(True)
        # definir a data atual como padrão
        self.input_data.setDate(QDate.currentDate())
        self.formulario.addRow("Data limite:", self.input_data)

        # Adicionar o formulário ao layout principal
        self.layout_principal.addLayout(self.formulario)

        # Botão guardar
        self.btn_guardar = QPushButton("Guardar tarefa")
        self.layout_principal.addWidget(self.btn_guardar)

import sys
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = TaskDialog()
    janela.show()

    sys.exit(app.exec())