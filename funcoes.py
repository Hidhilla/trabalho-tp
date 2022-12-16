from json_storage import lerJson, gravarJson


def criar(paciente: dict) -> dict:
    pacientes = lerJson()
    paciente['codigo'] = gerarId()
    pacientes.append(paciente)
    gravarJson(pacientes)


def editar(paciente: dict) -> None:
    pacientes = lerJson()
    for i, data in enumerate(pacientes):
        if data['codigo'] == paciente['codigo']:
            pacientes[i] = paciente
    gravarJson(pacientes)


def excluir(codigo: int) -> None:
    pacientes = lerJson()
    for paciente in pacientes:
        if paciente['codigo'] == codigo:
            pacientes.remove(paciente)
    gravarJson(pacientes)


def selecionar(codigo: int) -> dict | None:
    pacientes = lerJson()
    for paciente in pacientes:
        if paciente['codigo'] == codigo:
            return paciente
    return None


def selecionar_todos() -> list:
    return lerJson()


def gerarId() -> int:
    pacientes = lerJson()
    if len(pacientes) == 0:
        return 1
    return pacientes[-1]['codigo'] + 1
