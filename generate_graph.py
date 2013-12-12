import json
from get_country_code import get_cc, get_continent
import networkx as nx

input_file = "24h_5k_users_followers_countries"
output_file = "graph_full"

total_entries = 0
with_country = 0

g = nx.DiGraph()

def increment_edge(n1, n2):
    if n1 == n2:
        return
    increment_node(n1)
    make_node(n2)
    if not g.has_edge(n1, n2):
        g.add_edge(n1, n2)

    if 'weight' in g.edge[n1][n2]:
        g.edge[n1][n2]['weight'] += 1
    else:
        g.edge[n1][n2]['weight'] = 1

def increment_node(name):
    make_node(name)
    if 'weight' in g.node[name]:
        g.node[name]['weight'] += 1
    else:
        g.node[name]['weight'] = 1


def make_node(name):
    if not g.has_node(name):
        g.add_node(name)
    if not 'continent' in g.node[name] and name != None:
        g.node[name]['continent'] = get_continent(name)


for line in open("processed/"+input_file+".json"):
    user = json.loads(line)

    user_c = user['country']

    for follower in user['followers']:
        follower_c = follower['country']
        increment_edge(user_c, follower_c)

nx.write_gexf(g, "graphs/"+output_file+".gexf")