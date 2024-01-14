def longest_word(list_words):
    max=''
    for i in list_words:
        if len(i) > len(max):
            max=i
    return f"Longest word:{max} and Length of longest word:{len(max)}"


list_words=[]
n=int(input("Enter the length of list:"))
for i in range(n):
    words=input("Enter Words:")
    list_words.append(words)
print("List of words:",list_words)
print(longest_word(list_words))