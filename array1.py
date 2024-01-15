def contains_duplicate(s,t):
    hashset1 = set()
    hashset2 =set()
    for i in range(len(s)):
        hashset1[s[i]] = 1+hashset1.get(s[i],0)
        hashset2[t[i]] = 1+ hashset2.get(t[i],0)
    for j in hashset1:
        if hashset1.get("j",0) !=hashset2.get("j",0):
            return False
        else:
            return True
    
