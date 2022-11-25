def minimizarCozinheiros(tarefas, duracao, deadline):
    # Faz a ordenação crescente pelo deadline.
    tarefas_ordenadas = sorted(tarefas, key=lambda x: deadline[x])
    tempo = 0
    solucao = []
    cozinheiros = 1

    for tarefa in tarefas_ordenadas:
        tempo += duracao[tarefa]
        if tempo > deadline[tarefa]:
            tempo -= duracao[tarefa]
            solucao.append(tarefa)

    if solucao:
        cozinheiros += minimizarCozinheiros(solucao, duracao, deadline) # Faz a chamada recursiva, caso neceessário para tratar as demais tarefas.

    return cozinheiros


def main():
    tarefas = [
        "Espaguete",
        "Carne",
        "Calabresa",
        "Alho",
        "Queijo",
        "Feijão",
        "Folhas",
        "Arroz"
    ]

    duracao = {
        "Espaguete": 15,
        "Carne": 90,
        "Calabresa": 15,
        "Alho": 25,
        "Queijo": 80,
        "Feijão": 150,
        "Folhas": 25,
        "Arroz": 120
    }

    deadline = {
        "Espaguete": 100,
        "Carne": 140,
        "Calabresa": 200,
        "Alho": 210,
        "Queijo": 130,
        "Feijão": 180,
        "Folhas": 240,
        "Arroz": 230
    }

    cozinheiros = minimizarCozinheiros(tarefas, duracao, deadline)

    print("Será necessário ", cozinheiros, " cozinheiro(s)")

if __name__ == "__main__":
    main()
