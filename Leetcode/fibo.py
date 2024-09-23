def main(n:int):
    if n<= 1:
        return n
    return main(n-1)+main(n-2)


if __name__ == "__main__":
    n = int(input("no 1\t"))
    print(main(n))
