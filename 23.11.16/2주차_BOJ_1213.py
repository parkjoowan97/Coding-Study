S = input()
dict = {}
for i in range (0,len(S)):
    if S[i] in dict:
        dict[S[i]] += 1
    else:
        dict[S[i]] = 1

alphabet = sorted(dict.items())
cnt = 0
k = 0
for i in range (0,len(alphabet)):
    if alphabet[i][1] % 2 == 1:
        cnt += 1
        k += i
if cnt == 0 or cnt == 1:
    ans = ""
    if cnt == 1:
        for i in range (0,len(alphabet)):
            if i == k:
                ans += str(alphabet[i][0]) * ((alphabet[i][1] - 1) // 2)
            else:
                ans += str(alphabet[i][0]) * ((alphabet[i][1]) // 2)
        
        ans_reverse = "".join(reversed(ans))
        ans += str(alphabet[k][0])
        ans += ans_reverse
    if cnt == 0:
        for i in range (0,len(alphabet)):
            ans += str(alphabet[i][0]) * ((alphabet[i][1]) // 2)
        ans_reverse = "".join(reversed(ans))
        ans += ans_reverse 
    print(ans)
else:
    print("I'm Sorry Hansoo")
        
