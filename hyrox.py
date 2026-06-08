import os
from datetime import datetime
from agente import falar_com_agente_streaming

os.system('clear')

# open("Treinos.txt", "a", encoding='utf-8').close()
# open("Exercicios.txt", "a", encoding='utf-8').close()
# open("Competicoes.txt", "a", encoding='utf-8').close()

titulos = ['Treino', 'Tipo', 'Data', 'Duração', 'Intensidade']
treinos = []
tipos = []
datas = []
duracoes = []
intensidades = []
cargas_treinos = []

titulos_exercicios = ['Exercício', 'Duração', 'Distância/Reps', 'Data']
exercicios_especificos = []
exercicios_duracoes = []
exercicios_distancias = []
exercicios_datas = []
exercicios_cargas = []
exercicios_segundos = []

competicoes_nomes = []
competicoes_datas = []
competicoes_locais = []
competicoes_categorias = []

duracoes_minutos = []


#opção 1
def atualizar_arquivo_treinos():
    with open('Treinos.txt', 'w', encoding='utf-8') as tre:
        for i in range(len(treinos)):
            tre.write(f"Treino: {treinos[i]} | Tipo: {tipos[i]} | Carga: {cargas_treinos[i]} | Duração: {duracoes[i]} | Intensidade: {intensidades[i]} | Data: {datas[i]} |\n")
            

#opção 2
def atualizar_arquivo_exercicios():
    with open('Exercicios.txt', 'w', encoding='utf-8') as arq_ex:
        for i in range(len(exercicios_especificos)):
            arq_ex.write(f"Exercício: {exercicios_especificos[i]} | Carga: {exercicios_cargas[i]} | Duração: {exercicios_duracoes[i]} | Distância: {exercicios_distancias[i]} | Data: {exercicios_datas[i]}\n")

#opção 3
def atualizar_arquivo_competicoes():
    with open('Competicoes.txt', 'w', encoding='utf-8') as arq_comp:
        for i in range(len(competicoes_nomes)):
            arq_comp.write(f"Competição: {competicoes_nomes[i]} | Data: {competicoes_datas[i]} | Local: {competicoes_locais[i]} | Categoria: {competicoes_categorias[i]}\n")

#opção 5
def sugestoes_personalizadas():
    print("\n-------- DIVISÃO SEMANAL COM BASE NO NÍVEL DE EXPERIÊNCIA --------")
    print("1. Iniciante\n2. Intermediário\n3. Avançado")
    try:
        opcao = int(input("\nEscolha o seu nível atual (1-3): "))
        niveis = {
            1: {"nivel": "Iniciante", "Divisão": "3x na semana (1x Força, 1x Corrida, 1x Simulação leve)", "cargas": "Sled Push: 75kg | Wall Balls: 4kg", "Estratégia": "Foque em completar os exercícios. Pace confortável."},
            2: {"nivel": "Intermediário", "Divisão": "4 a 5x na semana (2x Força, 2x Corrida, 1x Simulação)", "cargas": "Sled Push: 125kg | Wall Balls: 6kg (M)/4kg (F)", "Estratégia": "Trabalhe as transições (Roxzone)."},
            3: {"nivel": "Avançado", "Divisão": "6x na semana (2x Força, 3x Corrida com intervalos, 1x Simulação)", "cargas": "Sled Push: 175kg | Wall Balls: 9kg (M)/6kg (F)", "Estratégia": "Foque no pace de corrida entre as estações."}
        }
        if opcao in niveis:
            d = niveis[opcao]
            print(f"\nNível: {d['nivel']}\nDivisão Semanal: {d['Divisão']}\nCargas Ideais: {d['cargas']}\nEstratégia: {d['Estratégia']}")
        else:
            print("\nOpção inválida. Escolha um número entre 1 e 3.")
    except ValueError:
        print("\nErro: Digite um número inteiro válido.")
    input("\nPressione Enter para voltar ao menu.")

