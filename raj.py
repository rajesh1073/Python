s1="masada"
s2="rajesh"
raj=""
for ch in s1:
    if ch in s2 and ch not in raj:
        raj=raj+ch
print(" ".join(raj))