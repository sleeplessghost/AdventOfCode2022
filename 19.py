from collections import defaultdict, deque, namedtuple
import math

State = namedtuple('State', ['production', 'resources', 'time'])

def parseLine(line):
    parsed = [parsePart(part) for part in ' '.join(line.split()[2:]).split('.')]
    return {robot: costs for robot,costs in parsed}

def parsePart(part):
    bits = part.split()
    robot_type = bits[1]
    cost_dict = defaultdict(int)
    costs = ' '.join(bits[4:]).split(' and ')
    for cost in costs:
        value, resource = cost.split()
        cost_dict[resource] = int(value)
    return robot_type, cost_dict

def getNextStates(state, blueprint, resource_limits, time_limit):
    if state.time >= time_limit - 1: return
    producing = [res for res in state.production if state.production[res] > 0]
    for robot, cost_dict in blueprint.items():
        if robot in resource_limits and state.production[robot] >= resource_limits[robot]: continue
        if any(cost > 0 and res not in producing for res,cost in cost_dict.items()): continue
        time_to_wait = 0
        for resource in cost_dict:
            required = cost_dict[resource]
            owned = state.resources[resource]
            per_min = state.production[resource]
            if required > owned:
                wait = math.ceil((required - owned) / per_min)
                time_to_wait = max(time_to_wait, wait)
        time_to_wait += 1
        new_production = state.production.copy()
        new_resources = state.resources.copy()
        for resource in producing: new_resources[resource] += time_to_wait * state.production[resource]
        for resource in cost_dict: new_resources[resource] -= cost_dict[resource] 
        new_production[robot] += 1
        yield State(new_production, new_resources, state.time + time_to_wait)

def produce(blueprint, limit):
    resource_limits = {r: max(costs[r] for costs in blueprint.values()) for r in ['ore', 'clay', 'obsidian']}
    initial = State(defaultdict(int, {'ore': 1}), defaultdict(int), 0)
    q = deque([initial])
    while q:
        state = q.popleft()
        next_states = [s for s in getNextStates(state, blueprint, resource_limits, limit) if s.time <= limit]
        for s in next_states: q.append(s)
        if not any(next_states):
            time_remaining = limit - state.time
            yield state.resources['geode'] + time_remaining * state.production['geode']

blueprints = [parseLine(line[:-1]) for line in open('in/19.txt').read().splitlines()]
best_geodes = []
for i in range(len(blueprints)):
    print(i, '/', len(blueprints))
    best_geodes.append(max(produce(blueprints[i], 24)))
print('part1:', sum((i+1) * geodes for i,geodes in enumerate(best_geodes)))

best_geodes = []
for i in range(len(blueprints[:3])):
    print(i, '/', len(blueprints[:3]))
    best_geodes.append(max(produce(blueprints[i], 32)))
print('part2:', math.prod(best_geodes))