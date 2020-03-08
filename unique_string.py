class Unique():
    def __init__(self, s):
        self.s = s
   
    def unique(self):
        if len(self.s) == 0:
            return False
        d = {}
        for val in self.s:
            d[val] = d.get(val, 0) + 1

        for k, v in d.items():
            if v > 1:
                return False
        return True


i = 'aa'
U = Unique(i)
print(U.unique())
