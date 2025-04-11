H, M = input().split()
H = int(H)
M = int(M)
if M < 45:
    H = (H - 1) % 24
    M += 15
else:
    M -= 45
print(H, M)