class ReverseIter():
    def __init__(self, *args):
        self.li = list(args)
        self.le = len(self.li)

    def __iter__(self):
        self.coun = self.le - 1
        return self

    def __next__(self):
        if self.coun >= 0:
            self.c = self.li[self.coun]
            x = self.c
            self.coun -= 1
            return x
        else:
            raise StopIteration


r = ReverseIter(2, 'hfhf', 12)
for i in r:
    print(i)
