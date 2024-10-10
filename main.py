import pandas as pd

# Carregar o dataset
data = pd.read_csv('archive/transporte.csv')  # Substitua pelo nome do seu arquivo

# Exibir as primeiras linhas do dataframe
print(data.head())

# Verificar informações gerais sobre o dataset
print(data.info())

# Exibir estatísticas descritivas
print(data.describe())

# Exibir colunas do dataset
print(data.columns)

# Verificar dados ausentes
missing_data = data.isnull().sum()
print("Dados ausentes por coluna:")
print(missing_data[missing_data > 0])  # Exibe apenas colunas com dados ausentes

# Verificar tipos de dados
print("Tipos de dados:")
print(data.dtypes)

missing_data = data.isnull().sum()
print("Dados ausentes por coluna:")
print(missing_data) 

# Remover linhas com dados ausentes (opcional, dependendo do contexto)
data_cleaned = data.dropna()

data_cleaned = data_cleaned.drop_duplicates()

# Verificar valores únicos na coluna NumberOfBoardings
print("Valores únicos na coluna 'NumberOfBoardings':")
print(data_cleaned['NumberOfBoardings'].unique())

data_cleaned = data_cleaned[data_cleaned['NumberOfBoardings'] >= 0]

missing_data_after_cleaning = data_cleaned.isnull().sum()
print("Dados ausentes por coluna após limpeza:")
print(missing_data_after_cleaning[missing_data_after_cleaning > 0]) 

data_cleaned.to_csv('dados_transporte_limpos.csv', index=False)

# Análise de embarques por rota
embarcacoes_por_rota = data_cleaned.groupby('RouteID')['NumberOfBoardings'].sum().sort_values(ascending=False)
print("Total de embarques por rota:")
print(embarcacoes_por_rota)

# Agrupar por semana
embarcacoes_por_semana = data_cleaned.groupby('WeekBeginning')['NumberOfBoardings'].sum().sort_values(ascending=False)
print("Total de embarques por semana:")
print(embarcacoes_por_semana)


import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de total de embarques por rota
plt.figure(figsize=(12, 6))
sns.barplot(x=embarcacoes_por_rota.index, y=embarcacoes_por_rota.values)
plt.title('Total de Embarques por Rota')
plt.xlabel('Route ID')
plt.ylabel('Total de Embarques')
plt.xticks(rotation=45)
plt.show()


# Histogramas para visualizar a distribuição do número de embarques
plt.figure(figsize=(10, 5))
sns.histplot(data_cleaned['NumberOfBoardings'], bins=30, kde=True)
plt.title('Distribuição do Número de Embarques')
plt.xlabel('Número de Embarques')
plt.ylabel('Frequência')
plt.grid()
plt.show()

import folium

# Criar um mapa base
mapa = folium.Map(location=[latitude_media, longitude_media], zoom_start=12)  # Defina os valores médios de latitude e longitude

# Adicionar marcadores para cada parada
for idx, row in data_cleaned.iterrows():
    folium.CircleMarker(
        location=(row['Latitude'], row['Longitude']),  # Supondo que você tenha essas colunas
        radius=row['NumberOfBoardings'] / 100,  # Ajuste o raio conforme necessário
        color='blue',
        fill=True,
        fill_opacity=0.5,
        popup=f"Stop: {row['StopName']}<br>Embarques: {row['NumberOfBoardings']}"
    ).add_to(mapa)

# Salvar o mapa em um arquivo HTML
mapa.save('mapa_embarques.html')


from geopy.geocoders import Nominatim
import time

import requests


def geocode(address):
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1"
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Levanta um erro para códigos de status 4xx e 5xx
            return response.json()
        except requests.exceptions.HTTPError as err:
            if response.status_code == 503:
                print(f"Service unavailable, retrying... {attempt + 1}/{max_retries}")
                time.sleep(2 ** attempt)  # Exponencial backoff
            else:
                print(f"HTTP error: {err}")
                break
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break
    return None

address = "181 Cross Rd"
result = geocode(address)
if result:
    print(result)
else:
    print("Geocoding failed.")



# Agrupar por RouteID e somar o número de embarques
route_boardings = data.groupby('RouteID')['NumberOfBoardings'].sum().reset_index()

# Ordenar as rotas pela quantidade de embarques
route_boardings = route_boardings.sort_values(by='NumberOfBoardings', ascending=False)

# Exibir as rotas com mais embarques
print(route_boardings.head())


import matplotlib.pyplot as plt
import seaborn as sns

# Definir o estilo dos gráficos
sns.set(style="whitegrid")

# Criar um gráfico de barras para mostrar as rotas mais populares
plt.figure(figsize=(10, 6))
sns.barplot(x='RouteID', y='NumberOfBoardings', data=route_boardings.head(10), palette='Blues_d')

# Adicionar títulos e labels
plt.title('Top 10 Rotas com Mais Embarques', fontsize=16)
plt.xlabel('RouteID', fontsize=12)
plt.ylabel('Número de Embarques', fontsize=12)

# Exibir o gráfico
plt.show()



