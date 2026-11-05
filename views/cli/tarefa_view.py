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

            prioridades = { "1": Prioridade.BAIXA, "2": Prioridade.MEDIA, "3": Prioridade.ALTA, "4": Prioridade.URGENTE}

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

    def atualizar_tarefa(self) -> None:
        try:
            tarefa_id = int(input("Digite o ID da tarefa: "))

            tarefa = self.controller.obter_tarefa(tarefa_id)

            if tarefa is None:
                print("Tarefa não encontrada.")
                return

            dados = {}

            print("\n========== ATUALIZAR TAREFA ==========")
            print(f"Título atual: {tarefa.titulo}")
            print(f"Descrição atual: {tarefa.descricao}")
            print(f"Prioridade atual: {tarefa.prioridade.value}")
            print(f"Categoria atual: {tarefa.categoria.nome}")

            if tarefa.data_limite:
                print(f"Data limite atual: {tarefa.data_limite:%d/%m/%Y}")
            else:
                print("Data limite atual: Sem prazo")

            # Atualizar título
            titulo = input("\nNovo título (Enter para manter): ")

            if titulo.strip():
                dados["titulo"] = titulo

            # Atualizar descrição
            descricao = input("Nova descrição (Enter para manter): ")

            if descricao.strip():
                dados["descricao"] = descricao

            # Atualizar prioridade
            prioridade = input("Nova prioridade (Enter para manter): ")

            if prioridade.strip():
                for p in Prioridade:
                    # p é um membro da enumeração Prioridade ex: Prioridade.ALTA 
                    # casefold() é usado para comparação sem diferenciar maiúsculas de minúsculas
                    if prioridade.strip().casefold() in (p.name.casefold(), p.value.casefold()):
                        dados["prioridade"] = p
                        break
                else:
                    raise ValueError("Prioridade inválida.")

            # Atualizar categoria
            categoria = input("Nova categoria (Enter para manter): ")

            if categoria.strip():
                dados["categoria"] = Categoria(categoria)

            # Atualizar data limite
            data_limite = input("Nova data limite (dd/mm/aaaa): ")

            if data_limite.strip():
                dados["data_limite"] = datetime.strptime(data_limite,"%d/%m/%Y")

            # Verificar se existem alterações
            if not dados:
                print("Nenhuma alteração foi realizada.")
                return

            self.controller.atualizar_tarefa(tarefa_id, **dados)

            print("\nTarefa atualizada com sucesso!")

        except (ValueError, TypeError) as erro:
            print(f"\nErro ao atualizar tarefa: {erro}")

    def eliminar_tarefa(self) -> None:
        try:
            tarefa_id = int(input("ID da tarefa a eliminar: "))
            tarefa = self.controller.obter_tarefa(tarefa_id)
            if tarefa is None:
                print("Tarefa não encontrada.")
                return

            confirmacao = input(f"Tem certeza que deseja eliminar {tarefa.titulo} desta tarefa? (s/n): ").strip().lower()

            if confirmacao != "s":
                print("Operação cancelada.")
                return

            self.controller.eliminar_tarefa(tarefa_id)
            print("\nTarefa eliminada com sucesso!")

        except (ValueError, TypeError) as erro:
            print(f"\nErro ao eliminar tarefa: {erro}")

    def concluir_tarefa(self) -> None:
        try:
            tarefa_id = int(input("ID da tarefa a concluir: "))
            tarefa = self.controller.obter_tarefa(tarefa_id)

            if tarefa is None:
                print("Tarefa não encontrada.")
                return
            if tarefa.concluida:
                print("Esta tarefa já está concluída.")
                return
            
            confirmacao = input(f"Tem certeza que deseja concluir {tarefa.titulo}? (s/n): ").strip().lower()

            if confirmacao != "s":
                print("Operação cancelada.")
                return

            self.controller.concluir_tarefa(tarefa_id)
            print("\nTarefa concluída com sucesso!")

        except (ValueError, TypeError) as erro:
            print(f"\nErro ao concluir tarefa: {erro}")

    def reabrir_tarefa(self) -> None:
        try:
            tarefa_id = int(input("ID da tarefa a reabrir: "))
            tarefa = self.controller.obter_tarefa(tarefa_id)

            if tarefa is None:
                print("Tarefa não encontrada.")
                return
            if not tarefa.concluida:
                print("Esta tarefa já está aberta.")
                return

            confirmacao = input(f"Tem certeza que deseja reabrir '{tarefa.titulo}'? (s/n): ").strip().lower()

            if confirmacao != "s":
                print("Operação cancelada.")
                return

            self.controller.reabrir_tarefa(tarefa_id)
            print("\nTarefa reaberta com sucesso!")

        except (ValueError, TypeError) as erro:
            print(f"\nErro ao reabrir tarefa: {erro}")

    def pesquisar_tarefas(self) -> None:
        try:
            termo = input("Digite o termo de pesquisa: ").strip().lower()
            resultados = self.controller.pesquisar_tarefas(termo)

            if not resultados:
                print("Nenhuma tarefa encontrada.")
                return

            print("\nTarefas encontradas:")
            for tarefa in resultados:
                status = "Concluída" if tarefa.concluida else "Pendente"

                print(f"\nID: {tarefa.id}")
                print(f"Título: {tarefa.titulo}")
                print(f"Prioridade: {tarefa.prioridade.value}")
                print(f"Categoria: {tarefa.categoria.nome}")
                print(f"Estado: {status}")
                print("-" * 40)

        except (ValueError, TypeError) as erro:
            print(f"\nErro ao pesquisar tarefas: {erro}")

    def filtrar_tarefas(self) -> None:
        try:
            print("\n========== FILTRAR TAREFAS ==========")
            print("1. Tarefas pendentes")
            print("2. Tarefas concluídas")
            print("3. Tarefas atrasadas")
            print("4. Tarefas dentro do prazo")
            print("5. Filtrar por prioridade")
            print("6. Filtrar por categoria")

            criterio = input("\nEscolha o tipo de filtro: ").strip()

            filtros = {}

            if criterio == "1":
                filtros["concluida"] = False

            elif criterio == "2":
                filtros["concluida"] = True

            elif criterio == "3":
                filtros["atrasada"] = True

            elif criterio == "4":
                filtros["atrasada"] = False

            elif criterio == "5":
                print("\nPrioridades disponíveis:")
                for prioridade in Prioridade:
                    print(f"- {prioridade.value}")

                escolha = input("Digite a prioridade: ").strip().casefold()

                for prioridade in Prioridade:
                    if escolha in (prioridade.name.casefold(),prioridade.value.casefold()):
                        filtros["prioridade"] = prioridade
                        break
                else:
                    print("Prioridade inválida.")
                    return

            elif criterio == "6":
                nome_categoria = input("Digite o nome da categoria: ").strip()

                if not nome_categoria:
                    print("Categoria inválida.")
                    return

                filtros["categoria"] = Categoria(nome_categoria)

            else:
                print("Opção de filtro inválida.")
                return

            resultados = self.controller.filtrar_tarefas(**filtros)

            if not resultados:
                print("\nNenhuma tarefa encontrada.")
                return

            print("\n========== TAREFAS FILTRADAS ==========")

            for tarefa in resultados:
                status = "Concluída" if tarefa.concluida else "Pendente"

                print(f"\nID: {tarefa.id}")
                print(f"Título: {tarefa.titulo}")
                print(f"Descrição: {tarefa.descricao}")
                print(f"Prioridade: {tarefa.prioridade.value}")
                print(f"Categoria: {tarefa.categoria.nome}")
                print(f"Estado: {status}")

                if tarefa.data_limite:
                    print(f"Data limite: {tarefa.data_limite:%d/%m/%Y}")
                else:
                    print("Data limite: Sem prazo")

                print("-" * 40)

            print(f"\nTotal de tarefas encontradas: {len(resultados)}")

        except (ValueError, TypeError) as erro:
            print(f"\nErro ao filtrar tarefas: {erro}")


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
                self.atualizar_tarefa()
            elif opcao == "5":
                self.eliminar_tarefa()
            elif opcao == "6":
                self.concluir_tarefa()
            elif opcao == "7":
                self.reabrir_tarefa()
            elif opcao == "8":
                self.pesquisar_tarefas()
            elif opcao == "9":
                self.filtrar_tarefas()
            elif opcao == "0":
                print("Obrigado por utilizar o TaskManager. Até breve!")
                break
            else:
                print("Opção inválida. Tente novamente.")
           