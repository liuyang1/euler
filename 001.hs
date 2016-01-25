main = print $ foldl1 (+) [i | i <- [0..(1000 - 1)], i `mod` 3 == 0 || i `mod` 5 == 0]
