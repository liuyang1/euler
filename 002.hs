fibn (a, b) = (b, a + b)

fib = map fst $ iterate fibn (1, 1)

fibEvenSum t = sum $ filter even $ takeWhile (< t) fib

main = print $ fibEvenSum (4 * 1000 * 1000)
