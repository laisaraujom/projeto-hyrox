import os
os.system('cls')


#Projeto: “HYROX Planner”
#Descrição do Problema:
#Júlia começou a treinar para competições de HYROX, que combina corrida
#com exercícios funcionais de alta intensidade. No entanto, ela tem dificuldade
#em organizar seus treinos, controlar sua evolução, planejar os dias de
#descanso, acompanhar o desempenho em cada modalidade (corrida, sled
#push, burpees, entre outros) e se preparar adequadamente para as
#competições. Pensando nisso, vamos criar o sistema “HYROX Planner”, que
#ajudará Juliana (e outros atletas) a planejar seus treinos, monitorar seu
#desempenho e se preparar melhor para provas.

#Requisitos Funcionais:
#1. CRUD de Treinos:
#O usuário poderá adicionar, visualizar, editar e excluir treinos, com informações
#como: nome do treino, tipo (corrida, força, simulado HYROX), data, duração e
#intensidade.


while True:
    opcao = int(input("Menu de Opções: \n1. Adicionar treino \n2. Visualizar treinos \n3. Editar treinos \n4. Excluir treino \n5. Sair \nDigite o número da opção desejada: "))
    if opcao == 5:
        break
    elif opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
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