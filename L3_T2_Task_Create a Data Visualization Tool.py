import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(data_file):
    try:
        df = pd.read_csv(data_file)

        x = df['x']
        y = df['y']

        plt.scatter(x, y)
        plt.title('Scatter Plot')
        plt.xlabel('X-axis Label')
        plt.ylabel('Y-axis Label')

        plt.show()

    except FileNotFoundError:
        print(f'Error: File "{data_file}" not found.')

visualize_data('your_dataset.csv')