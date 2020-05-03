from collections import defaultdict


class anagram:
    def __init__(self, words=[]):
        self.words = words

# O(N^2) * N log N = O(N^2)

    def group_anagrams(self):
        temp_dict = defaultdict() # O(1)
        temp_list = [] # O(1)
        for val in self.words: # O(N) # O(1)
            temp_list.sort() # O(N)
            v = ''.join([i for i in val]) # O(1)
            if v not in temp_dict.keys(): # O(1)
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
