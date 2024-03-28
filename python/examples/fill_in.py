import collections

Item = collections.namedtuple('Item', ['color', 'size'])

class Box:
    colors = 'black white red blue'.split()
    sizes = [n for n in range(1, 51)]

    def __init__(self):
        self.container = [Item(color, size) for color in self.colors for size in self.sizes]

    def __getitem__(self, position):
        return self.container[position]
    
    # def __setitem__(self, item):
    #     self.container.append(item)


box = Box()