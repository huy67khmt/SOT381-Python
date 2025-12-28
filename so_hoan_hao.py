# Tìm số hoàn hảo nhỏ hơn 1000.

for i in range(1,1000): 
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(f"{i} la so hoan hao")