
class Folder:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.folders = []
        self.files = []
        self.cachedSize = None

    def mkdir(self, name):
        self.folders.append((folder := Folder(self, name)))
        return folder

    def mkfile(self, size, name):
        self.files.append((file := File(size, name)))
        return file

    def size(self):
        if self.cachedSize == None:
            self.cachedSize = sum(d.size() for d in self.folders) + sum(f.size for f in self.files)
        return self.cachedSize

    def search(self, searchFunction):
        if searchFunction(self): yield self
        yield from (match for f in self.folders for match in f.search(searchFunction))

class File:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name

def parseLines(root, lines):
    current: Folder = root
    for line in lines:
        match line.split():
            case '$', 'cd', '/': current = root
            case '$', 'cd', '..': current = current.parent
            case '$', 'cd', name: current = next(d for d in current.folders if d.name == name)
            case '$', 'ls': continue
            case 'dir', name: current.mkdir(name)
            case size, name: current.mkfile(size, name)

root = Folder(None, 'root')
lines = [line.strip() for line in open('in/07.txt')]
parseLines(root, lines)
space_to_clear = 30_000_000 - 70_000_000 + root.size()

print('part1:', sum(d.size() for d in root.search(lambda dir: dir.size() <= 100_000)))
print('part2:', min(d.size() for d in root.search(lambda dir: dir.size() >= space_to_clear)))