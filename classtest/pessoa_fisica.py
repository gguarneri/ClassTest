"""Módulo de definição da classe ``PessoaFisica``."""
from classtest.pessoa import Pessoa


class PessoaFisica(Pessoa):
    """Classe para definição de pessoas físicas.

    A classe ``PessoaFisica`` é uma especialização da classe básica ``Pessoa``.
    As *pessoas físicas* são cidadões reais,
    identificados por um número único gerado pela Receita Federal e conhecido por **CPF** (*Cadastro de Pessoa
    Física*).
    """

    def __init__(self, cpf, nome, idade):
        """Construtor da classe.

        O construtor cria uma nova instância da classe, exigindo ``nome``, ``idade`` e ``CPF``.
        """

        # Chama o construtor da classe básica.
        super().__init__(nome, idade)

        # Atribuição dos atributos da instância.
        #: Identificador do Cadastro de Pessoa Física gerado pela Receita Federal. Esse atributo não é numérico, uma
        #: vez que a Receita Federal estabelece o padrão ``###.###.###-##``.
        self.cpf = cpf

    def get_cpf(self):
        """Método de leitura do atributo ``cpf``."""
        return self.cpf

    def set_cpf(self, cpf):
        """Método de escrita no atributo ``cpf``."""
        self.cpf = cpf