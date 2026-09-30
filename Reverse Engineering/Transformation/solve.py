def reverse_operation(c):
    n = ord(c)
    n1 = chr(n >> 8)
    n2 = chr(n & 0xFF)
    return n1, n2
enc = '慣慤敭祻ㄶ形楴獟楮獴㌴摟潦弸強㤰扡㌷敽'
flag = ''
for i in enc:
    n1, n2 = reverse_operation(i)
    flag = flag + n1 + n2
print(flag)