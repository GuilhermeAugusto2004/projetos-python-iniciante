itens = []


def adicionar_itens(nome, preco, quantidade):
    item = {"nome": nome, "valor": preco, "Quantidade no estoque": quantidade}
    itens.append(item)


def remover_item(nome):
    for item in itens:
        if item["nome"] == nome:
            itens.remove(item)
            break


def visualizar_itens():
    for item in itens:
        print(
            f"Nome: {item['nome']}, Preço: {item['valor']}, Quantidade: {item['Quantidade no estoque']}"
        )


def calcular_custo(
    nome_item,
    qtd_usada,
):
    for item in itens:
        if item["nome"] == nome_item:
            custo_total = qtd_usada * item["valor"]
            return custo_total
    return "Item não encontrado"


valor_mao_de_obra = 0


def menu():
    global valor_mao_de_obra
    while True:
        adicionar = input(
            "Deseja adicionar um item? [S]/[N]/[V] para voltar/[M] para adicionar valor da mão de obra "
        )
        if adicionar.lower() == "s" or adicionar.lower() == "sim":
            nome = input("Digite o nome do item: ")
            preco = float(input("Digite o preço do item: "))
            quantidade = int(input("Digite a quantidade do item: "))
            adicionar_itens(nome, preco, quantidade)
        elif adicionar.lower() == "m":
            valor_mao_de_obra = float(input("Digite o valor da mão de obra: "))
        elif (
            adicionar.lower() == "n"
            or adicionar.lower() == "nao"
            or adicionar.lower() == "v"
        ):
            break


while True:
    bem_vindo = input(
        "Bem Vindo\n O que deseja fazer: soma [ss], adicionar [ad], visualizar lista [vl], sair [S] "
    )

    if bem_vindo.lower() == "ad":
        menu()
    elif bem_vindo.lower() == "vl":
        visualizar_itens()
    elif bem_vindo.lower() == "ss":
        custo_total = 0

        while True:
            nome_item = input("Digite o nome do produto ou [V] para voltar: ")
            if nome_item.lower() == "v":
                break
            qtd_usada = int(input("Quantidade de Material gasto: "))
            custo_parcial = calcular_custo(
                nome_item,
                qtd_usada,
            )
            if type(custo_parcial) == str:
                print(custo_parcial)
            else:
                custo_total += custo_parcial
        custo_total += valor_mao_de_obra
        print(f"Custo Total: {custo_total}")
    elif bem_vindo.lower() == "s":
        print("Saindo...")
        break
