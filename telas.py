import os

class Pacientes:
    def cadastrarPaciente():
        Pacientes.limparTela()
        print("-------- Cadastro de paciente --------")
        paciente = {}
        paciente['codigo'] = str(input("Código do Paciente: "))
        paciente['nome'] = str(input("Nome do Paciente: "))
        paciente['endereco'] = str(input("Endereço do Paciente:  "))
        paciente['cpf'] = str(input("CPF do Paciente: "))
        paciente['telefone'] = str(input("Telefone do Paciente: "))
        paciente['data de nascimento'] = str(input("Data de Nascimento do Paciente:"))

        return paciente


    def editarPaciente():
        Pacientes.limparTela()
        print("-------- Edição de paciente --------")
        paciente = {}
        paciente['codigo'] = int(input('Código: '))
        paciente['nome'] = input('Nome: ')
        paciente['endereco'] = input('Endereço: ')
        paciente['cpf'] = input('cpf: ')
        paciente['telefone'] = input('telefone: ')
        paciente['data de nascimento'] = input( 'Data de Nascimento do Paciente: ' )

        return paciente


    def excluirPaciente():
        print("-------- Exclusão de Paciente --------")
        Pacientes.limparTela()
        codigo = int(input('Código: '))
        return codigo


    def selecionarPaciente():
        Pacientes.limparTela()
        print("-------- Seleção de Paciente --------")
        codigo = int(input('Código: '))
        return codigo


    def exibirPaciente(paciente):
        print("-------- paciente --------")
        print(f"Codigo: {paciente['codigo']}")
        print(f"Nome: {paciente['nome']}")
        print(f"Endereço: {paciente['endereco']}")
        print(f"Cpf: {paciente['cpf']}")
        print(f"Telefone: {paciente['telefone']}")
        print(f"Data de Nascimento: {paciente['data de nascimento']}")


    def exibirPacientes(pacientes):
        Pacientes.limparTela()
        print("---------------- Pacientes ----------------")
        for paciente in pacientes:
            Pacientes.exibirpaciente(paciente)
        Pacientes.travarTela()


    def limparTela():
        os.system('clear' if os.name == 'posix' else 'cls')


    def travarTela():
        input('Pressione ENTER para continuar...')


    def exibirMsg(msg):
        print(msg)
        Pacientes.travarTela()
