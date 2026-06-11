## Este projeto foi desenvolvido por: 
Ana Júlia Melo, Ana Luiza Câmara, Arthur Marenga, Beatriz Vieira, Laís Moura e Victor Telles.

## Créditos
Este projeto utiliza um módulo de agente fornecido pelo mentor Victor Costa

# HYROX Planner

Este projeto foi desenvolvido em Python para ajudar atletas a organizarem e acompanharem toda a rotina de preparação para o HYROX. O programa permite salvar os treinos diários, marcar os tempos das estações específicas da modalidade, gerenciar o calendário de provas, controlar o peso/composição corporal e falar com um bot de IA.

---

## Menu principal

1. **Gestão de Treinos:** Permite cadastrar, ver, editar e apagar treinos de Corrida (C), Força (F) ou Simulados HYROX (S).
2. **Exercícios e Controle de Desempenho:** Registro dos tempos, distâncias e cargas de cada exercício feito.
3. **Planejamento de Competições:** Cronograma das próximas provas com contagem regressiva automática.
4. **Acompanhamento de Evolução:** Relatório que mostra a quantidade de treinos feitos, seus melhores e piores tempos e como está a progressão de cargas.
5. **Sugestões Personalizadas:** Dicas de divisões de treino na semana e metas de carga com base no seu nível (Iniciante, Intermediário ou Avançado).
6. **Composição Corporal (Bioimpedância):** Histórico de peso, massa magra e gordura. O sistema calcula sozinho se você ganhou ou perdeu peso em relação ao último registro.
7. **Falar com o Agente:** Abre um chat com IA via streaming para analisar os dados dos seus arquivos e tirar dúvidas.

---

## Manual do Usuário

### 1. Menu de Treinos
* **Adicionar Treino:** Escolha se o treino foi de Corrida, Força ou Simulado.
* **Onde salva:** Todos os treinos vão direto para o arquivo `Treinos.txt`.

### 2. Exercícios Específicos HYROX
Na hora de cadastrar, o sistema lista as 8 estações oficiais do HYROX e já sugere a distância padrão de cada uma (você pode mudar se quiser):
* `SkiErg` (1000m) e `Rowing` (1000m)
* `Sled Push` (50m) e `Sled Pull` (50m)
* `Burpee Broad Jumps` (80m)
* `Farmer's Carry` (200m)
* `Sandbag Lunges` (100m)
* `Wall Balls` (Aqui o sistema pede para você digitar o número de repetições)
* *Esses dados ficam salvos em `Exercicios.txt`.*

### 3. Planejamento de Competições
* Você cadastra o nome da prova, o local, a categoria e a data do evento.
* Quando puxar a lista de competições, o programa calcula os dias em tempo real e avisa: 
    * `[Faltam X dias para a prova!]`
    * `[É hoje!]`
    * `[Essa competição já passou.]`
* *Os dados ficam salvos em `Competicoes.txt`.*

### 4. Histórico de Peso e Bioimpedância
* Dá para cadastrar o peso total, massa muscular e gordura informando a data.
* A tabela organiza tudo por ordem de data e usa os símbolos `(+)` para ganho de massa/peso e `(-)` para perda de massa/peso em comparação com o exame anterior.

---

## Arquivos

O sistema funciona com arquivos de texto locais que servem para guardar as informações de forma simples (eles são criados e atualizados sozinhos na mesma pasta do código):
* `Treinos.txt` (Histórico de treinos gerais)
* `Exercicios.txt` (Tempos e marcas dos exercícios específicos)
* `Competicoes.txt` (Calendário de eventos)
* `pesos.txt` (Dados de evolução da balança e bioimpedância)

---

## Como executar o projeto

1. Instale o Python no seu computador.
2. Certifique-se de que o arquivo `agente.py` (com a função do chat de IA) está na mesma pasta que o script principal.
3. Abra o terminal e comece a cadastrar seus exercícios!
