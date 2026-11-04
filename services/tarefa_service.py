from models.tarefa import Tarefa
from repositories.tarefa_repository import TarefaRepository
from models.prioridade import Prioridade
from models.categoria import Categoria

class TarefaService:
    def __init__(self, repositorio: TarefaRepository):
        self.repositorio = repositorio


    def adicionar(self, tarefa: Tarefa) -> None:
        # carrega todas as tarefas existentes do repositório
        tarefas = self.repositorio.carregar()
        for tarefa_existente in tarefas:
            if tarefa_existente.id == tarefa.id:
                raise ValueError(f"Já existe uma tarefa com o ID {tarefa.id}.")
            
        tarefas.append(tarefa)
        self.repositorio.guardar(tarefas)

    def listar_todas(self) -> list[Tarefa]:
        return self.repositorio.carregar()

    def obter_por_id(self, tarefa_id: int) -> Tarefa | None:
        self._validar_id(tarefa_id)
        # 3. Procurar a tarefa.
        tarefas = self.repositorio.carregar()
        for tarefa in tarefas:
            if tarefa.id == tarefa_id:
                return tarefa
        # 4. Devolver a tarefa ou None.
        return None

    # **dados seria um dicionário contendo os campos a serem atualizados e seus respectivos valores.
    def atualizar(self, tarefa_id: int, **dados) -> Tarefa:
        if not dados:
            raise ValueError("Deves fornecer pelo menos um campo para atualizar.") 

        self._validar_id(tarefa_id)

        campos_permitidos = (
            "titulo",
            "descricao",
            "prioridade",
            "categoria",
            "data_limite"
        )

        # para cada chave em dados, verificar se é permitida
        for campo in dados:
            if campo not in campos_permitidos:
                raise ValueError(f"Campo não permitido: {campo}")


        tarefas = self.repositorio.carregar()

        for tarefa in tarefas:
            if tarefa.id == tarefa_id:
                for campo, valor in dados.items():
                    # tarefa: o objeto que queremos modificar.
                    # "campo": o atributo que queremos atualizar.
                    # "valor": o novo valor.
                    # setattr(objeto, atributo, novo_valor)
                    setattr(tarefa, campo, valor)

                self.repositorio.guardar(tarefas)
                return tarefa

        raise ValueError(f"Tarefa com ID {tarefa_id} não encontrada.")

    def eliminar(self, tarefa_id: int) -> None:
        self._validar_id(tarefa_id)

        tarefas = self.repositorio.carregar()

        for tarefa in tarefas:
            if tarefa.id == tarefa_id:
                tarefas.remove(tarefa)
                self.repositorio.guardar(tarefas)
                return

        raise ValueError(f"Tarefa com ID {tarefa_id} não encontrada.")

    def _validar_id(self, tarefa_id: int) -> None:
        if not isinstance(tarefa_id, int) or isinstance(tarefa_id, bool):
            raise TypeError("O ID deve ser um número inteiro.")

        if tarefa_id <= 0:
            raise ValueError("O ID deve ser um número positivo.")

    def concluir(self, tarefa_id: int) -> Tarefa:
        self._validar_id(tarefa_id)

        tarefas = self.repositorio.carregar()

        for tarefa in tarefas:
            if tarefa.id == tarefa_id:
                tarefa.concluir()
                self.repositorio.guardar(tarefas)
                return tarefa

        raise ValueError(f"Tarefa com ID {tarefa_id} não encontrada.")

    def reabrir(self, tarefa_id: int) -> Tarefa:
        self._validar_id(tarefa_id)

        tarefas = self.repositorio.carregar()

        for tarefa in tarefas:
            if tarefa.id == tarefa_id:
                tarefa.reabrir()
                self.repositorio.guardar(tarefas)
                return tarefa

        raise ValueError(f"Tarefa com ID {tarefa_id} não encontrada.")

    def pesquisar(self, titulo: str) -> list[Tarefa]:
        if not isinstance(titulo, str):
            raise TypeError("O título deve ser uma string.")

        titulo = titulo.strip().lower()
        if not titulo:
            raise ValueError("O título não pode estar vazio.")
        
        tarefas = self.repositorio.carregar()
        resultado = []
        for tarefa in tarefas:
            if titulo in tarefa.titulo.lower():
                resultado.append(tarefa)
        return resultado

    def filtrar(
        self,
        prioridade: Prioridade | None = None,
        categoria: Categoria | None = None,
        concluida: bool | None = None,
        atrasada: bool | None = None) -> list[Tarefa]:

        # 1. Validar prioridade
        if prioridade is not None and not isinstance(prioridade, Prioridade):
            raise TypeError("A prioridade deve ser um membro de Prioridade.")

        # 2. Validar categoria
        if categoria is not None and not isinstance(categoria, Categoria):
            raise TypeError("A categoria deve ser um membro de Categoria.")

        # 3. Validar estado de conclusão
        if concluida is not None and not isinstance(concluida, bool):
            raise TypeError("O parâmetro concluida deve ser True, False ou None.")

        # 4. Validar estado de atraso
        if atrasada is not None and not isinstance(atrasada, bool):
            raise TypeError("O parâmetro atrasada deve ser True, False ou None.")

        # 5. Carregar tarefas do repositório
        tarefas = self.repositorio.carregar()

        # 6. Aplicar filtros
        resultado = []

        for tarefa in tarefas:

            if prioridade is not None and tarefa.prioridade != prioridade:
                continue

            if categoria is not None and tarefa.categoria != categoria:
                continue

            if concluida is not None and tarefa.concluida != concluida:
                continue

            if atrasada is not None and tarefa.esta_atrasada() != atrasada:
                continue

            resultado.append(tarefa)

        return resultado