import Data.List (sort)

digits n = if a == 0 then [b] else digits a ++ [b]
    where (a, b) = divMod n 10

pandigital n = n > 10 ^ 8 && n < 10 ^ 9 && sort (digits n) == [1..9]

concatNum :: [Int] -> Int
concatNum = read . concatMap show

pand2 = filter pandigital $ map (\x -> concatNum (map (* x) [1..2])) [1000..10000]
pand3 = filter pandigital $ map (\x -> concatNum (map (* x) [1..3])) [100..333]
pand4 = filter pandigital $ map (\x -> concatNum (map (* x) [1..4])) [10..100]
pand5 = filter pandigital $ map (\x -> concatNum (map (* x) [1..5])) [10..100]

maxPand = maximum $ concat [pand2, pand3, pand4, pand5]
-- 932718654 = concatNum $ 9327 * [1, 2]
