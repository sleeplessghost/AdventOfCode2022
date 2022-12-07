
class Folder:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.folders = []
        self.files = []
        self.cachedSize = None

    def size(self):
        if self.cachedSize == None:
            self.cachedSize = sum(d.size() for d in self.folders) + sum(f.size for f in self.files)
        return self.cachedSize

    def search(self, searchFunction):
        searchResults = []
        if searchFunction(self): searchResults.append(self)
        for folder in self.folders:
            matches = folder.search(searchFunction)
            searchResults.extend(matches)
        return searchResults

class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

def parseLines(root, lines):
    current = root
    for line in lines:
        match line.split():
            case '$', 'cd', '/': current = root
            case '$', 'cd', '..': current = current.parent
            case '$', 'cd', name: current = mkdir(current, name)
            case '$', 'ls': continue
            case 'dir', name: mkdir(current, name)
            case size, name: mkfile(current, size, name)

def mkdir(dir, name):
    sub = next((d for d in dir.folders if d.name == name), None)
    if sub == None:
        sub = Folder(dir, name)
        dir.folders.append(sub)
    return sub

def mkfile(dir, size, name):
    file = next((f for f in dir.files if f.name == name), None)
    if file == None:
        file = File(int(size), name)
        dir.files.append(file)
    return file

root = Folder(None, 'root')
lines = [line.strip() for line in open('in/07.txt')]
parseLines(root, lines)
space_to_clear = 30_000_000 - 70_000_000 + root.size()

print('part1:', sum(d.size() for d in root.search(lambda dir: dir.size() <= 100_000)))
print('part2:', min(d.size() for d in root.search(lambda dir: dir.size() >= space_to_clear)))