#!python

import re
import sys

import matplotlib.pyplot as plt
import networkx as nx

toplevel = re.compile(r'(.*?) contain (.*)')

# Ok, so what we're going to try here is a tree structure. I think the 
# structure should look like this:
#   light_red --> bright_white, muted_yellow
#   dark_orange --> bright_white, muted_yellow
#   bright_white --> shiny_gold
# etc.
#     LR 
#    /  \
#   BW   MY
#   |
#   SG
#
# I think the algorithm here is to find all the nodes in the graph 
# that are dominators of the Shiny Gold node. To do this, we'll 
# flip the edges around and find all of the nodes that are reachable
# from SG

bag_graph = nx.DiGraph()
holding_graph = nx.DiGraph()

for line in open(sys.argv[1], 'r').readlines():
    rule_str = line.strip()
    res = toplevel.match(rule_str)
    if res is None:
        print(f'Bad line? {rule_str}')
        break
    lhs = ' '.join(res.group(1).split(' ')[:-1])
    rest = res.group(2)
    
    rhs = [" ".join(x.strip().split(' ')[:-1]) for x in rest.split(',')]
    #print(lhs, rhs)

    if not lhs in bag_graph.nodes():
        bag_graph.add_node(lhs, )

    for r in rhs:
        if r == 'no other':
            continue
        node = ' '.join(r.split(' ')[1:])
        weight = int(r.split(' ')[0])
        bag_graph.add_edge(node, lhs)
        holding_graph.add_edge(lhs, node, weight=weight)

reachable_colors = set([])
for node in bag_graph.nodes():
    if node == 'shiny gold':
        continue
    if nx.algorithms.shortest_paths.generic.has_path(bag_graph, 'shiny gold', node):
        reachable_colors.add(node)

print(f'There are {len(reachable_colors)} reachable colors:')
print(f'{sorted(reachable_colors)}')

# Part 2

def whats_inside(G, current):
    # Base case
    if holding_graph.out_degree(current) == 0:
        return 1
    else:
        # Recursion
        sum = 1
        for child in G.neighbors(current):
            weight = G.get_edge_data(current, child)['weight']
            #print(current, weight, child)
            sum += weight * whats_inside(G, child)
        return sum

bag_count = whats_inside(holding_graph, 'shiny gold')
bag_count -= 1  # don't add one for shiny_gold in the root
print(f'Shiny Gold has to hold {bag_count} bags!')

# If you want to print it, uncomment these lines. NX kinda sucks at graph layout
# though, unless you get really fancy with the arguments.
#pos = nx.spring_layout(bag_graph, k=1)
#pos = nx.circular_layout(holding_graph)
#nx.draw_networkx(holding_graph, pos)
#nx.draw_networkx_edge_labels(bag_graph, pos, edge_labels=nx.get_edge_attributes(holding_graph, 'weight'))
#plt.show()