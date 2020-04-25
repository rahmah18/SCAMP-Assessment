def fib():
     n = int(input())
     a = 0
     b = 1
     p = []
     for i in range(n):
         p.append(a)
         a,b = b,a+b
     print(p)
fib()