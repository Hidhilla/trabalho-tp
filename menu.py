from telas import *
from funcoes import *

def menu():
    Pacientes.limparTela()
    print("-------- Sistema de paciente --------")
    print("1 - Cadastrar Pacientes")
    print("2 - Editar Paciente")
    print("3 - Excluir Paciente")
    print("4 - Selecionar Paciente")
    print("5 - Listar Pacientes")
    print("6 - Sair")
    print("-------------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


while True:
    opcao = menu()

    if opcao == 1:
        paciente = Pacientes.cadastrarPaciente()
        criar(paciente)
        Pacientes.exibirMsg("Paciente cadastrado com sucesso!")
    elif opcao == 2:
        paciente = Pacientes.editarPaciente()
        editar(paciente)
        Pacientes.exibirMsg("Paciente editado com sucesso!")
    elif opcao == 3:
        Pacientes.limparTela()
        codigo = Pacientes.excluirPaciente()
        excluir(codigo)
        Pacientes.exibirMsg("Paciente excluído com sucesso!")
    elif opcao == 4:
        codigo = Pacientes.selecionarPaciente()
        paciente = selecionar(codigo)
        if paciente == None:
            Pacientes.exibirMsg("Paciente não encontrado!")
        else:
            Pacientes.exibirPaciente(paciente)
            Pacientes.travarTela()
    elif opcao == 5:
        paciente = selecionar_todos()
        Pacientes.exibirPacientes(paciente)
    elif opcao == 6:
        break
