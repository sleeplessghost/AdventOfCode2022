class Folder:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.folders = []
        self.files = []
        self.cachedSize = None

    def size(self):
        if self.cachedSize == None:
            self.cachedSize = sum(f.size() for f in self.folders) + sum(size for size,name in self.files)
        return self.cachedSize

    def search(self, searchFunction):
        if searchFunction(self): yield self
        yield from (match for f in self.folders for match in f.search(searchFunction))

def parseLines(root, lines):
    current: Folder = root
    for line in lines:
        match line.split():
            case '$', 'cd', '/': current = root
            case '$', 'cd', '..': current = current.parent
            case '$', 'cd', name: current = next(f for f in current.folders if f.name == name)
            case '$', 'ls': continue
            case 'dir', name: current.folders.append(Folder(current, name))
            case size, name: current.files.append((int(size), name))

root = Folder(None, 'root')
parseLines(root, open('in/07.txt').read().splitlines())
space_to_clear = 30_000_000 - (70_000_000 - root.size())
print('part1:', sum(d.size() for d in root.search(lambda dir: dir.size() <= 100_000)))
print('part2:', min(d.size() for d in root.search(lambda dir: dir.size() >= space_to_clear)))