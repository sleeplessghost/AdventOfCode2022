from collections import deque, namedtuple

State = namedtuple('State', ['valve', 'time', 'rate', 'total', 'visited'])

def parse(line):
    x = line.replace(',','').replace(';','').replace('rate=','').split()
    valve = x[1]
    flow = int(x[4])
    tunnels = x[9:]
    return (valve, flow, tunnels)

def distsearch(lookup):
    distances = dict()
    for node in lookup.keys():
        dist_map = distances[node] = dict()
        q = deque([(node, 0)])
        while q:
            current, distance = q.popleft()
            _, tunnels = lookup[current]
            for node in (t for t in tunnels if t not in dist_map.keys()):
                dist_map[node] = distance + 1
                q.append((node, distance + 1))
    return distances

def canPath(location, time, visited, target, distances, limit):
    return target not in visited and limit - time >= distances[location][target] + 1

def value(state, limit):
    return (limit - state.time) * state.rate + state.total

def getNextState(state, node, distances, lookup):
    distance = distances[state.valve][node] + 1
    total = distance * state.rate + state.total
    flow,_ = lookup[node]
    return State(node, state.time + distance, state.rate + flow, total, {*state.visited, node})
    
def nodesearch(lookup, distances, value_nodes):
    q = deque([State('AA', 0, 0, 0, {'AA'})])
    while q:
        state = q.popleft()
        possible_nodes = [node for node in value_nodes if canPath(state.valve, state.time, state.visited, node, distances, 30)]
        if not any(possible_nodes):
            yield value(state, 30)
        else:
            for node in possible_nodes: q.append(getNextState(state, node, distances, lookup))

def elesearch(lookup, distances, value_nodes):
    q = deque([(State('AA', 0, 0, 0, {'AA'}), State('AA', 0, 0, 0, {'AA'}))])
    maxValue = 0
    while q:
        mine, elephant = q.popleft()
        visited = {*mine.visited, *elephant.visited}
        my_nodes = [node for node in value_nodes if canPath(mine.valve, mine.time, visited, node, distances, 26)]
        ele_nodes = [node for node in value_nodes if canPath(elephant.valve, elephant.time, visited, node, distances, 26)]
        testval = (value(mine, 26) / (mine.time+1)) + (value(elephant, 26) / (elephant.time+1))
        maxValue = max(maxValue, testval)
        if testval < maxValue // 1.7: continue
        if not any((*my_nodes, *ele_nodes)):
            yield value(mine, 26) + value(elephant, 26)
        else:
            for my_node in my_nodes:
                my_next = getNextState(mine, my_node, distances, lookup)
                if not any(ele_nodes):
                    q.append((my_next, elephant))
                for ele_node in (e for e in ele_nodes if e != my_node):
                    q.append((my_next, getNextState(elephant, ele_node, distances, lookup)))
            if not any(my_nodes):
                for ele_node in ele_nodes:
                    q.append((mine, getNextState(elephant, ele_node, distances, lookup)))

valves = [parse(line.strip()) for line in open('in/16.txt')]
lookup = {valve: (flow, tunnels) for valve, flow, tunnels in valves}
value_nodes = [valve for (valve,flow,tunnels) in valves if flow > 0]
distances = distsearch(lookup)

print('part1:', max(r for r in nodesearch(lookup, distances, value_nodes)))
print('part2:', max(r for r in elesearch(lookup, distances, value_nodes)))