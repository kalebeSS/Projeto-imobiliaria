import pandas as pd
import numpy as np

def generate_data(n_samples=100):
    np.random.seed(42)
    bedrooms = np.random.randint(1, 5, n_samples)
    bathrooms = np.random.randint(1, 4, n_samples)
    square_meters = np.random.randint(50, 300, n_samples)
    price = 100 * bedrooms + 50 * bathrooms + square_meters + np.random.normal(0, 1000, n_samples)

    data = pd.DataFrame({
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'square_meters': square_meters,
        'price': price
    })

    data.to_csv('data/imoveis.csv', index=False)

generate_data()