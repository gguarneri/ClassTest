"""Módulo de definição da classe básica ``PessoaJuridica``."""
from classtest.pessoa import Pessoa


class PessoaJuridica(Pessoa):
    """Classe para definição de pessoas jurídicas.

    A classe ``PessoaJuridica`` é uma especialização da classe básica ``Pessoa``. As *pessoas jurídicas* são
    associadas a entidades tais como empresas, associações, fundações.
    As *pessoas jurídicas* são identificados por um número único
    gerado pela Receita Federal e conhecido por **CNPJ** (*Cadastro Nacional de Pessoa Jurídica*).
    """

    def __init__(self, cnpj, nome, idade):
        """Construtor da classe.

        O construtor cria uma nova instância da classe, exigindo ``nome``, ``idade`` e ``CNPJ``.
        """

        # Chama o construtor da classe básica.
        super().__init__(nome, idade)

        # Atribuição dos atributos da instância.
        #: Identificador do *Cadastro Nacional de Pessoa Jurídica* gerado pela Receita Federal.
        #: Esse atributo não é numérico, uma vez que a Receita Federal estabelece o padrão ``##.###.###/####-##``.
        self.cnpj = cnpj

    def get_cnpj(self):
        """Método de leitura do atributo ``cnpj``."""
        return self.cnpj

    def set_cnpj(self, cnpj):
        """Método de escrita no atributo ``cnpj``."""
        self.cnpj = cnpj