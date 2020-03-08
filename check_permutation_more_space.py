class CheckPermutation:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def check_permutation(self):
        if len(self.s1) == 0 or len(self.s2) == 0 or len(self.s1) != len(self.s2): # n
            return False
        s = {}
        for val in self.s1:
            s[val] = 1
        for val in self.s2:
            if not s[val] == 1:
                return False
        print(s)
        return True


c = CheckPermutation('', '')
print(c.check_permutation())
