def repli(c:str,start,end):
    if start>=end:
        return True
    return (c[start]==c[end]) and repli(c,start+1,end-1)

start =0
c = "abba"
end= len(c)
print(repli(c,start,end))