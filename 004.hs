isPalind n = s == reverse s
    where s = show n

num = maximum $ filter isPalind [a * b | a <- xs, b <- xs]
    where xs = [100..1000]
