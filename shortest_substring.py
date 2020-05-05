from collections import defaultdict
import logging


class substring:
    def __init__(self, string='', charset={}):
        self.string = string
        self.charset = charset

    def shortest_substring(self):
        str_loc = [i for i in self.string]
        ind = {}
        for v in str_loc:
            for val in self.charset:
                if v == val:
                    if v in ind.keys():
                        ind[v].append(str_loc.index(v))
                    else:
                        ind[v] = [str_loc.index(v)]
        print(ind.items())

    def run(self):
        sub = self.shortest_substring()
        return sub


if __name__ == "__main__":
    input = 'figehaeci'
    input2 = 'fucehaeve'
    input_set = {'a', 'e', 'i'}
    input_set2 = {'a', 'e', 'c'}
    a = substring(input, input_set)
    # print(a.run())
    output = a.run()
    print(output)
    a = substring(input2, input_set2)
    output = a.run()
    print(output)
