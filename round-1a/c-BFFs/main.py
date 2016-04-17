import itertools
import sys

T = int(next(sys.stdin))

for t in range(T):
    print('test case #', t)
    group_size = int(next(sys.stdin))
    bff_list = [ int(x) for x in next(sys.stdin).split(' ') ]

    single_cycles = set()
    for i, n in enumerate(bff_list):
        if i + 1 is bff_list[bff_list[i] - 1]:
            single_cycles.add(frozenset([i, n - 1]))

    walks = set()
    for start_index in range(len(bff_list)):
        current_index = start_index
        walk = set()
        while current_index not in walk and walk not in walks:
            walk.add(current_index)
            current_index = bff_list[current_index] - 1
        walks.add(frozenset(walk))

    unique_walks = [ walk for walk in walks if not any([ otherwalk > walk for otherwalk in walks ]) ]

    # cycle_walks = set()
    # for cycle in single_cycles:
        # cycle_walks.add(max([ walk for walk in unique_walks if cycle in walk and walk not in cycle_walks ]))

    print('unique walks', unique_walks)
    print('cycles', single_cycles)
    # print('cycle walks', cycle_walks)
