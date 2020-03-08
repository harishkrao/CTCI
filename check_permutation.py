class CheckPermutation:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def check_permutation(self):
        if len(self.s1) == 0 or len(self.s2) == 0: # n
            return False
        self.s1 = sorted(self.s1)
        self.s2 = sorted(self.s2)
        if self.s1 == self.s2: # n O(n)
            return True
        else:
            return False


c = CheckPermutation('abcd', 'cba')
print(c.check_permutation())
