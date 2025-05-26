N , M = input().split()
N = int(N)
M = int(M)
wordlist = []
for i in range(N) :
    word = input()
    if len(word) >= M :
        wordlist.append(word)
print(wordlist)
