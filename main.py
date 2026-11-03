from models.tarefa import Tarefa
from models.prioridade import Prioridade
from models.categoria import Categoria

def main():
    print('=' * 40)
    print('       Welcome to Task Manager')
    print('=' * 40)

    categoria_estudos = Categoria("ESTUDOS", "Categoria para estudos")

    tarefa = Tarefa(
        id=1,
        titulo="Estudar Python",
        descricao="Estudar Programação Orientada a Objetos",
        prioridade=Prioridade.URGENTE,
        categoria=categoria_estudos)

    print(tarefa.titulo)
    print(tarefa.descricao)
    print(tarefa.prioridade.value)
    print(tarefa.concluida)
    print(tarefa.data_criacao)
    print(tarefa.data_limite)
    print(tarefa.categoria.nome)
    tarefa.concluir()
    print(tarefa.concluida)
    tarefa.reabrir()
    print(tarefa.concluida) 


if __name__ == '__main__':
    main()