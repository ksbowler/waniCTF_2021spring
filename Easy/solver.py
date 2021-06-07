def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext

def decrypt(ct,a,b):
	pt = ""
	for x in ct:
		if ord("A") <= ord(x) <= ord("Z"):
			x = ord(x) - ord("A")
			for i in range(26):
				if x == (a*i+b)%26:
					x = chr(i + ord("A"))
					pt += x
					break
		else: pt += x
	return pt


enc = "HLIM{OCLSAQCZASPYFZASRILLCVMC}"
test = "FLAG"
ans = []
for i in range(len(test)):
	temp = []
	for a in range(26):
		for b in range(26):
			t = encrypt(test[i],a,b)
			if t == enc[i]:
				temp.append([a,b])

	ans.append(temp)

#print(ans)
#print(ans[0])
for i in range(len(ans[0])):
	#ans[0][i]が他にもあるか探索
	check = True
	for j in range(1,len(ans)):
		ch = False
		for k in range(len(ans[j])):
			if ans[0][i] == ans[j][k]:
				ch = True
				break
		if not ch:
			check = False
			break
	if check:
		print(ans[0][i])
		print(decrypt(enc,ans[0][i][0],ans[0][i][1]))
