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

def getNextStates(state, blueprint, resource_limits, time_limit, resource_lookup):
    if state.time >= time_limit - 1: return
    for robot, cost_dict in blueprint.items():
        index = resource_lookup[robot]
        if robot in resource_limits and state.production[index] >= resource_limits[robot]: continue
        if any(cost > 0 and state.production[resource_lookup[res]] == 0 for res,cost in cost_dict.items()): continue
        time_to_wait = 0
        for resource,cost in cost_dict.items():
            if cost == 0: continue
            index = resource_lookup[resource]
            owned = state.resources[index]
            per_min = state.production[index]
            if cost > owned:
                wait = math.ceil((cost - owned) / per_min)
                time_to_wait = max(time_to_wait, wait)
        time_to_wait += 1
        new_resources = tuple(state.resources[i] + (time_to_wait * state.production[i]) - cost_dict[r] for r,i in resource_lookup.items())
        new_production = tuple(state.production[i] + (r == robot) for r,i in resource_lookup.items())
        yield State(new_production, new_resources, state.time + time_to_wait)

def produce(blueprint, limit):
    resource_lookup = {r:i for i,r in enumerate(['ore', 'clay', 'obsidian', 'geode'])}
    resource_limits = {r: max(costs[r] for costs in blueprint.values()) for r in ['ore', 'clay', 'obsidian']}
    initial = State((1,0,0,0), (0,0,0,0), 0)
    q = deque([initial])
    visited = set()
    best_geodes_time = defaultdict(int)
    while q:
        state = q.popleft()
        next_states = [s for s in getNextStates(state, blueprint, resource_limits, limit, resource_lookup) if s.time <= limit]
        for s in next_states:
            if s not in visited:
                visited.add(s)
                if s.resources[-1] >= best_geodes_time[s.time] - 1:
                    best_geodes_time[s.time] = max(s.resources[-1], best_geodes_time[s.time])
                    q.append(s)
        if not any(next_states):
            time_remaining = limit - state.time
            yield state.resources[-1] + time_remaining * state.production[-1]

blueprints = [parseLine(line[:-1]) for line in open('in/19.txt').read().splitlines()]
best_geodes = (max(produce(blueprint, 24)) for blueprint in blueprints)
print('part1:', sum((i+1) * geodes for i,geodes in enumerate(best_geodes)))

best_geodes = (max(produce(blueprint, 32)) for blueprint in blueprints[:3])
print('part2:', math.prod(best_geodes))