"""Módulo de definição da classe básica ``Pessoa``."""


class Pessoa(object):
    """Classe básica para definição de pessoas.

    Essa classe serve como classe básica para a definição de pessoas físicas e jurídicas.
    """

<<<<<<< HEAD
    def __init__(self, nome, idade, endereco='Beco sem Nome'):
=======
    def __init__(self, nome, idade, apelido = "Zé"):
>>>>>>> c29eb4156eff0ec16d84f4e5d82db228c5c4f6f5
        """Construtor da classe.

        O construtor cria uma nova instância da classe, exigindo um nome e uma idade.
        """

        # Atribuição dos atributos da instaância.
        #: Nome oficial da pessoa.
        self.nome = nome

        #: Idade da pessoa, em anos.
        self.idade = idade

<<<<<<< HEAD
        #: Endereço da pessoa
        self.endereco = endereco
=======
        #: Apelido da pessoa.
        self.apelido = apelido
>>>>>>> c29eb4156eff0ec16d84f4e5d82db228c5c4f6f5

    def set_nome(self, nome):
        """Método de escrita no atributo ``nome``."""
        self.nome = nome

    def set_idade(self, idade):
        """Método de escrita no atributo ``idade``."""
        self.idade = idade

<<<<<<< HEAD
    def set_endereco(self, endereco):
        """Método de escrita no atributo ``endereco``."""
        self.endereco = endereco
=======
    def set_apelido(self, apelido):
        """Método de escrita no atributo ``apelido``."""
        self.apelido = apelido
>>>>>>> c29eb4156eff0ec16d84f4e5d82db228c5c4f6f5

    def get_nome(self):
        """Método de leitura do atributo ``nome``."""
        return self.nome

    def get_idade(self):
        """Método de leitura do atributo ``idade``."""
        return self.idade

<<<<<<< HEAD
    def get_endereco(self):
        """Método de leitura do atributo ``endereco``."""
        return self.endereco
=======
    def get_apelido(self):
        """Método de leitura do atributo ``apelido``."""
        return self.apelido
>>>>>>> c29eb4156eff0ec16d84f4e5d82db228c5c4f6f5
