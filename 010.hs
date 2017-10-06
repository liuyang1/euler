-- slow, but work
-- sieve solution, check http://github.com/liuyang1/test/lang/haskell codebase
isPrime x = all (\i -> x `mod` i /= 0) $ takeWhile (\i -> i * i <= x) (2:[3,5..(x `div` 2)])

primes n = filter isPrime [2..n]

main = do
        print $ sum $ primes (1000 * 1000 * 2)
