def shortestToChar(s, c):
    occurences = []
    for i in range(len(s)):
        if s[i]==c:
            occurences.append(i)
    print(occurences)
    answer = []
    for i in range(len(s)):
        if s[i] == c:
            answer.append(0)
        else:
            temp = []
            for j in range(len(occurences)):
                temp.append(abs(occurences[j] - i))
            answer.append(min(temp))
    print(answer)
                
                
            


#s = "loveleetcode"
#c = "e"
s = "aaab"
c = "b"
shortestToChar(s, c)
