count = 0
def foo( n ):
    global count
    if n == 0: 
        print(1)
        count = count +1
    else: 
        for i in range(1, pow(2, n)+1): 
            foo( n - 1 )


foo(5)
print(count)
