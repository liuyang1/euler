fs = [\n-> n * (n + 1) `div` 2,         -- triangle
     \n-> n * n,                        -- square
     \n -> n * (3 * n - 1) `div` 2,     -- pentagonal
     \n -> n * (2 * n - 1),             -- hexagonal
     \n -> n * (5 * n - 3) `div` 2,     -- heptagonal
     \n -> n * (3 * n - 2)]             -- octagonal

adj i x = (x `div` 100, x `mod` 100, i)
bak (a, b, _) = a * 100 + b

cand = concatMap (\(i, f) -> map (adj i) $ filter four $ map f [10..150]) $ zip [0..] fs
    where four n = n>999 && n<=9999

fst3 (a, b, c) = a
snd3 (a, b, c) = b
thd3 (a, b, c) = c

next st = map (:st) $ filter f cand
    where f i = fst3 i == snd3 (head st) && all (\j -> thd3 i /= thd3 j) st

cyc = head $ filter iscyc $ (!! 5) $ iterate (concatMap next) $ map (:[]) cand
    where iscyc st = snd3 (head st) == fst3 (last st)
ret = sum $ map bak cyc
main = print ret
