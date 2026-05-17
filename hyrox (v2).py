mport os
os.system('cls')


#Projeto: “HYROX Planner”

#Variáveis do tópico 1
titulos = ['Treino', 'Tipo', 'Data', 'Duração', 'Intensidade']
treinos = []
tipos = []
datas = []
duracoes = []
intensidades = []

#Variáveis do tópico 2:
exercicios_especificos = []
exercicios_duracoes = []
exercicios_distancias = []

def atualizar_arquivo_treinos():
    with open('Treinos.txt', 'w', encoding='utf-8') as tre:
        for i in range(len(treinos)):
            tre.write(f"Treino: {treinos[i]} | Tipo: {tipos[i]} | Data: {datas[i]} | Duração: {duracoes[i]} | Intensidade: {intensidades[i]}\n")
            
def atualizar_arquivo_exercicios():
    with open('Exercicios.txt', 'w', encoding='utf-8') as arq_ex:
        for i in range(len(exercicios_especificos)):
            arq_ex.write(f"Exercício: {exercicios_especificos[i]} | Duração: {exercicios_duracoes[i]} | Distância: {exercicios_distancias[i]}\n")

def menu_treinos():
    while True:
        print("\n-------- MENU DE OPÇÕES --------")
        print("Escolha um número para acessar: \n1. Treinos \n2. Exercícios e controle de desempenho\n3. Planejamento de competições \n4. Acompanhamento de evolução \n5. Armazenamento de dados \n6. Sugestões personalizadas \n7. Extra \n8. Sair \nDigite a opção que deseja acessar: "))
        
        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número de 1 a 8.")
            input("Pressione Enter para continuar.")
            continue

        if opcao == 8:
            print("\nAcesso finalizado.")
            break

        elif opcao == 1:
            #opcao de opções para a opção 1 (parte 1 do trab)
            while True:
                print("\n-------- ACESSO AOS TREINOS --------")
                print("1. Adicionar treino \n2. Visualizar treinos \n3. Editar treinos \n4. Excluir treino \n5. Voltar ao Menu Principal")
                try:
                    sub_opcao = int(input("\nDigite o número da opção desejada: "))
                except ValueError:
                    print("Opção inválida! Digite apenas números.")
                    input("Pressione Enter para continuar.")
                    continue
                if sub_opcao == 5:
                    break
                
                #adicionar treino
                elif sub_opcao == 1:
                    treino = input("Adicione o nome do treino desejado: ").capitalize()
                    treinos.append(treino)
                    
                    #adicionar tipo de treino
                    while True:
                        tipo = input("Adicione o tipo de treino: \nC - Corrida \nF - Força \nS - Simulado HYROX \n").upper()
                        if tipo == "C":
                            tipos.append("Corrida")
                            break
                        elif tipo == "F":
                            tipos.append("Força")
                            break
                        elif tipo == "S":
                            tipos.append("Simulado HYROX")
                            break
                        else:
                            print("Opção inválida!")
                        
                #adicionar duração do exercício
                    while True:
                        try: 
                            duracao = int(input("Digite a duração do exercício, em minutos: "))
                            if duracao <= 0:
                                print("Duração inválida. Tente novamente.")
                            elif duracao >= 600:
                                print("Essa duração parece muito grande. Por questões de segurança, digite novamente.")
                            #transformação do exercício em horas e minutos
                            else:
                                horas = str(duracao // 60)
                                minutos = str(duracao%60)
                                valor = str(horas + 'h' + ' ' + minutos + 'min')                
                                duracoes.append(valor)
                                #adicionar data
                                data = input("Digite a data do exercício feito (formato DD/MM/AA): ")        
                                datas.append(data)
                                break
                        except ValueError:
                            print("Erro: Digite um número inteiro válido para os minutos.")

                #adicionar intensidade
                    while True:
                        try:
                            intensidade = int(input("Digite o número correspondente à intensidade do exercício: \n1. Leve\n2. Moderada\n3. Alta\n"))
                            if intensidade == 1:
                                intensidades.append("Leve")
                                break
                            elif intensidade == 2:
                                intensidades.append("Moderada")
                                break
                            elif intensidade == 3:
                                intensidades.append("Alta")
                                break
                            else:
                                print("Opção inválida. Tente novamente")
                        except ValueError:
                            print("Erro: Digite apenas 1, 2 ou 3.")
                            
                        atualizar_arquivo_treinos()
                        print("\nTreino adicionado e salvo com sucesso!")
                        input("Pressione Enter para continuar.")
                    
                #visualizar treinos
                elif sub_opcao == 2:
                    if len(treinos) == 0:
                        print("\nVocê ainda não cadastrou nenhum treino!\n")
                    else:
                        print('\n')
                        for i in range(len(titulos)):
                            print(f'{titulos[i]: <30}', end = '')
                        print('\n' + '-' * 150)
                                
                        for i in range(len(treinos)):
                            print(f'{treinos[i]: <30}', end = '')
                            print(f'{tipos[i]: <30}', end = '')
                            print(f'{datas[i]: <30}', end = '')
                            print(f'{duracoes[i]: <30}', end = '')
                            print(f'{intensidades[i]: <30}', end = '\n')
                        
                            input("\nPressione Enter para voltar ao opcao.")
                            
                    #editar treinos
                elif sub_opcao == 3:
                    if len(treinos) == 0:
                        print("Não há treinos cadastrados para editar.")
                        input("Pressione Enter para continuar.")
                        continue
                    
                    #mostrar os treinos para conferência do usuário
                    print("Treinos cadastrados:")
                    print(*treinos, sep = ', ')
                    
                    nome = input("Digite o nome do treino a ser editado: ").capitalize()
                    
                    #verificação da existência do treino
                    if nome in treinos:
                        indice = treinos.index(nome)
                        print(f"\nEditando o treino '{nome}':")
                        novo_nome = input(f"Digite o novo nome do treino: ").capitalize()
                        
                        while True:
                            novo_tipo = input(f"Digite o novo tipo do exercício de {nome}: \nC - Corrida \nF - Força \nS - Simulado HYROX \n").upper()
                            if novo_tipo == "C":
                                tipo_formatado = "Corrida"
                                break
                            elif novo_tipo == "F":
                                tipo_formatado = "Força"
                                break
                            elif novo_tipo == "S":
                                tipo_formatado = "Simulado HYROX"
                                break
                            else:
                                print("Opção inválida!")
                            
                        nova_data = input("Digite a nova data (DD/MM/AA): ")
                        
                        treinos[indice] = novo_nome
                        tipos[indice] = tipo_formatado
                        datas[indice] = nova_data
                        
                        #salvando as alterações na lista
                        atualizar_arquivo_treinos()
                        print("\nTreino alterado com sucesso!")
                        input("Pressione Enter para continuar.")
                            
                    else:
                        print(f"O treino {nome} não está cadastrado.")
                        input("Pressione Enter para continuar.")
                        
                    #excluir treino        
                elif sub_opcao == 4:
                    if len(treinos) == 0:
                        print("Não há treinos cadastrados para excluir.")
                        input("Pressione Enter para continuar...")
                        continue
                    
                        #mostrar os treinos para conferência do usuário
                    print("Treinos cadastrados:")
                    print(*treinos, sep = ', ')
                    
                    nome = input("Digite o nome do treino a ser excluído: ").capitalize()
                    if nome in treinos:
                        indice = treinos.index(nome)
                        
                        #remove de todas as listas
                        treinos.pop(indice)
                        tipos.pop(indice)
                        datas.pop(indice)
                        duracoes.pop(indice)
                        intensidades.pop(indice)
                        
                        atualizar_arquivo_treinos()
                        print(f"\nTreino '{nome}' removido com sucesso!")
                        input("Pressione Enter para continuar.")
                        
                    else:
                        print(f"o treino {nome} não está cadastrado.")
                        input("Pressione Enter para continuar.")
                    #qualquer outro número dá erro
                else:
                    print("Opção inválida")
                    input("Pressione Enter para continuar.")

        elif opcao == 2:
            while True:
                print("\n-------- EXERCÍCIOS E CONTROLE DE DESEMPENHO --------")
                print("1. Cadastrar exercício específico \n2. Visualizar exercícios e evolução \n3. Voltar ao menu principal")
                
                try:
                    sub_opcao_exercicio = int(input("\nDigite o número da opção desejada: "))
                except ValueError:
                    print("Opção inválida! Digite apenas números.")
                    input("Pressione Enter para continuar.")
                    continue
                
                if sub_opcao_exercicio == 3:
                    break
                
                elif sub_opcao_exercicio == 1:
                    exercicio = input("\nQual desses exercícios deseja adicionar (sled push, sled pull, burpee broad jumps, wall balls, farmer's carry ou outro?)? ").capitalize()
                    if exercicio == "Outro":
                        outro_exercicio = input("Insira o nome do exercício que deseja realizar: ").capitalize()
                        exercicios_especificos.append(outro_exercicio)
                    else: 
                        exercicios_especificos.append(exercicio)
                        
                        
                        
                        
       
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
            pass
    elif opcao == 6:
        pass
    elif opcao == 7:
        pass
    else:
        print("\nOpção inválida. Tente novamente\n")

#2. Exercícios e Controle de Desempenho:
#O usuário poderá cadastrar exercícios específicos do HYROX (como sled push,
#sled pull, burpee broad jumps, wall balls, farmer’s carry, entre outros),
#registrando métricas como tempo, distância, carga e repetições. Esses dados
#permitirão acompanhar a evolução do desempenho ao longo do tempo.

le = []
r = input("Deseja adicionar algum exercício específico?(Responder com S ou N) ").upper
while r == "S": 
    ex = input("Qual desses exercícios deseja adicionar (sled push,sled pull, burpee broad jumps, wall balls, farmer's carry ou outro?) ?").capitalize
    if ex == "Outro":
         ex1 = input("Insira o nome do exercício que deseja realizar: ").capitalize
         le.append(ex1)
    else: 
         le.append(ex)
    durac = int(input("Digite a duração do exercício, em minutos: "))
            #verificação de valores por segurança
    if durac <= 0:
                print("Duração inválida. Tente novamente")
    elif durac >= 600:
                print("Essa duração parece muito grande. Por questões de segurança, digite novamente")
            #transformação do exercício em horas e minutos
    else:
                horas = str(durac // 60)
                minutos = str(durac%60)
                valor = str(horas + 'h' + ' ' + minutos + 'min')                
                le.append(valor)
                tre.write(' | Duração: ' + horas + 'h' + minutos + 'min')
    r1 = input("É necessário percorrer alguma distância para realizar esse exercício? (responder com S ou N) ").upper
    if r1 == "S":
        dist = int("Insira a distância a ser percorrida em metros: ")
        if dist<=0:
             print("Distância inválida. Tente novamente.")
        else:
             km = str(dist//1000)
             metros = str(dist%1000)
             valor1 = str(km + "km"+''+metros + 'm')
             le.append(valor1)
             tre.write(' | Distância: ' + km + 'km' + metros + 'm')


    r = input("Deseja adicionar mais algum exercício específico?(Responder com S ou N) ").upper

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