from collections import defaultdict


class anagram:
    def __init__(self, words=[]):
        self.words = words

    def group_anagrams(self):
        temp_dict = defaultdict()
        temp_list = []
        for val in self.words:
            for c in val:
                temp_list.append(c)
            temp_list.sort()
            v = ''.join(temp_list)
            if v not in temp_dict.keys():
                temp_dict[v] = [val]
            else:
                temp_dict[v].append(val)
            temp_list = []
        return list(temp_dict.values())

    def run(self):
        possible_count = self.group_anagrams()
        return possible_count


if __name__ == "__main__":
    input = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    input2 = ['eat', 'ate', 'apt', 'pat', 'tea', 'now', 'ateate']
    a = anagram(input)
    output = a.group_anagrams()
    print(output)
    a = anagram(input2)
    output2 = a.group_anagrams()
    print(output2)
    a.run()
