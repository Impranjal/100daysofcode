def main(word:str):
    l = 0
    n = len(word) -1
    while(l <=n):
        if word[l] == word[n]:
            l+=1
            n-=1
        else:
            return -1
    return 0
if __name__ == "__main__":
    word = input("enter the word\t")
    print(main(word))