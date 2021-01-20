#数字转Base64
def p64(n):
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result = []
    temp = n
    print(temp%64)
    if 0==temp:
        result.append("0")
    else:
        while 0 <temp:
            result.append(table[int(temp%64)])
            temp //= 64
    return ''.join([x for x in reversed(result)])
print(p64(0b01100110011011000110000101100111011110110100011001110101010011100101111101100111011010010100011001111101))
print(p64(0xc8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2))

