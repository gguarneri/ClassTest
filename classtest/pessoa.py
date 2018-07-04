"""Módulo de definição da classe básica ``Pessoa``."""


class Pessoa(object):
    """Classe básica para definição de pessoas.

    Essa classe serve como classe básica para a definição de pessoas físicas e jurídicas.
    """

    def __init__(self, nome, idade, endereco='Beco sem Nome'):
        """Construtor da classe.

        O construtor cria uma nova instância da classe, exigindo um nome e uma idade.
        """

        # Atribuição dos atributos da instaância.
        #: Nome oficial da pessoa.
        self.nome = nome

        #: Idade da pessoa, em anos.
        self.idade = idade

        #: Endereço da pessoa
        self.endereco = endereco

    def set_nome(self, nome):
        """Método de escrita no atributo ``nome``."""
        self.nome = nome

    def set_idade(self, idade):
        """Método de escrita no atributo ``idade``."""
        self.idade = idade

    def set_endereco(self, endereco):
        """Método de escrita no atributo ``endereco``."""
        self.endereco = endereco

    def get_nome(self):
        """Método de leitura do atributo ``nome``."""
        return self.nome

    def get_idade(self):
        """Método de leitura do atributo ``idade``."""
        return self.idade

    def get_endereco(self):
        """Método de leitura do atributo ``endereco``."""
        return self.endereco
