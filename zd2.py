def decodeString(s):
    def helper(i):
        res = ""
        while i < len(s) and s[i] != ']':
            if not s[i].isdigit():
                res += s[i]
                i += 1
            else:
                k = 0
                while i < len(s) and s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                i += 1  # Skip '['
                decodedStr, i = helper(i)
                i += 1  # Skip ']'
                res += k * decodedStr
            i += 1
        return res, i

    i = 0
    result, _ = helper(i)
    return result

print("Введите:")
s = input()
print("Вывод:", decodeString(s))
