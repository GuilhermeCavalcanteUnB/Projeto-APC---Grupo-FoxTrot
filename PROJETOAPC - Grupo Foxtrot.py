listaAlimentos = [] #Cria-se uma lista para armazenar os alimentos adicionados no programa


def menu(): #Função responsável pela exibição das opções disponíveis pelo código para interação do usuário
    print('=--------------------------------------------------=')
    print('DESPERDÍCIO DE ALIMENTOS\n')
    print('Selecione a opção que deseja:\n')
    print('1. Adicionar alimentos\n')
    print('2. Remover alimentos\n')
    print('3. Listar Alimentos\n')
    print('4. Gerar Relatório\n')
    print('5. Fechar Programa\n')
    print('=--------------------------------------------------=')


def adicionarAlimentos(): #Função para se adicionar um alimento junto com sua unidade de medida, seu preço por unidade, o produzido e o desperdiçado
    print()
    print('Adicionando Alimento'.center(50, '=')) #Exibição do título

    nomeAlimento = input('\nQual o nome do alimento?\n').lower() #Solicita o nome do alimento e o altera para letras minúsculas
    unidadeMedida = input('\nQual a unidade de medida? (kg; g; L)\n').lower() #Solicita a unidade de medida do alimento e o altera para letras minúsculas
    precoUnidade = float(input('\nQual o preço por unidade, em reais?\n').replace(',', '.')) #Solicita o preço por unidade e o converte a float
    qtdProduz = float(input(f'\nQuanto foi produzido, em {unidadeMedida}?\n')) #Solicita o que foi produzido e o converte em float
    qtdDesper = float(input(f'\nQuanto foi o desperdício, em {unidadeMedida}?\n')) #Solicita o que foi despediçado e o converte em float

    lista = [nomeAlimento, unidadeMedida, precoUnidade, qtdProduz, qtdDesper] #Cria uma lista com as informações do alimento
    listaAlimentos.append(lista) #Adiciona o alimento à lista de alimentos

    print('\n#===================================================#\n')
    print('\nVocê deseja adicionar mais um alimento? (sim/não)\n'.center(50, ' ')) #Pergunta se o usuário quer adicionar mais um alimento
 
    resposta = input().lower() #Lê a resposta do usuário, caso seja 'sim' retorna a função
    if resposta == 'sim':
        adicionarAlimentos()


def removerAlimentos(): #Função para remoção de um dos alimentos da lista de alimentos
    if not listaAlimentos: #Verifica se a lista de alimentos está vazia
        print("\nNão há alimentos registrados para remover!")
        return

    print('\nRemovendo Alimento'.center(50, '=')) #Exibe o título

    print('\nLista de Alimentos'.center(50, '=')) #Exibe a lista de alimentos enumerada
    for i, alimento in enumerate(listaAlimentos):
        print(f"{i+1}. {alimento[0]}")

    print('\nQual alimento você quer remover? (Digite o número)\n') #Solicita qual alimento o usuário quer remover baseado no número na lista
    try:
        alimento_idx = int(input()) - 1 #Lê qual alimento o usuário deseja remover
        if 0 <= alimento_idx < len(listaAlimentos):
            print(
                f'\nVocê deseja remover "{listaAlimentos[alimento_idx][0]}"? (sim/não)') #Confirma se o alimento a ser removido está correto
            resposta = input().lower()
            if resposta == 'sim':
                del listaAlimentos[alimento_idx]
            print('Lista de Alimentos Atualizada'.center(50, '=')) #Exibe a lista atualizada sem o item escolhido para remoção
            for alimento in listaAlimentos:
                print(alimento[0])
        else:
            print("\nÍndice inválido.")
    except ValueError:
        print("\nEntrada inválida. Digite um número.")

    print('\n#===================================================#\n') #Verifica se o usuário deseja remover mais uma alimento, se 'sim' retorna a função
    print('\nVocê deseja remover mais um alimento? (sim/não)\n'.center(50, ' '))
    resposta = input().lower()
    if resposta == 'sim':
        removerAlimentos()


def listarAlimentos(): #Função para a listagem dos alimentos já incluídos na lista de alimentos
    if listaAlimentos:
        print("Lista de Alimentos".center(50, '=')) 
        for alimento in listaAlimentos:
            print(alimento[0])
    else:
        print("\nNão há alimentos registrados.")


# Lista de mensagens motivacionais
mensagens_motivacionais = [
    "Cada alimento que você salva é um passo para um planeta mais sustentável. Pense no futuro, evite o desperdício!",
    "Desperdiçar menos hoje é garantir recursos para as gerações de amanhã. Faça a sua parte!",
    "O planeta não é descartável. Reduza o desperdício e preserve a vida na Terra.",
    "Desperdício zero é o caminho para um mundo mais consciente e responsável. Comece agora!",
    "Cada grão de alimento desperdiçado é um recurso natural que não voltará. Valorize o que você tem!",
    "A natureza nos dá tudo o que precisamos. Cabe a nós usarmos com sabedoria e sem desperdício.",
    "Pequenas ações, como evitar o desperdício, geram grandes impactos no meio ambiente. Seja a mudança!",
    "Desperdiçar alimentos é desperdiçar água, energia e vida. Pense nisso antes de descartar.",
    "O futuro do planeta está em nossas mãos. Reduza o desperdício e construa um amanhã melhor.",
    "Cada refeição planejada é um ato de amor ao meio ambiente. Diga não ao desperdício!",
    "Desperdício é falta de consciência. Sustentabilidade é responsabilidade. Escolha o seu lado!",
    "A Terra é a nossa casa. Vamos cuidar dela evitando o desperdício e promovendo a sustentabilidade.",
    "Desperdiçar menos é uma forma de agradecer ao planeta por tudo o que ele nos oferece.",
    "O desperdício de hoje é a escassez de amanhã. Faça escolhas conscientes e preserve o futuro.",
    "Cada ação conta! Reduzir o desperdício é um compromisso com o planeta e com as próximas gerações."
]

