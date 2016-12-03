import utils
from pprint import pprint

print('PURCHASE DATA UGLY ANALYSIS')
# analyze purchase data
purchases, products = utils.get_purchases_products()
interesting_purchases = utils.get_only_lists([purchases[purchase] for purchase in purchases])

print('[>] Analyzing candidate sets. \t (this might some time)')
pprint(sorted(set((cand, utils.support(cand, interesting_purchases ), utils.get_lift_confidence(cand, interesting_purchases)) for cand in utils.generate_candidates(interesting_purchases)), key=lambda x:x[2][0]))



# analyze event attendance
import networkx as nx
import matplotlib.pyplot as plt

print('EVENT ATTENDANCE DATA UGLY ANALYSIS')
# make graph
print('[>] Creating graph...')
G = nx.Graph()
for edge in utils.get_edge():
    G.add_edges_from(utils.get_edge(limit_files=5, rule=lambda stat: stat == 'maybe' or stat == 'going'))
# analyze degrees
degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
#print "Degree sequence", degree_sequence
dmax=max(degree_sequence)

plt.loglog(degree_sequence,'b-',marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")

print('[>] Drawing graph... \t [!] Now this will take a looooot of time :)')
plt.axes([0.45,0.45,0.45,0.45])
Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
pos=nx.spring_layout(Gcc)
plt.axis('off')
nx.draw_networkx_nodes(Gcc,pos,node_size=20)
nx.draw_networkx_edges(Gcc,pos,alpha=0.4)
# save drawing
plt.savefig("degree_histogram.png")
plt.show()

# # Uncomment this part if interested in seeing the assortativity or the centralities
# r=nx.degree_assortativity_coefficient(G)
# print("%3.1f"%r)
# centralities = nx.degree_centrality(G)
# ordered_people = sorted([(n, centralities[n]) for n in centralities], key=lambda x: x[1])
# bcentralities = nx.betweenness_centrality(G)
# important_people = sorted([(n, bcentralities[n]) for n in centralities], key=lambda x: x[1])
# pprint(important_people)