#opcao 6
def ordenar_datas():
    dados = []
    if not os.path.exists("pesos.txt"):
        return []

    with open("pesos.txt", "r") as f:
        for linha in f:
            linha_limpa = linha.strip()
            if not linha_limpa:
                continue
                
            partes = linha_limpa.split(",")
            if len(partes) == 4:
                try:
                    dados.append({
                        "data": partes[0],
                        "total": float(partes[1]),
                        "magra": float(partes[2]),
                        "gorda": float(partes[3])
                    })
                except ValueError:
                    continue
    try:
        dados.sort(key=lambda x: datetime.strptime(x["data"], "%d/%m/%y"))
    except ValueError:
        print("Erro: Formato de data inválido.")
    return dados

def cadastrar_pesos():
    print("1. Cadastro de bioimpedância")
    data = input("Data (dd/mm/aa): ")
    try:
        datetime.strptime(data, "%d/%m/%y")
        t = float(input("Peso Total (kg): "))
        m = float(input("Massa Muscular (kg): "))
        g = float(input("Massa de Gordura (kg): "))
        
        with open("pesos.txt", "a") as f:
            f.write(f"{data},{t},{m},{g}\n")
        print("\nRegistro adicionado.")
    except ValueError:
        print("\nErro: Formato de data inválido ou números incorretos.")

def exibir_evolucao_valores():
    dados = ordenar_datas()
    if not dados:
        print("\n[!] Nenhum registro encontrado no arquivo pesos.txt.")
        return

    print("\n" + "="*71)
    print(f"{'DATA':<10} | {'TOTAL':<16} | {'M. MUSCULAR':<16} | {'M. GORDURA':<16}")
    print("-" * 71)

    for i in range(len(dados)):
        atual = dados[i]
        
        if i == 0:
            v_t, v_m, v_g = "       ", "       ", "       "
        else:
            anterior = dados[i-1]
            dt = atual['total'] - anterior['total']
            dm = atual['magra'] - anterior['magra']
            dg = atual['gorda'] - anterior['gorda']

            def fmt_v(v):
                s = "+" if v > 0 else ""
                return f"({s}{v:.1f})" if v != 0 else "( 0.0)"

            v_t = f"{fmt_v(dt):>7}"
            v_m = f"{fmt_v(dm):>7}"
            v_g = f"{fmt_v(dg):>7}"

        c_t = f"{atual['total']:>5.1f} kg {v_t}"
        c_m = f"{atual['magra']:>5.1f} kg {v_m}"
        c_g = f"{atual['gorda']:>5.1f} kg {v_g}"

        print(f"{atual['data']:<10} | {c_t:<16} | {c_m:<16} | {c_g:<16}")

    print("="*71)
    print("Legenda: (+) Ganho | (-) Perda")

