class Categoria:
    def __init__(self, nome: str, descricao: str = "") -> None:
        self.nome = nome
        self.descricao = descricao

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str):
            raise TypeError("O nome da categoria deve ser uma string.")
        
        novo_nome = novo_nome.strip()

        if not novo_nome:
            raise ValueError("O nome da categoria não pode ser vazio.")
        self._nome = novo_nome

    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao: str):
        if not isinstance(nova_descricao, str):
            raise TypeError("A descrição da categoria deve ser uma string.")
        self._descricao = nova_descricao.strip()