# Função para selecionar uma mensagem aleatória
def mensagem_aleatoria():
    from time import time  # Usamos o tempo atual para gerar um índice "aleatório"
    indice = int(time() * 1000) % len(mensagens_motivacionais)  # Gera um índice baseado no tempo
    return mensagens_motivacionais[indice]

def gerarRelatorio(): #Função para a gerar um relátorio, trazendo as informações registradas e a relação sobre o desperdício
    if not listaAlimentos:
        print("\nNão há alimentos registrados para gerar o relatório!")
        return
    # Função para calcular o tamanho máximo de cada coluna
    def calcularTamanhoColunas():
        tamanhoItem = max(len("Item"), max(len(alimento[0]) for alimento in listaAlimentos))
        tamanhoQuantidade = max(len("Quantidade Desperdiçada"), len("XX.XX"))
        tamanhoValor = max(len("Valor Perdido"), len("R$ XXX.XX"))
        tamanhoPorcentagem = max(len("% Desperdício"), len("XX.XX%"))
        return tamanhoItem, tamanhoQuantidade, tamanhoValor, tamanhoPorcentagem

    tamanhoItem, tamanhoQuantidade, tamanhoValor, tamanhoPorcentagem = calcularTamanhoColunas()

    # Tamanho total da tabela
    tamanhoTotalTabela = tamanhoItem + tamanhoQuantidade + tamanhoValor + tamanhoPorcentagem + 13

    # Título dinâmico
    titulo = "RELATÓRIO DE DESPERDÍCIO"
    print(f"{titulo} {'=' * (tamanhoTotalTabela - len(titulo) - 1)}")
    print()

    # Função para criar a linha de separação
    def criarLinhaSeparadora():
        linha = f"|{'-' * (tamanhoItem + 2)}|{'-' * (tamanhoQuantidade + 2)}|{'-' * (tamanhoValor + 2)}|{'-' * (tamanhoPorcentagem + 2)}|"
        return linha

    # Cabeçalho da tabela
    print(f"| {'Item':<{tamanhoItem}} | {'Quantidade Desperdiçada':<{tamanhoQuantidade}} | {'Valor Perdido':<{tamanhoValor}} | {'% Desperdício':<{tamanhoPorcentagem}} |")
    print(criarLinhaSeparadora())

    totalValorPerdido = 0
    totalDesperdicioPorcentagem = 0
    totalDesper = 0 
    totalProduz = 0

    for alimento in listaAlimentos:
        nome, unidade, preco, qtdProduz, qtdDesper = alimento
        desperdicioMonetario, desperdicioPorcentagem = calcularDesperdicio(qtdProduz, qtdDesper, preco)
        totalValorPerdido += desperdicioMonetario
        totalProduz += qtdProduz
        totalDesper += qtdDesper
        totalDesperdicioPorcentagem = (totalDesper / totalProduz) * 100

        # Ajuste para alinhar os valores corretamente
        print(f"| {nome:<{tamanhoItem}} | {qtdDesper:>{tamanhoQuantidade}.1f} | R$ {desperdicioMonetario:>{tamanhoValor - 3}.2f} | {desperdicioPorcentagem:>{tamanhoPorcentagem - 1}.2f}% |")

    # Linha de separação antes do total
    print("-" * tamanhoTotalTabela)

    # Total Geral
    espacosAntesTotal = tamanhoItem + tamanhoQuantidade + 5  # Ajuste para alinhar o total
    print(f"Total Geral: {' ' * (espacosAntesTotal - len('Total Geral:'))}| R$ {totalValorPerdido:>{tamanhoValor - 3}.2f} | {totalDesperdicioPorcentagem:>{tamanhoPorcentagem - 1}.2f}% do total")
    print("=" * tamanhoTotalTabela)
    
    # Mensagem motivacional aleatória
    print("\nMensagem:")
    print(mensagem_aleatoria())


def calcularDesperdicio(qtdProduz, qtdDesper, precoUnidade): #Função para o cálculo do desperdício, tanto do impacto monetário quanto a porcentagem
    desperdicioMonetario = (qtdProduz - qtdDesper) * precoUnidade
    desperdicioPorcentagem = (qtdDesper * 100) / qtdProduz
    return desperdicioMonetario, desperdicioPorcentagem


def iniciarPrograma(): #Função para inicializar o programa e 
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            adicionarAlimentos()
        elif opcao == '2':
            removerAlimentos()
        elif opcao == '3':
            listarAlimentos()
        elif opcao == '4':
            gerarRelatorio()
        elif opcao == '5':
            gerarRelatorio()
            print("\nPrograma encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

iniciarPrograma()

