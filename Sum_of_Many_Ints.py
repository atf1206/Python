
def f(n, m):
    n = int(n)
    counter = 0
    leftover = 0
    
    if n == m:
        counter = (n-1)/2.0 * n
        return counter
        
    if n < m:
        counter = n/2.0 * (n+1)
        return counter
        
    elif n > m:
        #print "adding ", ((m-1)/2.0) * m
        counter = ((m-1)/2.0) * m
        
        #print "multiplying by ", (int(1.0 * n / m))
        counter *= (int(1.0 * n / m))
        
        leftover = (n - int(1.0 * n / m) * m)
        print "leftover = ", leftover
        counter += (leftover/2.0) * (leftover+1)
        
        #print "returning ", counter
        return counter
    else:
        return False
