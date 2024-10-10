import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título do dashboard
st.title('Dashboard de Análise de Dados de Transporte Público')

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('dados_transporte_limpos.csv')
    return data

data = load_data()

# Exibir os dados carregados
st.write("Visualizando os dados brutos:")
st.dataframe(data.head())

# Agrupar dados por RouteID
route_boardings = data.groupby('RouteID')['NumberOfBoardings'].sum().reset_index()

# Gráfico de barras interativo
st.write("Número total de embarques por rota")
fig, ax = plt.subplots()
sns.barplot(x='RouteID', y='NumberOfBoardings', data=route_boardings.sort_values(by='NumberOfBoardings', ascending=False).head(10), ax=ax)
ax.set_title('Top 10 Rotas com Mais Embarques')
st.pyplot(fig)


# Converter a coluna de datas para formato datetime
data['WeekBeginning'] = pd.to_datetime(data['WeekBeginning'])

# Filtro de datas
st.write("Filtrar dados por período:")
start_date = st.date_input('Data de início', data['WeekBeginning'].min())
end_date = st.date_input('Data de fim', data['WeekBeginning'].max())

# Filtrar o DataFrame com base no intervalo de datas
filtered_data = data[(data['WeekBeginning'] >= pd.to_datetime(start_date)) & (data['WeekBeginning'] <= pd.to_datetime(end_date))]

# Exibir o DataFrame filtrado
st.write("Dados filtrados por período:")
st.dataframe(filtered_data.head())


# Dropdown para selecionar uma rota
route_id = st.selectbox('Selecione uma rota para detalhamento:', route_boardings['RouteID'].unique())

# Filtrar os dados pela rota selecionada
route_data = data[data['RouteID'] == route_id]

# Exibir dados da rota selecionada
st.write(f'Detalhes da rota {route_id}:')
st.dataframe(route_data)

import matplotlib.dates as mdates

# Exibir gráfico de embarques ao longo do tempo para a rota selecionada
st.write(f'Número de embarques ao longo do tempo para a rota {route_id}:')

# Criar o gráfico
fig, ax = plt.subplots(figsize=(12, 6))  # Aumentar o tamanho da figura
sns.lineplot(x='WeekBeginning', y='NumberOfBoardings', data=route_data, ax=ax)

# Definir o título e os rótulos dos eixos
ax.set_title(f'Embarques ao longo do tempo - Rota {route_id}')
ax.set_xlabel('Data')
ax.set_ylabel('Número de Embarques')

# Melhorar a exibição das datas no eixo X
ax.xaxis.set_major_locator(mdates.MonthLocator())  # Mostrar as datas por mês
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Formato mês/ano

# Rotacionar os rótulos do eixo X
plt.xticks(rotation=45, ha='right')

plt.tight_layout()  # Ajustar automaticamente os espaçamentos
st.pyplot(fig)







