def reverseWords(S):
        s = ""
        a = len(S)
        for i in range(len(S)-1,-1,-1):
                if S[i] ==".":
                        s+= S[i::a-1]  
                        a= i              
        return s  
        # code here 
        

s = input("enter")
print(reverseWords(s))