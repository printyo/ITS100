sentence = input("Input: ").split()
ans = {}
for key in sentence:
    key = key.lower()
    if key in ans:
        ans[key] += 1
    else:
        ans[key] = 1
lis = sorted(ans.values(), reverse=True)
maxNum = lis[0]
print("Output:")
for key, value in ans.items():
    if value == maxNum:
        print(key, "=", value)