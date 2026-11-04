from controllers.tarefa_controller import TarefaController
from models.tarefa import Tarefa
from models.prioridade import Prioridade
from models.categoria import Categoria
from datetime import datetime

class TarefaView:
    def __init__(self, controller: TarefaController):
        self.controller = controller


    def mostrar_menu(self) -> None:
        print("\n" + "=" * 40)
        print("             TASK MANAGER")
        print("=" * 40)
        print("  1. Adicionar tarefa")
        print("  2. Listar tarefas")
        print("  3. Consultar tarefa por ID")
        print("  4. Atualizar tarefa")
        print("  5. Eliminar tarefa")
        print("  6. Concluir tarefa")
        print("  7. Reabrir tarefa")
        print("  8. Pesquisar tarefas")
        print("  9. Filtrar tarefas")
        print("  0. Sair")
        print("=" * 40)

    def obter_opcao(self) -> str:
        return input("Escolha uma opção: ")

    def adicionar_tarefa(self) -> None:
        try:
            # Recolher informações
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")

            # Escolher prioridade
            print("\nPrioridades disponíveis:")
            print("1. Baixa")
            print("2. Média")
            print("3. Alta")
            print("4. Urgente")

            opcao = input("Escolha a prioridade [2]: ").strip()

            prioridades = {
                "1": Prioridade.BAIXA,
                "2": Prioridade.MEDIA,
                "3": Prioridade.ALTA,
                "4": Prioridade.URGENTE
            }

            prioridade = prioridades.get(opcao or "2")

            if prioridade is None:
                raise ValueError("Prioridade inválida.")

            # Recolher categoria
            nome_categoria = input("Digite a categoria: ").strip()

            categoria = (Categoria(nome_categoria) if nome_categoria else None)

            # Recolher data limite
            data_texto = input("Data limite (AAAA-MM-DD) ou Enter para ignorar: ").strip()

            data_limite = (datetime.strptime(data_texto, "%Y-%m-%d") if data_texto else None)

            # Enviar dados ao Controller
            tarefa = self.controller.adicionar_tarefa(
                titulo=titulo,
                descricao=descricao,
                prioridade=prioridade,
                categoria=categoria,
                data_limite=data_limite
            )

            print("\nTarefa adicionada com sucesso!")
            print(f"ID: {tarefa.id}")
            print(f"Título: {tarefa.titulo}")

        except (ValueError, TypeError) as erro:
            print(f"\nErro ao adicionar tarefa: {erro}")
        
    def listar_tarefas(self) -> None:
        tarefas = self.controller.listar_tarefas()

        if not tarefas:
            print("\nNão existem tarefas registadas.")
            return

        print("\n" + "=" * 45)
        print("             LISTA DE TAREFAS")
        print("=" * 45)

        for tarefa in tarefas:
            print(f"\nID: {tarefa.id}")
            print(f"Título: {tarefa.titulo}")
            print(f"Descrição: {tarefa.descricao}")
            print(f"Prioridade: {tarefa.prioridade.value}")
            print(f"Categoria: {tarefa.categoria.nome}")

            estado = "Concluída" if tarefa.concluida else "Pendente"
            print(f"Estado: {estado}")

            if tarefa.data_limite:
                print(f"Data limite: {tarefa.data_limite:%d/%m/%Y}")
            else:
                print("Data limite: Sem prazo")

            print("-" * 45)

    def consultar_tarefa(self) -> None:
        tarefa_id = int(input("Digite o ID da tarefa: "))

        tarefa = self.controller.obter_tarefa(tarefa_id)

        if tarefa is None:
            print("Tarefa não encontrada.")
            return

        print("\n========== DETALHES DA TAREFA ==========")
        print(f"ID: {tarefa.id}")
        print(f"Título: {tarefa.titulo}")
        print(f"Descrição: {tarefa.descricao}")
        print(f"Prioridade: {tarefa.prioridade.value}")
        print(f"Categoria: {tarefa.categoria.nome}")
        print(f"Estado: {'Concluída' if tarefa.concluida else 'Pendente'}")

        if tarefa.data_limite:
            print(f"Data limite: {tarefa.data_limite:%d/%m/%Y}")
        else:
            print("Data limite: Sem prazo")

        print("========================================")

    def executar(self) -> None:
        while True:
            self.mostrar_menu()
            opcao = self.obter_opcao().strip()
            if opcao == "1":
                self.adicionar_tarefa()
            elif opcao == "2":
                self.listar_tarefas()
            elif opcao == "3":
                self.consultar_tarefa()
            elif opcao == "4":
                pass
            elif opcao == "5":
                pass
            elif opcao == "6":
                pass
            elif opcao == "7":
                pass
            elif opcao == "8":
                pass
            elif opcao == "9":
                pass
            elif opcao == "0":
                print("Obrigado por utilizar o TaskManager. Até breve!")
                break
            else:
                print("Opção inválida. Tente novamente.")
           