from pwn import *
import re
def extract_secret(binary_bytes: bytes) -> int:
    idx = binary_bytes.find(b'\xc7\x45\xfc')
    return int.from_bytes(binary_bytes[idx+3:idx+7], byteorder='little')
io = remote("chatelaine.cylabacademy.net", 24588)
start = io.recvuntil(b"What's the secret?:", timeout=10)
for i in range(1, 21):
    text = start.decode(errors='ignore')
    hex_data = re.search(r'([0-9a-fA-F]{100,})', text).group(1)
    binary_bytes = bytes.fromhex(hex_data)
    secret = extract_secret(binary_bytes)
    io.sendline(str(secret).encode())
    try:
        start = io.recvuntil(b"What's the secret?:", timeout=10)
    except EOFError:
        print(io.recvall(timeout=5).decode(errors='ignore'))
        break
io.interactive()
