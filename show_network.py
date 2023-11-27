import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('distance_matrix.csv', index_col=0)
graph = nx.from_pandas_adjacency(df)
col = list(df.columns)
mapping = {i: '_'.join(col[i].split('_')[:3]) for i in range(len(col))}
graph = nx.relabel_nodes(graph, mapping)
plot = nx.draw_networkx(graph, with_labels=True, )
plt.savefig('graph.png')