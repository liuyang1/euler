{- find the smallest member of the longest amicable chian with no element exceeding one million -}
import qualified Data.Map as M
import Data.List (elemIndex, maximumBy)
import Data.Maybe (fromMaybe)

mapToSnd f = map (toSnd f)
    where toSnd f a = (a, f a)

mapToFst f = map (toFst f)
    where toFst f a = (f a, a)

maxOn f xs = maximumBy (\x y->compare (f x) (f y)) xs

isprime 2 = True
isprime n = h n 2
    where h n d
            | n `mod` d == 0 = False
            | d * d > n = True
            | otherwise = h n (d + 1)

primes = filter isprime [2..]

freq p (t, n)
    | r == 0 = freq p (t+1, d)
    | otherwise = (t, n)
       where (d,r) = n `divMod` p

h n (p:primes)
    | n == 1 = []
    | p * p > n = [(n,1)]
    | f == 0 = h m primes
    | otherwise = (p,f): (h m primes)
                          where (f, m) = freq p (0, n)

factor :: Integer -> [(Integer, Integer)]
factor n = h n primes

multi :: [(Integer, Integer)] -> Integer
multi xs = product $ [p^f | (p,f)<-xs]

amic :: [(Integer,Integer)] -> [Integer]
amic [] = [1]
amic ((p,f):xs) = (*) <$> [p^i | i <- [0..f]] <*> (amic xs)

{- 1, genereate factor frequency list
   2, from factor, generate all factor
   3, sum to get amicable number
-}
amicable :: Integer -> Integer
amicable n = (subtract n) $ sum $ amic $ factor n

nn = 1000 * 1000
amicLst = mapToSnd amicable [1..nn]
amicTbl = M.fromList $ amicLst

seqAmic 0 = []
--seqAmic n = n: seqAmic (amicTbl M.! n)
seqAmic n = n: seqAmic (M.findWithDefault 0 n amicTbl)


evenPick [] = []
evenPick [x] = [x]
evenPick (x:_:xs) = x: evenPick xs

pair xs = zip xs (evenPick xs)

    -- TODO: ring detect
    -- case, [6] [25,6..], [220,284], [562,284,220,..]
detect xs = map fst $ t0 ++ (if null t1 then [] else [head t1])
    where --(h, t) = splitAt 1 $ zip xs (evenPick xs)
          (t0, t1) = span (\(s, f)->s /= f) $ tail $ pair xs

ringAmic n = length $ detect $ seqAmic n

ans = mapToFst ringAmic [2..nn]
