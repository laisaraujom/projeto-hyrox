import os
os.system('cls' if os.name == 'nt' else 'clear')

#Projeto: “HYROX Planner”
#Descrição do Problema:
#Júlia começou a treinar para competições de HYROX, que combina corrida com exercícios funcionais de alta intensidade. No entanto, ela tem dificuldade 
# em organizar seus treinos, controlar sua evolução, planejar os dias de descanso, acompanhar o desempenho em cada modalidade (corrida, sled push, burpees, entre outros)
#e se preparar adequadamente para as competições. Pensando nisso, vamos criar o sistema “HYROX Planner”, que ajudará Juliana (e outros atletas) a planejar seus treinos, 
#monitorar seu desempenho e se preparar melhor para provas.


# treinos
# exercícios e controle de desempenho
# planejamento de competições
# acompanhamento de evolução
# armazenamento de dados
# sugestões personalizadas
# acompanhamento corporal (extra?)

#Requisitos Funcionais:
#1. CRUD de Treinos:
#O usuário poderá adicionar, visualizar, editar e excluir treinos, com informações
#como: nome do treino, tipo (corrida, força, simulado HYROX), data, duração e
#intensidade.
tre=open('Treinos.txt', 'a', encoding='utf-8')
titulos = ['Treino', 'Tipo', 'Data', 'Duração', 'Intensidade']
treinos = []
tipos = []
datas = []
duracoes = []
intensidades = []
#menu de opções
while True:
    opcao = int(input("Menu de Opções: \n1. Adicionar treino \n2. Visualizar treinos \n3. Editar treinos \n4. Excluir treino \n5. Sair \n\nDigite o número da opção desejada: "))
    #sair
    if opcao == 5:
        break
    #adicionar treino
    elif opcao == 1:
        treino = input("Adicione o nome do treino desejado: ").capitalize()
        treinos.append(treino)
        tre.write('Treino: ' + treino)
        #adicionar tipo de treino
        while True:
            tipo = input("Adicione o tipo de treino: \nC - Corrida \nF - Força \nS - Simulado HYROX \n").capitalize()
            if tipo == "C":
                tipos.append("Corrida")
                tre.write(' | Tipo: ' + 'Corrida')
                break
            elif tipo == "F":
                tipos.append("Força")
                tre.write(' | Tipo: ' + 'Força')
                break
            elif tipo == "S":
                tipos.append("Simulado HYROX")
                tre.write(' | Tipo: ' + 'Simulado HYROX')
                break
            else:
                print("Opção inválida!")
        #adicionar duração do exercício
        while True:
            duracao = int(input("Digite a duração do exercício, em minutos: "))
            #verificação de valores por segurança
            if duracao <= 0:
                print("Duração inválida. Tente novamente")
            elif duracao >= 600:
                print("Essa duração parece muito grande. Por questões de segurança, digite novamente")
            #transformação do exercício em horas e minutos
            else:
                horas = str(duracao // 60)
                minutos = str(duracao%60)
                valor = str(horas + 'h' + ' ' + minutos + 'min')                
                duracoes.append(valor)
                tre.write(' | Duração: ' + horas + 'h' + minutos + 'min')
                break
        #adicionar data
        data = input("Digite a data do exercício feito (formato DD/MM/AA): ")        
        datas.append(data)
        tre.write(' | Data: ' + data)
        #adicionar intensidade
        while True:
            intensidade = int(input("Digite o número correspondente à intensidade do exercício: \n1. Leve\n2. Moderada\n3. Alta\n"))
            if intensidade == 1:
                intensidades.append("Leve")
                tre.write(' | Intensidade: ' + 'Leve\n')
                break
            elif intensidade == 2:
                intensidades.append("Moderada")
                tre.write(' | Intensidade: ' + 'Moderada\n')
                break
            elif intensidade == 3:
                intensidades.append("Alta")
                tre.write(' | Intensidade: ' + 'Alta\n')
                break
            else:
                print("Opção inválida. Tente novamente")
    #visualizar treinos
    elif opcao == 2:
        for i in range(len(titulos)):
            print(f'{titulos[i]: <30}', end = '')
        print('\n')
        for i in range (len(treinos)):
            print(f'{treinos[i]: <30}', end = '')
            print(f'{tipos[i]: <30}', end = '')
            print(f'{datas[i]: <30}', end = '')
            print(f'{duracoes[i]: <30}', end = '')
            print(f'{intensidades[i]: <30}', end = '\n')
    #editar treinos
    elif opcao == 3:
        #mostrar os treinos para conferência do usuário
        print(*treinos, sep = ', ')
        while True:
            nome = input("Digite o nome do treino a ser editado: ").capitalize()
            #verificação da existência do treino
            if nome in treinos:
                #substituição do treino
                novo_nome = input(f"Digite o novo nome do {nome}: ").capitalize()
                novo_tipo = input(f"Digite o novo tipo do exercício de {nome}: \nCorrida \nForça \nSimulado HYROX \n").upper()
                indice = treinos.index(nome)
                treinos[indice] = novo_nome
                tipos[indice] = novo_tipo
                break
            else:
                print(f"o treino {nome} não está cadastrado")
    #excluir treino        
    elif opcao == 4:
        #mostrar os treinos para conferência do usuário
        print(*treinos, sep = ', ')
        while True:
            nome = input("Digite o nome do treino a ser excluído: ").capitalize()
            #mesma verificação
            if nome in treinos:
                indice = treinos.index(nome)
                treinos.pop(indice)
                tipos.pop(indice)
                break
            else:
                print(f"o treino {nome} não está cadastrado")
    #qualquer outro número dá erro
    else:
        print("Opção inválida")


#2. Exercícios e Controle de Desempenho:
#O usuário poderá cadastrar exercícios específicos do HYROX (como sled push,
#sled pull, burpee broad jumps, wall balls, farmer’s carry, entre outros),
#registrando métricas como tempo, distância, carga e repetições. Esses dados
#permitirão acompanhar a evolução do desempenho ao longo do tempo.


#3. Planejamento de Competições:
#O usuário poderá cadastrar competições futuras, informando data, local e
#categoria. Ao visualizar uma competição, o sistema deverá exibir quantos dias
#faltam para o evento.

while True:
    pass


#4. Acompanhamento de Evolução:
#O sistema deverá apresentar um resumo da evolução do atleta, como
#frequência de treinos, melhora de tempos e aumento de cargas ao longo do
#tempo.


#5. Armazenamento de Dados:
#Todos os registros serão salvos em arquivo .csv ou .txt, garantindo que o
#histórico de treinos, desempenho e competições esteja sempre acessível.


#6. Sugestões Personalizadas:
#Com base no nível do atleta (iniciante, intermediário ou avançado) e nos
#resultados anteriores, o sistema poderá sugerir treinos, divisão semanal, cargas
#ideais e estratégias para melhorar o desempenho em cada etapa do HYROX.


#7. Funcionalidade Extra:
#Sejam criativos.

#Requisitos não funcionais:
#1. Deve ser feito em Python sem o uso de bibliotecas adicionais.
#Utilizar a linha de comando para entrada e saída (interação pelo terminal);
#a. Exceções de bibliotecas:
#os -> os.system("clear") ou “cls”.
#datetime , random...
#Se precisar de outra biblioteca, verifique antes com os professores.
#
#3. O código deve estar organizado, portanto, deve conter:
#a. Funções para dividir o código de forma lógica e evitar repetições;
#b. Tratamento de exceções, para garantir que seu código esteja pronto para
#tratar casos inesperados.
#c. Legibilidade do código, incluindo nomeação de variáveis e funções.
#4. Deve ser feito um manual do usuário, explicando como utilizar a ferramenta e
#restrições gerais que a aplicação tenha.
#a. Fiquem à vontade para escolher como será feito esse manual. Pode ser um
#pdf, site, vídeo, carta...
#b. O manual é o readme que pode estar disponível no github do projeto (caso o
#grupo utilize o github, opcional, não será visto em sala de aula).

#6. Apresentação:
#a. A equipe deve apresentar o projeto feito para os professores.
#b. Todos envolvidos da equipe devem explicar alguma parte, e perguntas
#direcionadas serão feitas durante a apresentação.
#7. A entrega será em uma atividade do classroom
#a. O que deve ser entregue: Código da aplicação e Manual do usuário.
