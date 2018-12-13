p x = x * (3 * x - 1) `div` 2

pentagon = map p [1..]

idxs = concatMap (\x -> map (\b -> (b, x)) [1..(x - 1)]) [1..]

isIn n (x:xs) = case compare n x of
                  EQ -> True
                  GT -> isIn n xs
                  LT -> False

a = 1560090
ps = take 1200 pentagon

-- searchDiff d = filter (\x -> isIn (d + x) pentagon) pentagon
region d = map fst $ takeWhile (\(a, b) -> b - a <= d) $ zip pentagon (tail pentagon)
pent d = filter (\x -> isIn (d + x) pentagon) $ region d

xs0 = map region pentagon
