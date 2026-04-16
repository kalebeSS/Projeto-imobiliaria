import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Verificar valores nulos
    if df.isnull().sum().any():
        raise ValueError("Existem valores nulos no dataset.")

    return df

cleaned_df = clean_data('data/imoveis.csv')