import os
from datetime import datetime
os.system('cls')

open("Treinos.txt", "a", encoding='utf-8').close()
open("Exercicios.txt", "a", encoding='utf-8').close()
open("Competicoes.txt", "a", encoding='utf-8').close()
#Projeto: “HYROX Planner”

#Variáveis do tópico 1
titulos = ['Treino', 'Tipo', 'Data', 'Duração', 'Intensidade']
treinos = []
tipos = []
datas = []
duracoes = []
intensidades = []

#Variáveis do tópico 2:
titulos_exercicios = ['Exercício', 'Duração', 'Distância/Reps', 'Data']
exercicios_especificos = []
exercicios_duracoes = []
exercicios_distancias = []
exercicios_datas =[]

#Variáveis do tópico 3:
competicoes_nomes = []
competicoes_datas = []
competicoes_locais = []
competicoes_categorias = []

def atualizar_arquivo_treinos():
    with open('Treinos.txt', 'w', encoding='utf-8') as tre:
        for i in range(len(treinos)):
            tre.write(f"Treino: {treinos[i]} | Tipo: {tipos[i]} | Data: {datas[i]} | Duração: {duracoes[i]} | Intensidade: {intensidades[i]}\n")
            
def atualizar_arquivo_exercicios():
    with open('Exercicios.txt', 'w', encoding='utf-8') as arq_ex:
        for i in range(len(exercicios_especificos)):
            arq_ex.write(f"Exercício: {exercicios_especificos[i]} | Duração: {exercicios_duracoes[i]} | Distância: {exercicios_distancias[i]}\n")
            
def atualizar_arquivo_competicoes():
    with open('Competicoes.txt', 'w', encoding='utf-8') as arq_comp:
        for i in range(len(competicoes_nomes)):
            arq_comp.write(f"Competição: {competicoes_nomes[i]} | Data: {competicoes_datas[i]} | Local: {competicoes_locais[i]} | Categoria: {competicoes_categorias[i]}\n")
