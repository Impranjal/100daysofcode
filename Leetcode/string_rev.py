def main(word:str,word1:str):
        print(word[::-1],word1)
        if word[::-1] == word:
            
            return True
        else:
            return False
        
        return False


if __name__ == "__main__":
    word = input("enter\t")
    word1 = input("2 word\t")
    print(main(word,word1))