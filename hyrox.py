import os
from datetime import datetime
from agente import falar_com_agente_streaming

os.system('cls')

open("Treinos.txt", "a", encoding='utf-8').close()
open("Exercicios.txt", "a", encoding='utf-8').close()
open("Competicoes.txt", "a", encoding='utf-8').close()

titulos = ['Treino', 'Tipo', 'Data', 'Duração', 'Intensidade']
treinos = []
tipos = []
datas = []
duracoes = []
intensidades = []

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

duracoes_segundos = []

#limpar terminal
def clear():
    os.system('cls')
#opção 1
def atualizar_arquivo_treinos():
    with open('Treinos.txt', 'w', encoding='utf-8') as tre:
        for i in range(len(treinos)):
            tre.write(f"Treino: {treinos[i]} | Tipo: {tipos[i]} | Duração: {duracoes[i]} | Intensidade: {intensidades[i]} | Data: {datas[i]}\n")
def carregar_treinos():
    if not os.path.exists("Treinos.txt"):
        return

    with open("Treinos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(" | ")

            try:
                treinos.append(partes[0].replace("Treino: ", ""))
                tipos.append(partes[1].replace("Tipo: ", ""))
                duracoes.append(partes[2].replace("Duração: ", ""))
                intensidades.append(partes[3].replace("Intensidade: ", ""))
                datas.append(partes[4].replace("Data: ", ""))      
                
                tempo = partes[2].replace("Duração: ", "")
                tempo = tempo.replace("min", "").replace("s", "")
                minutos, segundos = tempo.split()
                duracoes_segundos.append((int(minutos) * 60) + int(segundos))
            except (IndexError, ValueError):
                continue
#opção 2
def atualizar_arquivo_exercicios():
    with open('Exercicios.txt', 'w', encoding='utf-8') as arq_ex:
        for i in range(len(exercicios_especificos)):
            arq_ex.write(f"Exercício: {exercicios_especificos[i]} | Carga (kg): {exercicios_cargas[i]} | Duração: {exercicios_duracoes[i]} | Distância/Repetições: {exercicios_distancias[i]} | Data: {exercicios_datas[i]}\n")

def carregar_exercicios():
    if not os.path.exists("Exercicios.txt"):
        return

    with open("Exercicios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(" | ")
            try:
                exercicios_especificos.append(partes[0].replace("Exercício: ", ""))
                exercicios_cargas.append(partes[1].replace("Carga (kg): ", ""))
                exercicios_duracoes.append(partes[2].replace("Duração: ", ""))
                exercicios_distancias.append(partes[3].replace("Distância: ", ""))
                exercicios_datas.append(partes[4].replace("Data: ", ""))

                tempo = partes[2].replace("Duração: ", "")
                tempo = tempo.replace("min", "").replace("s", "")
                minutos, segundos = tempo.split()

                exercicios_segundos.append((int(minutos) * 60) + int(segundos))
            except (IndexError, ValueError):
                continue
#opção 3
def atualizar_arquivo_competicoes():
    with open('Competicoes.txt', 'w', encoding='utf-8') as arq_comp:
        for i in range(len(competicoes_nomes)):
            arq_comp.write(f"Competição: {competicoes_nomes[i]} | Data: {competicoes_datas[i]} | Local: {competicoes_locais[i]} | Categoria: {competicoes_categorias[i]}\n")

def carregar_competicoes():
    if not os.path.exists("Competicoes.txt"):
        return

    with open("Competicoes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(" | ")

            try:
                competicoes_nomes.append(partes[0].replace("Competição: ", ""))
                competicoes_datas.append(partes[1].replace("Data: ", ""))
                competicoes_locais.append(partes[2].replace("Local: ", ""))
                competicoes_categorias.append(partes[3].replace("Categoria: ", ""))
            except IndexError:
                continue
#opção 5
def sugestoes_personalizadas():
    print("\n-------- DIVISÃO SEMANAL COM BASE NO NÍVEL DE EXPERIÊNCIA --------")
    print("1. Iniciante\n2. Intermediário\n3. Avançado (Simulado Completo - Oficial)")
    
    try:
        opcao = int(input("\nEscolha o seu nível atual (1-3): "))
        
        # Base de dados
        exercicios = {
            1:  {"nome": "Corrida",             "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            2:  {"nome": "Sled Push",           "iniciante": "20 metros",    "intermediario": "35 metros",    "avancado": "50 metros"},
            3:  {"nome": "Corrida",             "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            4:  {"nome": "Sled Pull",           "iniciante": "20 metros",    "intermediario": "35 metros",    "avancado": "50 metros"},
            5:  {"nome": "Corrida",             "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            6:  {"nome": "Burpee Broad Jump",   "iniciante": "30 metros",    "intermediario": "50 metros",    "avancado": "80 metros"},
            7:  {"nome": "Corrida",             "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            8:  {"nome": "Remo",                "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            9:  {"nome": "Corrida",             "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            10: {"nome": "Farmers Carry",       "iniciante": "30 metros",    "intermediario": "60 metros",    "avancado": "100 metros"},
            11: {"nome": "Corrida",             "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            12: {"nome": "Sandbag Lunges",      "iniciante": "30 metros",    "intermediario": "60 metros",    "avancado": "100 metros"},
            13: {"nome": "Corrida",             "iniciante": "300 metros",   "intermediario": "500 metros",   "avancado": "1.000 metros"},
            14: {"nome": "Wall Balls",          "iniciante": "40 repetições", "intermediario": "70 repetições", "avancado": "100 repetições"}
        }

        if opcao == 1 or opcao == 2:
            nivel_str = "Iniciante" if opcao == 1 else "Intermediário"
            chave_distancia = "iniciante" if opcao == 1 else "intermediario"
            
            # Mostra o menu descrevendo corrido quais são os exercícios de cada bloco
            print(f"\n--- MENU DE TREINOS - NÍVEL {nivel_str.upper()} ---")
            print("Treino A: Corrida, Sled Push, Corrida, Sled Pull, Corrida, Burpee Broad Jump, Corrida.")
            print("Treino B: Remo, Corrida, Farmers Carry, Corrida, Sandbag Lunges, Corrida, Wall Balls.")
            print("Treino C: Circuito Completo (Treino A + Treino B).")
            
            while True:
                escolha_treino = input("\nEscolha o treino do dia (A, B ou C): ").strip().upper()
                
                if escolha_treino == 'A':
                    indices = range(1, 8)
                    titulo_treino = "Treino A (Primeira Metade)"
                    break
                elif escolha_treino == 'B':
                    indices = range(8, 15)
                    titulo_treino = "Treino B (Segunda Metade)"
                    break
                elif escolha_treino == 'C':
                    indices = range(1, 15)
                    titulo_treino = "Treino C (Treino Completo)"
                    break 
                else:
                    print("\n⚠ Opção de treino inválida. Escolha apenas A, B ou C.")
                    input("Pressione Enter para tentar novamente...")

            # distâncias calculadas para o nível
            print(f"\n-----------------------------------")
            print(f"Nível: {nivel_str} | {titulo_treino}")
            print(f"-----------------------------------\n[Estrutura de Treino]")
            
            for i in indices:
                ex = exercicios[i]
                print(f"  {i}. {ex['nome']} - {ex[chave_distancia]}")
                
            cargas_texto = "Escolha uma carga leve que exija apenas um pouco de você." if opcao == 1 else "Escolha uma carga moderada e desafiadora para você."
            estrategia_texto = "Você deve terminar o treino um pouco cansada." if opcao == 1 else "Você deve terminar o treino cansada, mas não exausta."
            
            print(f"\n[Cargas Recomendadas]\n{cargas_texto}")
            print(f"\n[Estratégia do Treino]\n{estrategia_texto}")
            print(f"-----------------------------------")

        elif opcao == 3:
            # Avançado 
            print(f"\n-----------------------------------")
            print(f"Nível: Avançado")
            print(f"-----------------------------------\n[Estrutura de Treino - Simulado Oficial]")
            
            for i in range(1, 15):
                ex = exercicios[i]
                print(f"  {i}. {ex['nome']} - {ex['avancado']}")
                
            print(f"\n[Cargas Recomendadas]\nCargas oficiais da competição de acordo com a sua categoria.")
            print(f"\n[Estratégia do Treino]\nEsta sugestão é um simulado de todas as etapas do HYROX, com as distâncias oficiais.")
            print(f"Aproveite esse treino para testar sua evolução e diminuir o tempo total.")
            print(f"-----------------------------------")
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
            clear()
            continue

        if opcao == 8:
            print("\nAcesso finalizado.\n\n")
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
                    clear()
                    break
                
                
                elif sub_opcao == 1:
                    treino = input("Adicione o nome do treino desejado: ").capitalize()
                    treinos.append(treino)        
                    while True:
                        print ("--- TIPOS DE TREINO --- \nC - Corrida \nF - Força \nS - Simulado HYROX \n")
                        tipo = input("Digite a inicial correspondente ao tipo de treino: ").upper()
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
                            duracoes.append(valor_tempo)
                            duracoes_segundos.append((minutos * 60) + segundos)
                            break
                        except ValueError:
                            print("Erro: Digite um número no formato MM.SS.")
                    
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
                    
                    while True:
                        data = input("Digite a data do evento (formato DD/MM/AA): ")
                        try:
                            datetime.strptime(data, "%d/%m/%y")
                            datas.append(data)
                            break
                        except ValueError:
                            print("Formato de data errado. Tente colocar no padrão DD/MM/AA.")
                
                    atualizar_arquivo_treinos()
                    print("\nTreino adicionado e salvo com sucesso!")
                    input("Pressione Enter para continuar.")
                    clear()
                
                elif sub_opcao == 2:
                    arquivo = open('Treinos.txt', 'r', encoding='utf-8')
                    conteudo = arquivo.read()
                    arquivo.close()

                    if len(treinos) == 0: 
                        print("\nVocê ainda não cadastrou nenhum treino!\n")
                    else:
                        print('\n' + '-' * 150)
                        print(conteudo)
                        print('-' * 150)
                        
                    input("\nPressione Enter para voltar ao menu.")
                    clear()
                
                elif sub_opcao == 3:
                    if len(treinos) == 0:
                        print("Não há treinos cadastrados para editar.")
                        input("Pressione Enter para continuar.")
                        clear()
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
                            
                        while True: 
                            try: 
                                duracao_input = float(input("\nDigite o novo tempo (Exemplo: 3min e 45s, digite 3.45): "))
                                if duracao_input <= 0 or duracao_input >= 600:
                                    print("Duração inválida. Tente novamente.")
                                    continue
                                minutos = int(duracao_input)
                                segundos = round((duracao_input - minutos) * 100)
                                if segundos >= 60:
                                    print("Os segundos não podem ser maiores que 59. Use o formato MM.SS.")
                                    continue
                                nova_duracao = f"{minutos}min {segundos:02d}s"
                            except ValueError:
                                print("Erro: Digite um número no formato MM.SS.")   
                                
                            treinos[indice] = novo_nome
                            tipos[indice] = tipo_formatado
                            duracoes[indice] = nova_duracao
                            duracoes_segundos[indice] = (minutos * 60) + segundos
                                
                            atualizar_arquivo_treinos()
                            print("\nTreino alterado com sucesso!")
                            input("Pressione Enter para continuar.")
                            clear()
                            break
                    else:
                        print(f"O treino {nome} não está cadastrado.")
                        input("Pressione Enter para continuar.")
                        clear()

                elif sub_opcao == 4:
                    if len(treinos) == 0:
                        print("Não há treinos cadastrados para excluir.")
                        input("Pressione Enter para continuar...")
                        clear()
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
                        duracoes_segundos.pop(indice)
                        
                        atualizar_arquivo_treinos()
                        print(f"\nTreino '{nome}' removido com sucesso!")
                        input("Pressione Enter para continuar.")
                        clear()
                        
                    else:
                        print(f"o treino {nome} não está cadastrado.")
                        input("Pressione Enter para continuar.")
                        clear()
                else:
                    print("Opção inválida")
                    input("Pressione Enter para continuar.")
                    clear()
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
                    clear()
                    break
                
                elif sub_opcao_exercicio == 1:
                    print("\n-------- CADASTRAR EXERCÍCIO ESPECÍFICO --------")
                    try:
                        exercicio_digitado = int(input("\nQual desses exercícios deseja adicionar? \n1. SkiErg \n2. Sled Push \n3. Sled Pull \n4. Burpee Broad Jumps \n5. Rowing \n6. Farmer's Carry \n7. Sandbag Lunges \n8. Wall Balls \n9. Outro \n\nDigite o número referente à opção desejada: "))
                        
                        valor_distancia = "" 
                        
                        if exercicio_digitado == 1:
                            outro_exercicio = 'SkiErg'
                            distancia_padrao = '1000m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                        elif exercicio_digitado == 2:
                            outro_exercicio = 'Sled Push'
                            distancia_padrao = '50m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                        elif exercicio_digitado == 3:
                            outro_exercicio = "Sled Pull"
                            distancia_padrao = '50m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                        elif exercicio_digitado == 4:
                            outro_exercicio = 'Burpee Broad Jumps'
                            distancia_padrao = '80m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                        elif exercicio_digitado == 5:
                            outro_exercicio = 'Rowing'
                            distancia_padrao = '1000m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                        elif exercicio_digitado == 6:
                            outro_exercicio = "Farmer's Carry"
                            distancia_padrao = '200m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                        elif exercicio_digitado == 7:
                            outro_exercicio = 'Sandbag Lunges'
                            distancia_padrao = '100m'
                            print(f"Exercício: {outro_exercicio}. Distância padrão: {distancia_padrao}")
                            dist = input("Pressione Enter para manter o padrão ou insira uma nova distância: ")
                            valor_distancia = distancia_padrao if dist == '' else dist
                        elif exercicio_digitado == 8:
                            outro_exercicio = 'Wall Balls'
                            print("Exercício a ser cadastrado: Wall Balls.")
                            while True:
                                try:
                                    repeticoes = int(input("Insira a quantidade de repetições (arremessos) feitos: "))
                                    if repeticoes <= 0:
                                        print("Quantidade inválida. Tente novamente.")
                                    else:
                                        valor_distancia = f"{repeticoes} reps"
                                        break
                                except ValueError:
                                    print("Erro: Digite um número inteiro para as repetições.")
                        elif exercicio_digitado == 9:
                            outro_exercicio = input("Insira o nome do exercício que deseja adicionar: ").capitalize()
                            valor_distancia = input("Insira a distância ou repetições para este exercício, indicando a unidade em 'm' ou em 'reps': ")
                        else:
                            print("Opção inválida.")
                            continue
                    except ValueError:
                        print("Erro: Digite um número inteiro válido.")
                        input("Pressione Enter para continuar.")
                        clear()
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
                            segundos_totais = (minutos * 60) + segundos
                            break
                        except ValueError:
                            print("Erro: Digite um número no formato MM.SS.")

                    while True:
                        data_input = input("Digite a data do exercício feito (formato DD/MM/AA): ")
                        try:
                            data_convertida = datetime.strptime(data_input, "%d/%m/%y").date()
                            hoje = datetime.now().date()
                            if data_convertida > hoje:
                                print("Erro: a data inserida não pode estar no futuro.")
                            else:
                                break
                        except ValueError:
                            print("Formato de data inválido! Use o padrão DD/MM/AA.")

                    carga_exercicios_especificos = input("\nEsse exercício teve uso de carga/peso? (S - Sim / N - Não): ").upper()
                    if carga_exercicios_especificos == "S":
                        peso = int(input("Digite a carga utilizada em kg: "))
                        valor_carga = f"{peso} kg"
                    else:
                        valor_carga = "Sem carga"

                    exercicios_especificos.append(outro_exercicio)
                    exercicios_distancias.append(valor_distancia)
                    exercicios_duracoes.append(valor_tempo)
                    exercicios_segundos.append(segundos_totais)
                    exercicios_datas.append(data_input)
                    exercicios_cargas.append(valor_carga)

                    atualizar_arquivo_exercicios()
                    print("\nExercício gravado com sucesso!")
                    input("Pressione Enter para continuar.")
                    clear()

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
                    clear()
                    
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
                    clear()
                    continue
                
                if sub_opcao_comp == 3:
                    clear()
                    break
                
                elif sub_opcao_comp == 1:
                    print("\n--- Cadastrar Competição ---")
                    nome_comp = input("Nome do evento: ").upper()
                    
                    while True:
                        data_comp = input("Digite a data do evento (formato DD/MM/AA): ")
                        try:
                            datetime.strptime(data_comp, "%d/%m/%y")
                            break
                        except ValueError:
                            print("Formato de data errado. Tente colocar no padrão DD/MM/AA.")
                            
                    local_comp = input("Local (Cidade/Estado): ").upper()
                    categoria_comp = input("Categoria: ").upper()
                    
                    competicoes_nomes.append(nome_comp)
                    competicoes_datas.append(data_comp)
                    competicoes_locais.append(local_comp)
                    competicoes_categorias.append(categoria_comp)
                    
                    atualizar_arquivo_competicoes()
                    print(f"\nA competição {nome_comp} foi salva com sucesso!")
                    input("Pressione Enter para continuar.")
                    clear()
                    
                elif sub_opcao_comp == 2:
                    print("\n--- Minhas Competições ---")
                    if len(competicoes_nomes) == 0:
                        print("Você ainda não tem competições cadastradas.")
                    else:
                        for i in range(len(competicoes_nomes)):
                            dia_hoje = datetime.now().date()
                            dia_da_prova = datetime.strptime(competicoes_datas[i], "%d/%m/%y").date()
                            
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
                    clear()

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
                    clear()
                    break
                
                elif sub_opcao_evolucao == 1:
                    print("\n" + "="*85)
                    print(f"{'NOME DO TREINO':<25} | {'QTD':<5} | {'TEMPO MÍN':<12} | {'TEMPO MÁX':<12} | {'TIPO':<15}")
                    print("="*85)
                
                    if len(treinos) == 0:
                        print("\nVocê ainda não cadastrou nenhum treino!")
                        input("Pressione Enter para continuar.")
                        clear()
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
                                tempo_em_minutos = duracoes_segundos[j]
                                
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
                    clear()
                    
                elif sub_opcao_evolucao == 2:
                    texto_melhor_tempo = "N.A."
                    texto_pior_tempo = "N.A."
                    if len(exercicios_especificos) == 0:
                        print("\nVocê ainda não cadastrou nenhum exercício específico!")
                        input("Pressione Enter para continuar.")
                        clear()
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
                    clear()

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
                        var = 0
                        while var != '':
                            var = input("Pressione enter para voltar para o menu: ")
                        clear()
                    elif opcao == 3:
                        clear()
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
                        var = 0
                        while var != '':
                            var = input("Pressione enter para voltar para o menu: ")
                        break
                    elif opcao_desejada == 2:
                        falar_com_agente_streaming('Treinos.txt', "HYROX")
                        var = 0
                        while var != '':
                            var = input("Pressione enter para voltar para o menu: ")
                        break
                    elif opcao_desejada == 3:
                        falar_com_agente_streaming('Competicoes.txt', "HYROX")
                        var = 0
                        while var != '':
                            var = input("Pressione enter para voltar para o menu: ")
                        break
                    elif opcao_desejada == 4:
                        clear()
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Opção inválida! \nPressione enter para continuar")
                    input()
                    clear()
                    break
        else:
            print("\nOpção inválida! Escolha um número de 1 a 8.")
            input("Pressione Enter para continuar.")
            clear()
            
carregar_treinos()
carregar_exercicios()
carregar_competicoes()            
menu_treinos()