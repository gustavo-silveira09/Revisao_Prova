#Aqui vou desenvolver meu código de
#Teste para a Revisão da Prova

# Lista (array) que armazenará os motores em memória durante a execução
motores = []


def cadastrar_motor():
    print("\n--- Cadastrar Novo Motor ---")
    codigo = input("Código/ID do motor: ").strip()

    # Verifica se já existe um motor com o mesmo código
    for m in motores:
        if m["codigo"].lower() == codigo.lower():
            print("Erro: Já existe um motor cadastrado com este código.")
            return

    modelo = input("Modelo/Fabricante: ").strip()
    potencia = input("Potência (ex: 5 CV, 10 kW): ").strip()
    rotacao = input("Rotação (RPM): ").strip()
    tensao = input("Tensão (ex: 220V/380V): ").strip()

    motor = {
        "codigo": codigo,
        "modelo": modelo,
        "potencia": potencia,
        "rotacao": rotacao,
        "tensao": tensao,
    }

    motores.append(motor)
    print(f"Sucesso: Motor '{modelo}' (Cód: {codigo}) cadastrado!")


def listar_motores():
    print("\n--- Lista de Motores Cadastrados ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for i, m in enumerate(motores, start=1):
        print(
            f"{i}. Cód: {m['codigo']} | Modelo: {m['modelo']} | "
            f"Potência: {m['potencia']} | RPM: {m['rotacao']} | Tensão: {m['tensao']}"
        )


def buscar_motor():
    print("\n--- Buscar Motor ---")
    termo = input("Digite o código ou modelo do motor: ").strip().lower()
    encontrados = [
        m
        for m in motores
        if termo in m["codigo"].lower() or termo in m["modelo"].lower()
    ]

    if not encontrados:
        print("Nenhum motor encontrado com esse termo.")
        return

    for m in encontrados:
        print(
            f"-> Cód: {m['codigo']} | Modelo: {m['modelo']} | "
            f"Potência: {m['potencia']} | RPM: {m['rotacao']} | Tensão: {m['tensao']}"
        )


def editar_motor():
    print("\n--- Editar Motor ---")
    codigo = input("Informe o código do motor que deseja editar: ").strip()

    for m in motores:
        if m["codigo"].lower() == codigo.lower():
            print("Pressione ENTER para manter o valor atual.")
            novo_modelo = input(f"Modelo [{m['modelo']}]: ").strip()
            nova_potencia = input(f"Potência [{m['potencia']}]: ").strip()
            nova_rotacao = input(f"Rotação [{m['rotacao']}]: ").strip()
            nova_tensao = input(f"Tensão [{m['tensao']}]: ").strip()

            if novo_modelo:
                m["modelo"] = novo_modelo
            if nova_potencia:
                m["potencia"] = nova_potencia
            if nova_rotacao:
                m["rotacao"] = nova_rotacao
            if nova_tensao:
                m["tensao"] = nova_tensao

            print("Motor atualizado com sucesso!")
            return

    print("Motor não encontrado.")


def remover_motor():
    print("\n--- Remover Motor ---")
    codigo = input("Informe o código do motor que deseja remover: ").strip()

    for i, m in enumerate(motores):
        if m["codigo"].lower() == codigo.lower():
            removido = motores.pop(i)
            print(
                f"Motor '{removido['modelo']}' (Cód: {removido['codigo']}) removido."
            )
            return

    print("Motor não encontrado.")


def menu():
    while True:
        print("\n==============================")
        print("  SISTEMA DE CADASTRO DE MOTORES")
        print("==============================")
        print("1 - Cadastrar motor")
        print("2 - Listar motores")
        print("3 - Buscar motor")
        print("4 - Editar motor")
        print("5 - Remover motor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            editar_motor()
        elif opcao == "5":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()