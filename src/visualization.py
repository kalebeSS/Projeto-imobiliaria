import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['price'], bins=30, kde=True)
    plt.title('Distribuição de Preços Imobiliários')
    plt.xlabel('Preço')
    plt.ylabel('Frequência')
    plt.savefig('plots/distribution.png')
    plt.show()

def plot_correlation_matrix(correlation_matrix):
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlação entre Variáveis')
    plt.savefig('plots/correlation_matrix.png')
    plt.show()

plot_distribution(cleaned_df)
plot_correlation_matrix(correlation_matrix)