def menu_treinos():
    while True:
        print("\n-------- MENU DE OPÇÕES --------\n")
        print("1. Treinos \n2. Exercícios e controle de desempenho\n3. Planejamento de competições \n4. Acompanhamento de evolução \n5. Armazenamento de dados \n6. Sugestões personalizadas \n7. Extra \n8. Sair")
        
        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número de 1 a 8.")
            input("Pressione Enter para continuar.")
            continue
        if opcao == 8:
            print("\nAcesso finalizado.")
            break
        #tópico 1 do trabalho
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
                    arquivo = open('Treinos.txt', 'r', encoding='utf-8')
                    conteudo = arquivo.read()
                    arquivo.close() #Ver depois forma mais otimizada!
                    if conteudo == "": 
                        print("\nVocê ainda não cadastrou nenhum treino!\n")
                    else:
                        print('\n' + '-' * 150)
                        print(conteudo)
                        print('-' * 150)
                        
                    input("\nPressione Enter para voltar ao menu.")
                            
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
                        novo_nome = input("Digite o novo nome do treino: ").capitalize()
                        
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
        #tópico 2 do trabalho
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
                    print("\n-------- CADASTRAR EXERCÍCIO ESPECÍFICO --------")
                    try:
                        exercicio_digitado = int(input("\nQual desses exercícios deseja adicionar? \n1. SkiErg \n2. Sled Push \n3. Sled Pull \n4. Burpee Broad Jumps \n5. Rowing \n6. Farmer's Carry \n7. Sandbag Lunges \n8. Wall Balls \n9. Outro \n\nDigite o número referente à opção desejada: "))
                        if exercicio_digitado == 1:
                            outro_exercicio = 'SkiErg'
                            distancia_padrao = '1000m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                            exercicios_distancias.append(valor_distancia)
                        elif exercicio_digitado == 2:
                            outro_exercicio = 'Sled Push'
                            distancia_padrao = '50m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                            exercicios_distancias.append(valor_distancia)
                        elif exercicio_digitado == 3:
                            outro_exercicio = "Sled Pull"
                            distancia_padrao = '50m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                            exercicios_distancias.append(valor_distancia)
                        elif exercicio_digitado == 4:
                            outro_exercicio = 'Burpee Broad Jumps'
                            distancia_padrao = '80m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                            exercicios_distancias.append(valor_distancia)
                        elif exercicio_digitado == 5:
                            outro_exercicio = 'Rowing'
                            distancia_padrao = '1000m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                            exercicios_distancias.append(valor_distancia)
                        elif exercicio_digitado == 6:
                            outro_exercicio = "Farmer's Carry"
                            distancia_padrao = '200m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                            exercicios_distancias.append(valor_distancia)
                        elif exercicio_digitado == 7:
                            outro_exercicio = 'Sandbag Lunges'
                            distancia_padrao = '100m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                            exercicios_distancias.append(valor_distancia)
                        elif exercicio_digitado == 8:
                            outro_exercicio = 'Wall Balls'
                            print("Exercício a ser cadastrado: Wall Balls.")
                            while True:
                                try:
                                    repeticoes = int(input("Insira a quantidade de repetições (arremessos) feitos: "))
                                    if repeticoes <= 0:
                                        print("Quantidade inválida. Tente novamente.")
                                    else:
                                        exercicios_distancias.append(f"{repeticoes} reps")
                                        break
                                except ValueError:
                                    print("Erro: Digite um número inteiro para as repetições.")
                        elif exercicio_digitado == 9:
                            outro_exercicio = input("Insira o nome do exercício que deseja adicionar: ").capitalize()
                            dist = input("Insira a distância ou repetições para este exercício, indicando a unidade em 'm' ou em 'reps': ")
                            exercicios_distancias.append(dist)
                    except ValueError:
                        print("Erro: Digite um número inteiro válido.")
                        input("Pressione Enter para continuar.")
                        continue
                    
                    #duração do exercício específico
                    while True:
                        try:
                            duracao_input = float(input("\nDigite o tempo (Exemplo: 3min e 45s, digite 3.45): "))
                            if duracao_input <= 0 or duracao_input >= 600:
                                print("Duração inválida. Tente novamente.")
                                continue
                            minutos = int(duracao_input)
                            segundos = round((duracao_input - minutos) * 100)
                            if segundos >= 60:
                                print("Os segundos não podem ser maiores que 59. Use o formato MM.SS.")
                                continue
                            valor_tempo = f"{minutos}min {segundos:02d}s"
                            exercicios_duracoes.append(valor_tempo)
                            break
                        except ValueError:
                            print("Erro: Digite um número decimal válido.")                            
                    while True:
                        data = input("Digite a data do exercício feito (formato DD/MM/AAAA): ")
                        try:
                            data_convertida = datetime.strptime(data, "%d/%m/%Y").date()
                            hoje = datetime.now().date()
                            if data_convertida > hoje:
                                print("Erro: a data inserida não pode estar no futuro.")    
                            else:
                                exercicios_datas.append(data)
                                break  
                        except ValueError:
                            break                    
                    exercicios_especificos.append(outro_exercicio)
                    atualizar_arquivo_exercicios()
                    print("\nExercício gravado com sucesso!")
                    input("Pressione Enter para continuar.")
                elif sub_opcao_exercicio == 2:
                    arquivo = open('Exercicios.txt', 'r', encoding='utf-8')
                    conteudo = arquivo.read()
                    arquivo.close()
                    if conteudo == "":
                        print("\nVocê ainda não cadastrou nenhum exercício específico!\n")
                    else:
                        print("\n-------- VISUALIZAR EXERCÍCIOS E EVOLUÇÃO --------")
                        print('-' * 100)
                        print(conteudo)
                        print('-' * 100)
                        
                    input("\nPressione Enter para voltar ao menu de exercícios.")
                    
        # Tópico 3 do trabalho
        elif opcao == 3:
            while True:
                print("\n-------- PLANEJAMENTO DE COMPETIÇÕES --------")
                print("1. Cadastrar nova competição")
                print("2. Visualizar competições e contagem regressiva")
                print("3. Voltar ao menu principal")
                
                try:
                    sub_opcao_comp = int(input("\nDigite o número da opção desejada: "))
                except ValueError:
                    print("Opção inválida! Digite apenas números.")
                    input("Pressione Enter para continuar.")
                    continue
                
                if sub_opcao_comp == 3:
                    break
                
                elif sub_opcao_comp == 1:
                    print("\n--- Cadastrar Competição ---")
                    nome_comp = input("Nome do evento: ").capitalize()
                    
                    # Verificação da data feita de um jeito mais simples
                    while True:
                        data_comp = input("Digite a data do evento (formato DD/MM/AAAA): ")
                        try:
                            # Apenas testa se a data é válida
                            datetime.strptime(data_comp, "%d/%m/%Y")
                            break
                        except ValueError:
                            print("Formato de data errado. Tente colocar no padrão DD/MM/AAAA.")
                            
                    local_comp = input("Local (Cidade/Estado): ").capitalize()
                    categoria_comp = input("Categoria: ").capitalize()
                    
                    competicoes_nomes.append(nome_comp)
                    competicoes_datas.append(data_comp)
                    competicoes_locais.append(local_comp)
                    competicoes_categorias.append(categoria_comp)
                    
                    atualizar_arquivo_competicoes()
                    print(f"\nA competição {nome_comp} foi salva com sucesso!")
                    input("Pressione Enter para continuar.")
                    
                elif sub_opcao_comp == 2:
                    print("\n--- Minhas Competições ---")
                    if len(competicoes_nomes) == 0:
                        print("Você ainda não tem competições cadastradas.")
                    else:
                        for i in range(len(competicoes_nomes)):
                            dia_hoje = datetime.now().date()
                            dia_da_prova = datetime.strptime(competicoes_datas[i], "%d/%m/%Y").date()
                            
                            conta_dias = dia_da_prova - dia_hoje
                            dias_que_faltam = conta_dias.days
                            
                            if dias_que_faltam > 0:
                                aviso = f"Faltam {dias_que_faltam} dias para a prova!"
                            elif dias_que_faltam == 0:
                                aviso = "É hoje!"
                            else:
                                aviso = "Essa competição já passou."
                                
                            print(f"\n[{aviso}]")
                            print(f"Evento: {competicoes_nomes[i]} | Quando: {competicoes_datas[i]}")
                            print(f"Onde: {competicoes_locais[i]} | Categoria: {competicoes_categorias[i]}")
                            print("-" * 45)
                            
                    input("\nPressione Enter para voltar.")
        else:
            print("\nOpção inválida! Escolha um número de 1 a 8.")
            input("Pressione Enter para continuar.")

menu_treinos()       

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