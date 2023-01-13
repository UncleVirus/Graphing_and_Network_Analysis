# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:24:04 2022

@author: grivi
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from(["A","B","C","D","E","F","G","H","I","J","K"])
G.add_edges_from([("A","C"),("B","C"),("C","D"),("D","E"),
("D","G"),("A","G"),("F","H"),("G","H"),("H","I"),
("I","J"),("I","K")])
nx.draw(G, node_size=400, node_color='red', with_labels=True, font_weight='bold')
print("degree centrality:")
for k, v in sorted(nx.degree_centrality(G).items(), key=lambda x: -x[1]):
      print(str(k)+":"+"{:.3}".format(v)+" ", end="")
print("\n")
print("eigenvector centrality:")
for k, v in sorted(nx.eigenvector_centrality(G).items(), key=lambda x: -x[1]):
      print(str(k)+":"+"{:.3}".format(v)+" ", end="")
print("\n")
print("between centrality:")
for k, v in sorted(nx.betweenness_centrality(G).items(), key=lambda x: -x[1]):
      print(str(k)+":"+"{:.3}".format(v)+" ", end="")
print("\n")
print("closeness centrality:")
for k, v in sorted(nx.closeness_centrality(G).items(), key=lambda x: -x[1]):
      print(str(k)+":"+"{:.3}".format(v)+" ", end="")
print("\n")