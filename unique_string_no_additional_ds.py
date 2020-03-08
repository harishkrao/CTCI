class Unique_No_DS():
    def __init__(self, s):
        self.s = s
   
    def unique_no_ds(self):
        if len(self.s) == 0:
            return False
        if len(self.s) == 1:
            return True
        for i in range(len(self.s)):
            if self.s[i] not in self.s[:i] and self.s[i] not in self.s[i+1:]:
                return True
            else:
                return False

i = 'abcdef'
U = Unique_No_DS(i)
print(U.unique_no_ds())
