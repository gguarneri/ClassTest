if __name__ == "__main__":
    # execute only if run as a script
    from classtest.pessoa_fisica import PessoaFisica
    from classtest.pessoa_juridica import PessoaJuridica

    a = PessoaFisica('111.222.333-44', nome='Alfredo', idade=22)

    print(a.get_cpf())
    print(a.get_nome())
    print(a.get_idade())

    b = PessoaJuridica('64.614.527/0001-99', nome='Empresa X', idade=10)

    print(b.get_cnpj())
    print(b.get_nome())
    print(b.get_idade())