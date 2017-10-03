defactor n = hlp n 2
    where hlp n i
              | i * i > n = [n]
              | n `mod` i == 0 = i: hlp (n `quot` i) i
              | otherwise = hlp n (i + 1)

main = do
        print $ defactor 13195
        print $ defactor 600851475143
