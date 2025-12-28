# In tất cả số Armstrong có 3 chữ số.

for i in range(100, 1000):
   tram = i//100
   chuc = (i//10) % 10
   donvi = i % 10
   
   if i == (tram**3 +chuc**3 + donvi**3): 
       print(i)