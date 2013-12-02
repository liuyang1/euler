print min(((i*j*(i+1)*(j+1)/4,i*j) for i in xrange(10000) for j in xrange(100)), key = lambda x:abs(x[0] - 2 * 10 ** 6))
