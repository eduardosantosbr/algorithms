'''
Autores: Eduardo Nunes Santos e Glaucia de Pádua da Silva

O algoritmo minimizarCozinheiros utiliza o método de programação conhecido como algoritmo guloso.
Esse algoritmo é aplicado sobre uma lista de tarefas. Inicialmente é efetuado a ordenação crescente pelo deadline das tarefas.
A seguir as tarefas são executas de modo a ser processadas em uma única thread (cozinheiro).
Para as tarefas remanescentes, foi utilizada uma chamada recursiva para criar uma nova thread, até que todas as tarefas sejam executadas.

Sobre o feedback referente a entrega da atividade A1:
    Referente ao uso da expansão da recorrência:
        A gente não conhecia, no entando tivemos acesso através do vídeo no youtube do
        Prof. Adenilso Simão https://www.youtube.com/watch?v=0iUDW9D3Lc8 
        [ICC II - Aula 12 - (2/4) - Quicksort - Complexidade do Pior Caso]
    Nesse vídeo é mostrado a análise do pior caso do algoritmo, que serviu de base para a nossa primeira atividade.
'''

def minimizarCozinheiros(tarefas, duracao, deadline):
    '''
    Implementação de algoritmo minimizarCozinheiros.
    
    Parameters
        tarefas (array): array de tarefas
        duracao (array): tempo de preparo de cada tarefa
        deadline (array): tempo limite para o preparo de cada tarefa
    '''    
    # Faz a ordenação crescente pelo deadline.                                          # Custo         Pior caso
    tarefas_ordenadas = sorted(tarefas, key=lambda x: deadline[x])                      # C1             * S(n)
    # Variável do tipo inteiro para controle de execução
    tempo = 0                                                                           # C2             * 1
    
    # Variável do tipo array para armazenar as tarefas remanescentes, ainda não distribuidas
    tarefas_remanescentes = []                                                          # C3             * 1
    # Variável do tipo inteiro para controle da quantidade de cozinheiros necessários
    cozinheiros = 1                                                                     # C4             * 1

    for tarefa in tarefas_ordenadas:                                                    # C5             * n + 1
        tempo += duracao[tarefa]                                                        # C6             * n
        # Verifica se o tempo de execução da tarefa ultrapassou o deadline
        if tempo > deadline[tarefa]:                                                    # C7             * n
            tempo -= duracao[tarefa]                                                    # C8             * n
            # Alimenta a lista de tarefas remanescentes, esse ponto é importante para garantir a recursividade
            tarefas_remanescentes.append(tarefa)                                        # C9             * n
 
    if tarefas_remanescentes:                                                           # C10            * 1
        # Faz a chamada recursiva, caso neceessário para tratar as demais tarefas. 
        cozinheiros += minimizarCozinheiros(tarefas_remanescentes, duracao, deadline)   # C11            * T(n-1)
 
    # Retorna a quantidade de cozinheiros necessários
    return cozinheiros                                                                  # C12            * 1


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

    # Faz a chamada principal do método minimizarCozinheiros
    cozinheiros = minimizarCozinheiros(tarefas, duracao, deadline)

    print("Será necessário ", cozinheiros, " cozinheiro(s)")

if __name__ == "__main__":
    main()
