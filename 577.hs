hexgaon n = sum $ zipWith (*) (map go [n,(n-3)..1]) [1..]
    where go n = (n - 1) * (n - 2) `div` 2

r n = sum $ map hexgaon [3..n]

r1 n = sum $ zipWith (*) (map go [n,(n-3)..1]) [1..]
    where go n = n * (n - 1) * (n - 2) `div` 6

main = print $ r1 12345
