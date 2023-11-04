import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(df, x_column, y_columns, graph_type):
    if graph_type == 'bar':
        df.plot(x=x_column, y=y_columns, kind='bar')
    elif graph_type == 'line':
        df.plot(x=x_column, y=y_columns, kind='line')
    elif graph_type == 'scatter':
        df.plot(x=x_column, y=y_columns, kind='scatter')
    elif graph_type == 'pie' and len(y_columns) == 1:
        df.plot.pie(y=y_columns[0], labels=df[x_column])
    else:
        print("Invalid graph type or data format.")
        return

    plt.title(f"{graph_type} plot")
    plt.xlabel(x_column)
    plt.ylabel(", ".join(y_columns))
    plt.show()

if __name__ == '__main__':
    data = {
        '1': [1, 2, 3, 4, 5],
        '2': [10, 20, 15, 30, 25],
        '3': [5, 15, 10, 20, 30],
    }

    df = pd.DataFrame(data)

    print("Available graph types: bar, line, scatter, pie")
    graph_type = input("Enter the graph type: ")
    x_column = input("Enter the X-axis column: ")
    y_columns = input("Enter the Y-axis column(s), separated by comma: ").split(",")
    
    for i in y_columns:
        plot_graph(df, x_column, i, graph_type)
