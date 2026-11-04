from models.tarefa import Tarefa
from models.prioridade import Prioridade
from models.categoria import Categoria
from datetime import datetime
from repositories.tarefa_repository import TarefaRepository
import json
from services.tarefa_service import TarefaService


def main():
    tarefa1 = Tarefa(
        id=3,
        titulo="Estudar Python",
        descricao="Estudar Programação Orientada a Objetos",
        prioridade=Prioridade.URGENTE,
        categoria=Categoria("ESTUDOS", "Categoria para estudos"),
        data_limite=datetime(2026, 11, 4)
    )

    repositorio = TarefaRepository()
    service = TarefaService(repositorio)
    resultado = service.filtrar(prioridade=Prioridade.URGENTE)
    for tarefa in resultado:
        print(f"ID: {tarefa.id}, Título: {tarefa.titulo}, Prioridade: {tarefa.prioridade}, Categoria: {tarefa.categoria.nome}, Data Limite: {tarefa.data_limite}, Concluída: {tarefa.concluida}")


if __name__ == '__main__':
    main()