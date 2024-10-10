# README - Análise de Dados de Transporte Público

## Introdução

Olá! Neste projeto, realizei uma análise de dados de transporte público com o objetivo de otimizar rotas e horários, analisando o fluxo de passageiros. Utilizei ferramentas como **Pandas**, **GeoPandas**, **Folium**, **Seaborn** e **Streamlit** para manipular e visualizar os dados de maneira eficaz. O intuito é fornecer insights que podem ajudar na melhoria do sistema de transporte público.

## Objetivos do Projeto

Os principais objetivos deste projeto foram:

- **Exploração de Dados**: Entender a estrutura dos dados e as características dos passageiros.
- **Identificação de Padrões de Mobilidade**: Descobrir como os passageiros utilizam o transporte público ao longo do tempo e por diferentes rotas.
- **Otimização de Rotas**: Propor melhorias nas rotas e horários com base na análise do fluxo de passageiros.

## Conjunto de Dados

Utilizei um conjunto de dados disponível no Kaggle, que contém informações sobre as viagens de transporte público. As principais colunas do dataset são:

| Coluna               | Descrição                                               |
|----------------------|---------------------------------------------------------|
| **TripID**           | Identificador único da viagem.                          |
| **RouteID**          | Identificador da rota utilizada na viagem.             |
| **StopID**           | Identificador da parada de ônibus.                     |
| **StopName**         | Nome da parada de ônibus.                              |
| **WeekBeginning**    | Data do início da semana correspondente à viagem.     |
| **NumberOfBoardings**| Número de embarques registrados na parada.            |

## Metodologia

1. **Análise dos Dados**: 
   - Inicialmente, fiz uma análise exploratória para entender a estrutura do conjunto de dados. 
   - Identifiquei valores ausentes, duplicatas e inconsistências.

2. **Limpeza dos Dados**: 
   - Removi entradas duplicadas.
   - Imputei valores ausentes onde necessário.
   - Assegurei que todas as colunas tinham os tipos de dados corretos.

3. **Visualização de Dados**:
   - Criei visualizações interativas para destacar informações relevantes:
     - **Número total de embarques por rota**: Utilizei gráficos de barras para mostrar quais rotas têm o maior número de embarques.
     - **Variação do número de embarques ao longo do tempo**: Utilizei gráficos de linha para mostrar como o número de embarques muda durante a semana.

4. **Filtragem de Dados**:
   - Implementei um filtro que permite ao usuário selecionar um intervalo de datas para analisar os dados.
   - Adicionei um menu dropdown que permite a seleção de rotas específicas para detalhamento adicional.

## Resultados

As análises e visualizações apresentaram insights valiosos, como:

- **Rotas com Maior Fluxo de Passageiros**: Identifiquei as 10 rotas mais utilizadas, o que pode ser útil para direcionar recursos e aumentar a frequência.
- **Tendências ao Longo do Tempo**: As visualizações mostraram picos de demanda em determinados dias da semana, indicando a necessidade de ajustes em horários específicos.

As informações obtidas podem ser utilizadas para propor melhorias na grade de horários e na capacidade das rotas, melhorando a experiência dos passageiros.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para manipulação de dados e criação de visualizações.
- **Pandas**: Biblioteca para análise de dados e manipulação de DataFrames.
- **Seaborn e Matplotlib**: Bibliotecas para visualização de dados, permitindo gráficos informativos e atrativos.
- **Streamlit**: Framework para criar aplicações web interativas, permitindo que outros visualizem e interajam com os dados de maneira simples.

## Como Executar o Projeto

1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
2. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
3. Execute a aplicação Streamlit:

    ````bash
    streamlit run dashboard.py

Abra o navegador e acesse http://localhost:8501 para visualizar o dashboard.

## Conclusão
Este projeto foi uma experiência valiosa na aplicação de análise de dados em um contexto de transporte público. Consegui apresentar insights úteis que podem auxiliar na tomada de decisões para otimizar o sistema de transporte. Acredito que este tipo de análise pode ter um impacto significativo na melhoria da mobilidade urbana e na satisfação dos passageiros.