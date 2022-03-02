def lcs(first, second, lenfirst, lensecond):
    if lenfirst == 0 or lensecond == 0:
        return 0

    if first[lenfirst-1] == second[lensecond-1]:
        return 1+lcs(first, second, lenfirst-1, lensecond-1)
    else:
        return max(lcs(first, second, lenfirst, lensecond-1), lcs(first, second, lenfirst-1, lensecond))

def memo_lcs(first, second, lenfirst, lensecond):

    k = [[-1]*(lensecond+1)for i in range(lenfirst+1)]

    if lenfirst == 0 or lensecond == 0:
        return 0
    if k[lenfirst][lensecond]!=-1:
        return k[lenfirst[lensecond]]

    if first[lenfirst-1] == second[lensecond-1]:
        k[lenfirst][lensecond] = 1+lcs(first, second, lenfirst-1, lensecond-1)
        return k[lenfirst][lensecond]
    else:
        k[lenfirst][lensecond] = max(lcs(first, second, lenfirst, lensecond-1), lcs(first, second, lenfirst-1, lensecond))
        return k[lenfirst][lensecond]

def dp_lcs(first, second, lenfirst, lensecond):
    k = [[-1] * (lensecond + 1) for i in range(lenfirst + 1)]

    for i in range(lenfirst+1):
        for j in range(lensecond+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif first[i - 1] == second[j - 1]:
                k[i][j] = 1 + k[i-1][j-1]
            else:
                k[i][j] = max(k[i][j-1], k[i-1][j])
    return k[lenfirst][lensecond]

def printLCS(first, second, lenfirst, lensecond):

    k = [[-1] * (lensecond + 1) for i in range(lenfirst + 1)]

    for i in range(lenfirst+1):
        for j in range(lensecond+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif first[i - 1] == second[j - 1]:
                k[i][j] = 1 + k[i-1][j-1]
            else:
                k[i][j] = max(k[i][j-1], k[i-1][j])

    i, j = lenfirst, lensecond
    lcs = ''
    while i>0 and j>0:
        if first[i-1] == second[j-1]:
            i -= 1
            j -= 1
            lcs = first[i-1] + lcs
        else:
            if k[i][j-1] > k[i-1][j]:
                j -= 1
            else:
                i -= 1
    return(lcs)

def longestCommomSubstring(X, Y, lenx, leny):
    k = [[0]*(leny+1) for i in range(lenx+1)]
    result = 0
    for i in range(lenx+1):
        for j in range(leny+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif X[i-1] == Y[j-1]:
                k[i][j] = 1 + k[i-1][j-1]
                result = max(result, k[i][j])
            else:
                k[i][j] = 0

    return result

x, y = 'abcdgh', 'abedfghr'
print(lcs(x,y, len(x), len(y)))
print(memo_lcs(x,y, len(x), len(y)))
print(dp_lcs(x,y, len(x), len(y)))
print(longestCommomSubstring(x,y, len(x), len(y)))
print(printLCS(x,y, len(x), len(y)))

