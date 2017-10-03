isPrime n = hlp n 2
    where hlp n i
              | i * i > n = True
              | n `mod` i == 0 = False
              | otherwise = hlp n (i + 1)

primes = filter isPrime [2..]

ret = primes !! (10001 - 1)
