import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import ward, dendrogram, linkage, single, complete
from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist
data=pd.read_csv("nosacz.csv")
wi =data.iloc[:, 1:11].values
data1=pd.read_csv("example.csv")
wi1 =data1.iloc[:, 1:9].values
data=data.set_index('gat')
del data.index.name
data1=data1.set_index('gat')
del data1.index.name

def augmented_dendrogram(*args, **kwargs):

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        for i, d in zip(ddata['icoord'], ddata['dcoord']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            plt.plot(x, y, 'ro')
            plt.annotate("%.3g" % y, (x, y), xytext=(0, -8),
                         textcoords='offset points',
                         va='top', ha='center')

    return ddata


#Ward's method
wx=ward(wi)
print('------------------------------------------')
print('Macierz odległości: ')
print('------------------------------------------')
print(wi)
print('------------------------------------------')
print('Macierz po wykonaniu klastrowania: ')
print('------------------------------------------')
print(wx)
z=hierarchy.linkage(wx, 'ward')
ddata=augmented_dendrogram(z,color_threshold=5,truncate_mode='lastp')
hierarchy.dendrogram(z, leaf_rotation=90, leaf_font_size=8, labels=data.index, color_threshold=10)
plt.axhline(y=10, c='black', lw=1, linestyle='solid')
plt.title('Metoda Warda')
plt.ylabel('Dystans')
plt.xlabel('Gatunek')
plt.show()

#nearest neighbour method
wx=single(wi)
print('------------------------------------------')
print('Macierz odległości: ')
print('------------------------------------------')
print(wi)
print('------------------------------------------')
print('Macierz po wykonaniu klastrowania: ')
print('------------------------------------------')
print(wx)
z=hierarchy.linkage(wx, 'single')
ddata=augmented_dendrogram(z,color_threshold=5,truncate_mode='lastp')
hierarchy.dendrogram(z, leaf_rotation=90, leaf_font_size=8, labels=data.index, color_threshold=6)
plt.axhline(y=6, c='black', lw=1, linestyle='solid')
plt.title('Metoda Najbliższego Sąsiedztwa')
plt.ylabel('Dystans')
plt.xlabel('Gatunek')
plt.show()

#farthest neighbour method
wx=complete(wi)
print('------------------------------------------')
print('Macierz odległości: ')
print('------------------------------------------')
print(wi)
print('------------------------------------------')
print('Macierz po wykonaniu klastrowania: ')
print('------------------------------------------')
print(wx)
z=hierarchy.linkage(wx, 'complete')
ddata=augmented_dendrogram(z,color_threshold=5,truncate_mode='lastp')
hierarchy.dendrogram(z, leaf_rotation=90, leaf_font_size=8, labels=data.index, color_threshold=10)
plt.axhline(y=10, c='black', lw=1, linestyle='solid')
plt.title('Metoda Najdalszego Sąsiedztwa')
plt.ylabel('Dystans')
plt.xlabel('Gatunek')
plt.show()

#Ward's method
wx=ward(wi1)
print('------------------------------------------')
print('Macierz odległości: ')
print('------------------------------------------')
print(wi1)
print('------------------------------------------')
print('Macierz po wykonaniu klastrowania: ')
print('------------------------------------------')
print(wx)
z=hierarchy.linkage(wx, 'ward')
ddata=augmented_dendrogram(z,color_threshold=5,truncate_mode='lastp')
hierarchy.dendrogram(z, leaf_rotation=90, leaf_font_size=8, labels=data1.index, color_threshold=200)
plt.axhline(y=200, c='black', lw=1, linestyle='solid')
plt.title('Metoda Warda')
plt.ylabel('Dystans')
plt.xlabel('Gatunek')
plt.show()

#nearest neighbour method
wx=single(wi1)
print('------------------------------------------')
print('Macierz odległości: ')
print('------------------------------------------')
print(wi1)
print('------------------------------------------')
print('Macierz po wykonaniu klastrowania: ')
print('------------------------------------------')
print(wx)
z=hierarchy.linkage(wx, 'single')
ddata=augmented_dendrogram(z,color_threshold=5,truncate_mode='lastp')
hierarchy.dendrogram(z, leaf_rotation=90, leaf_font_size=8, labels=data.index, color_threshold=85)
plt.axhline(y=85, c='black', lw=1, linestyle='solid')
plt.title('Metoda Najbliższego Sąsiedztwa')
plt.ylabel('Dystans')
plt.xlabel('Gatunek')
plt.show()

#farthest neighbour method
wx=complete(wi1)
print('------------------------------------------')
print('Macierz odległości: ')
print('------------------------------------------')
print(wi1)
print('------------------------------------------')
print('Macierz po wykonaniu klastrowania: ')
print('------------------------------------------')
print(wx)
z=hierarchy.linkage(wx, 'complete')
ddata=augmented_dendrogram(z,color_threshold=5,truncate_mode='lastp')
hierarchy.dendrogram(z, leaf_rotation=90, leaf_font_size=8, labels=data.index, color_threshold=150)
plt.axhline(y=150, c='black', lw=1, linestyle='solid')
plt.title('Metoda Najdalszego Sąsiedztwa')
plt.ylabel('Dystans')
plt.xlabel('Gatunek')
plt.show()
