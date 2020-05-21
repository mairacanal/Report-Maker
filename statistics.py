import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_data_x_time (data, time, dataType):

    if pd.Series(data).is_unique == True:
        return -1                            # Maybe return a constant when the content in database is constant

    else:
    
        df = pd.DataFrame(list(zip(data, time)), columns= [f'{dataType}', 'Time'])
        
        # Set a graph design
        plt.style.use(u'seaborn-pastel')

        # Create graph
        plt.plot(df['Time'], df[f'{dataType}'], marker='', color='blue', linewidth=1, alpha=0.7)

        # Add titles
        plt.title(f"{dataType} x Time", loc='left', fontsize=12, fontweight=0, color='black')
        plt.xlabel("Time")
        plt.ylabel(f"{dataType}")

        # Save graph
        plt.savefig(f'graph_{dataType}.png', dpi=96, bbox_inches='tight')
        return 1

def generate_compare_graph (data1, data2, data3, time, dataType1, dataType2, dataType3, comparing_data):

    df = pd.DataFrame(list(zip(data1, data2, data3, time)), columns= [f'{dataType1}', f'{dataType2}', f'{dataType3}', 'Time'])

    # Set a graph design
    plt.style.use(u'seaborn-pastel')

    # Create graph
    plt.plot(df['Time'], df[f'{dataType1}'], marker='', color='red', linewidth=1.5, alpha=0.7, label= f'{dataType1}')
    plt.plot(df['Time'], df[f'{dataType2}'], marker='', color='blue', linewidth=1.5, alpha=0.7, label= f'{dataType2}')
    plt.plot(df['Time'], df[f'{dataType3}'], marker='', color='green', linewidth=1.5, alpha=0.7, label= f'{dataType3}')

    # Add legend (Acertar)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Add titles
    plt.title(f"Comparing {comparing_data}", loc='left', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Time (s)")                              # Podemos entrar como parâmetro as unidades de medida
    plt.ylabel(f"{comparing_data}")

    # Save graph
    plt.savefig(f'graph_compare_{comparing_data}.png', dpi=96, bbox_inches='tight')
