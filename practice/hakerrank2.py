if __name__ == '__main__':
    n = int(input("Enter the number:"))
    if n >=1 and n <= 150:
        for i in range(1, n+1):
            print(f"{i}", end="")
    else:
        print("Check the number and try again")