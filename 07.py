
class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.subdirs = []
        self.files = []

class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

def mkdir(dir, name):
    sub = next((d for d in dir.subdirs if d.name == name), None)
    if sub == None:
        sub = Dir(dir, name)
        dir.subdirs.append(sub)
    return sub

def mkfile(dir, size, name):
    file = next((f for f in dir.files if f.name == name), None)
    if file == None:
        file = File(int(size), name)
        dir.files.append(file)
    return file

def lsdir(dir, lines, i):
    x = i+1
    part = lines[x].split(' ')
    while x < len(lines) and (part := lines[x].split(' '))[0] != '$':
        if part[0] == 'dir': mkdir(dir, part[1])
        else: mkfile(dir, part[0], part[1])
        x += 1
    return x

def dirsize(dir):
    return sum(f.size for f in dir.files) + sum(dirsize(d) for d in dir.subdirs)

def checkdir(dir, list, size):
    #flip for part1
    if dirsize(dir) >= size:
        list.append(dir)
    for d in dir.subdirs:
        checkdir(d, list, size)

lines = [line.strip() for line in open('in/07.txt')]

root = Dir(None, 'root')
current = root
i = 0
while i < len(lines):
    parts = lines[i].split(' ')
    if parts[0] == '$':
        if parts[1] == 'cd':
            if parts[2] == '/': current = root
            elif parts[2] == '..': current = current.parent
            else: current = mkdir(current, parts[2])
            i += 1
        elif parts[1] == 'ls':
            i = lsdir(current, lines, i)
            
resu = []
checkdir(root, resu, 100000)

print('part1:', sum(dirsize(d) for d in resu))

rtsize = dirsize(root)
freespace = 70000000 - rtsize
requiredremove = 30000000 - freespace

resu2 = []
checkdir(root, resu2, requiredremove)
totals = [dirsize(d) for d in resu2]


print('part2:', min(totals))