haystack ="leetcode"
needle = "leeto"
def strStr(haystack, needle):
    if len(haystack)>1:
        index = -1
        count =0
        for i in range(len(haystack)):
            if needle[0] == haystack[i] and needle[1] == haystack[i+1]:
                for j in range(len(needle)):
                    if needle[j] == haystack[i+j]:
                        count+=1
                    else:
                        break
            if count == len(needle):
                index = i
                return index
        return -1
    else:
        if haystack == needle:
            return 0
        else:
            return index

ans = strStr(haystack, needle)
print(ans)
