def palindrome_permutation(s):
    s = s.lower()
    if len(s) == 0:
        return False
    
    if len(s) == 1:
        return True

    d = {}
    for v in s:
        if v != ' ':
            d[v] = d.get(v, 0) + 1
    print(d)
    one_count = -1
    for k, v in d.items():
        if v == 1:
            one_count += 1
    if one_count <= 1:
        return True
    else:
        return False

print(palindrome_permutation('12321'))
print(palindrome_permutation('kayak'))
print(palindrome_permutation('malayalam'))
print(palindrome_permutation('something'))
print(palindrome_permutation('foo'))
print(palindrome_permutation('Tact coa'))