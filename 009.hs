pythagorean (a, b, c) = a ^ 2 + b ^ 2 == c ^ 2

nums n = filter pythagorean xs
    where xs = [(a, b, n - a - b)| a <- [1..(n `div` 2)], b <- [(a + 1)..n]]

main = do
        print $ nums 1000

-- 8, 15, 17
-- 8 + 15 + 17 = 40
