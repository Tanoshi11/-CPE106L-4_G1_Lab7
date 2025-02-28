import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(filename):

    df = pd.read_csv(filename)
    
    df = df.dropna()
    
    df['Average Price'] = df.iloc[:, 1:].mean(axis=1)
    df = df[['Year', 'Average Price']]
    df['Year'] = df['Year'].astype(int)
    
    return df

def plot_bread_prices(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Year'], df['Average Price'], marker='o', linestyle='-')
    plt.xlabel('Year')
    plt.ylabel('Average Price of Bread (USD)')
    plt.title('Average Price of Bread Over the Years')
    plt.grid(True)
    plt.show()

def main():
    filename = 'breadprice.csv'  
    df = load_and_clean_data(filename)
    plot_bread_prices(df)

if __name__ == "__main__":
    main()
