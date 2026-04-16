import pandas as pd

# Não importe nada do data_cleaning aqui. 
# A função deve ser independente e receber os dados pelo parâmetro 'df'.

def analyze_data(df):
    # Estatísticas básicas
    stats = df.describe()
    
    # Adicione o cálculo da matriz de correlação para retornar os dois valores
    correlation_matrix = df.corr(numeric_only=True) 
    
    return stats, correlation_matrix