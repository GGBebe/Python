x = 13
y = 55
z = 37
if x > y and x > z:
    if y > z:
        print(f"{x} en büyük sayı ve {z} en küçük sayıdır.")
    else:
        print(f"{x} en büyük sayı ve {y} en küçük sayıdır.")
elif y > x and y > z:
    if x > z:
        print(f"{y} en büyük sayı ve {z} en küçük sayıdır.")
    else:
        print(f"{y} en büyük sayı ve {x} en küçük sayıdır.")
elif z > x and z > y:
    if x > y:
        print(f"{z} en büyük sayı ve {y} en küçük sayıdır.")
    else:
        print(f"{z} en büyük sayı ve {x} en küçük sayıdır.")
else:
    print("sayılar arasında eşitlik vardır.")