from collections import defaultdict
import logging

# from collections import defaultdict

class UniqueString:
    def __init__(self, string=''):
        self.string = string

    def unique(self):
        d = {}
        for v in self.string:
            # print(v)
            d[v] = d.get(v, 0) + 1
        for a in d.values():
            if a > 1:
                return False
        return True

    def unique_inplace(self):
        self.string = ''.join(sorted(self.string))
        return self.string


    def run(self):
        sub = self.unique()
        sub1 = self.unique_inplace()
        return sub, sub1


if __name__ == "__main__":
    u = UniqueString('finding')
    results = u.run()
    print(results)
