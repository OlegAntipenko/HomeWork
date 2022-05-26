class ReverseIter():
    def __init__(self, *args):
        self.li = list(args)

    def reiter(self):
        new_list = []
        for i in self.li[::-1]:
            new_list.append(i)
        return new_list

r = ReverseIter(2, 'hfhf', 7)
print(r.reiter())