#menu geral
def menu_treinos():
    while True:
        print("\n-------- MENU DE OPÇÕES --------\n")
        print("1. Treinos \n2. Exercícios e controle de desempenho\n3. Planejamento de competições \n4. Acompanhamento de evolução \n5. Sugestões personalizadas \n6. Acompanhamento de composição corporal \n7. Falar com agente \n8. Sair")
        
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
                
                
                elif sub_opcao == 1:
                    treino = input("Adicione o nome do treino desejado: ").capitalize()
                    treinos.append(treino)
                    
                    
                    while True:
                        print ("--- TIPOS DE TREINO --- \nC - Corrida \nF - Força \nS - Simulado HYROX \n")
                        tipo = input("Digite a inicial correspondente ao tipo de treino: ").upper()
                        if tipo == "C":
                            tipos.append("Corrida")
                            cargas_treinos.append("N.A.")
                            break
                        elif tipo == "F":
                            tipos.append("Força")
                            carga = float(input("Digite a carga utilizada em kg: "))
                            cargas_treinos.append(carga)
                            break
                        elif tipo == "S":
                            tipos.append("Simulado HYROX")
                            cargas_treinos.append("N.A.")
                            break
                        else:
                            print("Opção inválida!")
                        
                    
                    while True:
                        try: 
                            duracao = int(input("Digite a duração do exercício, em minutos: "))
                            if duracao <= 0:
                                print("Duração inválida. Tente novamente.")
                            elif duracao >= 600:
                                print("Essa duração parece muito grande. Por questões de segurança, digite novamente.")
                            else:
                                horas = str(duracao // 60)
                                minutos = str(duracao % 60)
                                valor = str(horas + 'h' + ' ' + minutos + 'min')                
                                duracoes.append(valor)
                                duracoes_minutos.append(duracao)
                                
                                data = input("Digite a data do exercício feito (formato DD/MM/AA): ")        
                                datas.append(data)
                                break
                        except ValueError:
                            print("Erro: Digite um número inteiro válido para os minutos.")

                    
                    while True:
                        try:
                            print ("--- INTENSIDADES ---\n1. Leve\n2. Moderada\n3. Alta\n")
                            intensidade = int(input("Digite o número correspondente à intensidade do exercício: "))
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
                    
                
                elif sub_opcao == 2:
                    arquivo = open('Treinos.txt', 'r', encoding='utf-8')
                    conteudo = arquivo.read()
                    arquivo.close()

                    if conteudo == "": 
                        print("\nVocê ainda não cadastrou nenhum treino!\n")
                    else:
                        print('\n' + '-' * 150)
                        print(conteudo)
                        print('-' * 150)
                        
                    input("\nPressione Enter para voltar ao menu.")
                            
                
                elif sub_opcao == 3:
                    if len(treinos) == 0:
                        print("Não há treinos cadastrados para editar.")
                        input("Pressione Enter para continuar.")
                        continue
                    
                    print("Treinos cadastrados:")
                    print(*treinos, sep = ', ')
                    
                    nome = input("Digite o nome do treino a ser editado: ").capitalize()
                    
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
                        
                        atualizar_arquivo_treinos()
                        print("\nTreino alterado com sucesso!")
                        input("Pressione Enter para continuar.")
                            
                    else:
                        print(f"O treino {nome} não está cadastrado.")
                        input("Pressione Enter para continuar.")
    
                elif sub_opcao == 4:
                    if len(treinos) == 0:
                        print("Não há treinos cadastrados para excluir.")
                        input("Pressione Enter para continuar...")
                        continue
                    
                    print("Treinos cadastrados:")
                    print(*treinos, sep = ', ')
                    
                    nome = input("Digite o nome do treino a ser excluído: ").capitalize()
                    if nome in treinos:
                        indice = treinos.index(nome)
                        
                        treinos.pop(indice)
                        tipos.pop(indice)
                        datas.pop(indice)
                        duracoes.pop(indice)
                        intensidades.pop(indice)
                        duracoes_minutos.pop(indice)
                        cargas_treinos.pop(indice)
                        
                        atualizar_arquivo_treinos()
                        print(f"\nTreino '{nome}' removido com sucesso!")
                        input("Pressione Enter para continuar.")
                        
                    else:
                        print(f"o treino {nome} não está cadastrado.")
                        input("Pressione Enter para continuar.")
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
                            exercicios_segundos.append((minutos * 60) + segundos)
                            break
                        except ValueError:
                            print("Erro: Digite um número decimal válido.")

                    while True:
                        data = input("Digite a data do exercício feito (formato DD/MM/AA): ")
                        try:
                            data_convertida = datetime.strptime(data, "%d/%m/%y").date()
                            hoje = datetime.now().date()
                            if data_convertida > hoje:
                                print("Erro: a data inserida não pode estar no futuro.")    
                            else:
                                exercicios_datas.append(data)
                                break  
                        except ValueError:
                            print("Formato de data inválido! Use o padrão DD/MM/AA.") 
                            
                    carga_exercicios_especificos = input("\nEsse exercício teve uso de carga/peso? (S - Sim / N - Não): ").upper()
                    if carga_exercicios_especificos == "S":
                        peso = int(input("Digite a carga utilizada em kg: "))
                        exercicios_cargas.append(peso)
                    else:
                        exercicios_cargas.append("Sem carga")
                        
                    exercicios_especificos.append(outro_exercicio)
                    atualizar_arquivo_exercicios()
                    print("\nExercício gravado com sucesso!")
                    input("Pressione Enter para continuar.")

                elif sub_opcao_exercicio == 2:
                    arquivo = open('Exercicios.txt', 'r', encoding='utf-8')
                    conteudo = arquivo.read()
                    arquivo.close()

                    if len(exercicios_especificos) == 0:
                        print("\nVocê ainda não cadastrou nenhum exercício específico!\n")
                    else:
                        print("\n-------- VISUALIZAR EXERCÍCIOS --------")
                        print('-' * 100)
                        print(conteudo)
                        print('-' * 100)
                        
                    input("\nPressione Enter para voltar ao menu de exercícios.")
                    
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
                    
                    while True:
                        data_comp = input("Digite a data do evento (formato DD/MM/AAAA): ")
                        try:
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

        elif opcao == 4:
            while True:
                print("\n-------- ACOMPANHAMENTO DE EVOLUÇÃO --------")
                print("1. Treinos")
                print("2. Exercícios Específicos (Cargas, repetições e tempos)")
                print("3. Voltar ao Menu Principal")
                
                try:
                    sub_opcao_evolucao = int(input("\nDigite o número da opção desejada: "))
                    
                except ValueError:
                    print("Opção inválida! Digite apenas números.")
                    input("Pressione Enter para continuar.")
                    continue
                
                if sub_opcao_evolucao == 3:
                    break
                
                elif sub_opcao_evolucao == 1:
                    print("\n" + "="*85)
                    print(f"{'NOME DO TREINO':<25} | {'QTD':<5} | {'TEMPO MÍN':<12} | {'TEMPO MÁX':<12} | {'TIPO':<15}")
                    print("="*85)
                
                    if len(treinos) == 0:
                        print("\nVocê ainda não cadastrou nenhum treino!")
                        input("Pressione Enter para continuar.")
                        continue
                    
                    treinos_analisados = []
                    
                    for i in range(len(treinos)):
                        nome_atual = treinos[i]
                        
                        if nome_atual in treinos_analisados:
                            continue
                        
                        quantidade = 0
                        min_minutos = 9999999
                        max_minutos = -1
                        tempo_min_formatado = ""
                        tempo_max_formatado = ""
                        tipo_treino = tipos[i]
                        
                        for j in range(len(treinos)):
                            if treinos[j] == nome_atual:
                                quantidade += 1
                                
                                tempo_em_minutos = duracoes_minutos[j]
                                
                                if tempo_em_minutos < min_minutos:
                                    min_minutos = tempo_em_minutos
                                    tempo_min_formatado = duracoes[j]
                                    
                                if tempo_em_minutos > max_minutos:
                                    max_minutos = tempo_em_minutos
                                    tempo_max_formatado = duracoes[j]
                                    
                        print(f"{nome_atual:<25} | {quantidade:<5} | {tempo_min_formatado:<12} | {tempo_max_formatado:<12} | {tipo_treino:<15}")
                        treinos_analisados.append(nome_atual)
                    
                    print("="*85)
                    input("\nPressione Enter para continuar.")
                    
                elif sub_opcao_evolucao == 2:
                    texto_melhor_tempo = "N.A."
                    texto_pior_tempo = "N.A."
                    if len(exercicios_especificos) == 0:
                        print("\nVocê ainda não cadastrou nenhum exercício específico!")
                        input("Pressione Enter para continuar.")
                        continue
                    print("\n" + "="*115)
                    print(f"{'NOME DO EXERCÍCIO':<25} | {'QTD':<5} | {'TEMPO MÍN':<12} | {'TEMPO MÁX':<12} | {'CARGA INICIAL': <12} | {'CARGA ATUAL': <12} | {'MAIOR DIST/REPS': <22}")
                    print("="*115)
                    
                    exercicios_analisados = []
                    
                    for i in range(len(exercicios_especificos)):
                        nome_atual = exercicios_especificos[i]
                        
                        if nome_atual in exercicios_analisados:
                            continue
                        
                        quantidade = 0
                        menor_tempo_segundos = 999999  
                        maior_tempo_segundos = -1
                        
                        texto_carga_inicial = "Sem carga"
                        texto_carga_atual = "Sem carga"
                        achou_primeira_carga = False
                        
                        for j in range(len(exercicios_especificos)):
                            if exercicios_especificos[j] == nome_atual:
                                quantidade = quantidade + 1
                                
                                tempo_total_segundos = exercicios_segundos[j]
                                
                                if tempo_total_segundos < menor_tempo_segundos:
                                    menor_tempo_segundos = tempo_total_segundos
                                    texto_melhor_tempo = exercicios_duracoes[j]
                                    
                                if tempo_total_segundos > maior_tempo_segundos:
                                    maior_tempo_segundos = tempo_total_segundos
                                    texto_pior_tempo = exercicios_duracoes[j]
                                    
                                if exercicios_cargas[j] != "Sem carga":
                                    if not achou_primeira_carga:
                                        texto_carga_inicial = f"{exercicios_cargas[j]}kg"
                                        achou_primeira_carga = True
                                    
                                    texto_carga_atual = f"{exercicios_cargas[j]}kg"
                        
                        exemplo_distancia = exercicios_distancias[i]
                        
                        print(f"{nome_atual:<25} | {quantidade:<5} | {texto_melhor_tempo:<12} | {texto_pior_tempo:<12} | {texto_carga_inicial:<13} | {texto_carga_atual:<11} | {exemplo_distancia:<22}")
                        
                        exercicios_analisados.append(nome_atual)
                        
                    print("="*115)
                    input("\nPressione Enter para continuar.")

        elif opcao == 5:
            sugestoes_personalizadas()
            
        elif opcao == 6:
            while True:
                print("\n-------- ACOMPANHAMENTO DE COMPOSIÇÃO CORPORAL --------\n")
                print("1. Cadastrar bioimpedância")
                print("2. Ver evolução da composição corporal")
                print("3. Sair")
        
                try:
                    opcao = int(input("\nEscolha uma opção: "))
                    if opcao == 1:
                        cadastrar_pesos()
                    elif opcao == 2:
                        exibir_evolucao_valores()
                    elif opcao == 3:
                        break
                    else:
                        print("\nOpção inválida! Tente novamente")        
                except ValueError:
                    print("Erro: Digite um número inteiro válido.")

        elif opcao == 7:
            print("\n1. Falar com o agente sobre os exercícios cadastrados\n2. Falar com o agente sobre os treinos cadastrados\n3. Falar com o agente sobre as competições cadastradas\n4. Voltar ao menu principal")
            while True:
                try:
                    opcao_desejada = int(input("Digite o número da opção desejada: "))
                    if opcao_desejada == 1:
                        falar_com_agente_streaming('Exercicios.txt', "HYROX")
                        break
                    elif opcao_desejada == 2:
                        falar_com_agente_streaming('Treinos.txt', "HYROX")
                        break
                    elif opcao_desejada == 3:
                        falar_com_agente_streaming('Competicoes.txt', "HYROX")
                        break
                    elif opcao_desejada == 4:
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Opção inválida! \nPressione enter para continuar")
                    input()
                    break
        else:
            print("\nOpção inválida! Escolha um número de 1 a 9.")
            input("Pressione Enter para continuar.")
menu_treinos()