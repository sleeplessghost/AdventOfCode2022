from collections import deque

def parseDroplets(lines):
    return set(tuple(map(int, line.split(','))) for line in lines)

def countSides(droplets):
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    return sum((x+dx,y+dy,z+dz) not in droplets for dx,dy,dz in dirs for x,y,z in droplets)

def countEdges(droplets):
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    min_x, max_x = min(x for x,y,z in droplets), max(x for x,y,z in droplets)
    min_y, max_y = min(y for x,y,z in droplets), max(y for x,y,z in droplets)
    min_z, max_z = min(z for x,y,z in droplets), max(z for x,y,z in droplets)
    inside_bounds = lambda x,y,z: min_x-2 <= x <= max_x + 2 and min_y - 2 <= y <= max_y + 2 and min_z - 2 <= z <= max_z + 2
    startPoint = (min_x - 1, min_y - 1, min_z - 1)
    q, outer_edges = deque([startPoint]), set([startPoint])
    while q:
        x,y,z = q.popleft()
        neighbours = [(x+dx,y+dy,z+dz) for dx,dy,dz in dirs]
        for coord in neighbours:
            if inside_bounds(*coord) and coord not in outer_edges and coord not in droplets:
                q.append(coord)
                outer_edges.add(coord)
    return sum((x+dx,y+dy,z+dz) in outer_edges for dx,dy,dz in dirs for x,y,z in droplets)

droplets = parseDroplets(open('in/18.txt').read().splitlines())
print('part1:', countSides(droplets))
print('part2:', countEdges(droplets))