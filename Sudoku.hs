module Sudoku where

import           Control.Arrow ((&&&))
import           Data.Char     (digitToInt)
import           Data.List     (group, lines, minimumBy, nub, sort, splitAt,
                                transpose)
import           System.IO

-- basic function
groupCnt xs = map (head &&& length) $ group $ sort xs

minimumOn f xs = minimumBy (\x y -> compare (f x) (f y)) xs

toSnd0 f a = (a, f a)
toSnd f = map (toSnd0 f)

-- 按段划分，类似于Python中的xs[::9]
--splitSeg :: Int -> [Int] -> Mat
splitSeg n [] = []
splitSeg n xs = h: splitSeg n t
    where (h, t) = splitAt n xs

-- problem related
type Mat = [[Int]]

puzzle0 = [[5,3,0,0,7,0,0,0,0]
          ,[6,0,0,1,9,5,0,0,0]
          ,[0,9,8,0,0,0,0,6,0]
          ,[8,0,0,0,6,0,0,0,3]
          ,[4,0,0,8,0,3,0,0,1]
          ,[7,0,0,0,2,0,0,0,6]
          ,[0,6,0,0,0,0,2,8,0]
          ,[0,0,0,4,1,9,0,0,5]
          ,[0,0,0,0,8,0,0,7,9]] :: Mat
puzzle3 = [[2,0,0,0,8,0,3,0,0]
          ,[0,6,0,0,7,0,0,8,4]
          ,[0,3,0,5,0,0,2,0,9]
          ,[0,0,0,1,0,5,4,0,8]
          ,[0,0,0,0,0,0,0,0,0]
          ,[4,0,2,7,0,6,0,0,0]
          ,[3,0,1,0,0,7,0,4,0]
          ,[7,2,0,0,4,0,0,6,0]
          ,[0,0,4,0,1,0,0,0,3]] :: Mat
cands = [1..9]
boxSize = 3
matSize = 9
rs = [0..8]
mat2 = matSize * matSize
-- 所有的位置坐标
poss = sequence [[0..(matSize - 1)], [0..(matSize - 1)]]

-- 返回棋盘中对应的行或者列,或者所处的3x3的小方格
row, col :: Mat -> Int -> [Int]
row m x = m !! x
col m y = transpose m !! y

regionN n x = take n [(roundN n x)..]
    where roundN n x = (x `div` n) * n

box :: Mat -> Int -> Int -> [Int]
box m x y = map (\(i:j:_) -> (m !! i) !! j) $ boxPos x y
    where boxPos x y = sequence [regionN boxSize x, regionN boxSize y]
-- 找到所有的备选项
fcand :: Mat -> Int -> Int -> [Int]
fcand m x y = filter (`notElem` c) cands
    where c = row m x ++ col m y ++ box m x y

valid0 xs = all (\(x,c)->x==0||c<=1) $ groupCnt xs
valid :: Mat -> Bool
valid m = all valid0  (map (row m) rs ++ map (col m) rs)
-- valid should check box type, too. But it works now, so no further improve

updateCell :: Mat -> Int -> Int -> Int
updateCell m x y
    | v /= 0 = v
    | v == 0 && length vs == 1 = head vs -- 只有在一个可选择结果的时候，直接选择
    | otherwise = 0
    where v = m !! x !! y
          vs = fcand m x y

possCell :: Mat -> Int -> Int -> [Int]
possCell m x y
    | v /= 0 = [v]
    | v == 0 = vs
    where v = m !! x !! y
          vs = fcand m x y

rebuildMat :: [Int] -> Mat
rebuildMat = splitSeg matSize

-- 策略非常简单
-- 采用直接推断的方式: 同行同列同小格的元素不再出现,如果剩余备选项只有一个，则固定选择。
-- 否则，进入到下一个推测中
infer0 :: Mat -> Mat
infer0 m = if nm == m then m else infer0 nm
    where nm = updateCand m
          updateCand m = rebuildMat . map (\(i:j:_) -> updateCell m i j) $ poss

pgs mat = sum $ map (length . filter (/= 0)) mat

-- given mat, return index and its candidates (its candidates is minimal)
-- WARNING: minimum is fold1 function ,so it doesn't work on empty list
minBranch :: Mat -> ([Int], [Int])
minBranch m = if null mc then ([],[]) else minimumOn (\(_,c) -> length c) mc
    where mc = filter (\(_,c) -> length c > 1) $ toSnd (\(i:j:_) -> possCell m i j) poss

update xs n a = take n xs ++ [a] ++ drop (n + 1) xs

update2 mat n m a = take n mat ++ [update (mat !! n) m a] ++ drop (n+1) mat

possM m = if t == ([],[]) then [] else possMat m t
    where t = minBranch m
          possMat m (x:y:_, cs) = map (update2 m x y) cs

sudoku :: Mat -> [Mat]
sudoku m
  | pgs m0 == mat2 = [m0]
  | otherwise = filter valid $ concatMap sudoku $ possM m0
    where m0 = infer0 m

showMat m = do
        print "mat:"
        mapM_ print m

test puzzle = do
        print "orignal puzzle"
        showMat puzzle
        print $ pgs puzzle
        print "solution"
        showMat $ head $ sudoku puzzle

proc s = map (map (map digitToInt) . tail) $ splitSeg (matSize + 1) $ lines s

topLeft3 m = (\(x:y:z:_) -> x * 100 + y * 10 + z) $ take 3 $ head m

main = do
    s <- readFile "p096_sudoku.txt"
    --test $ (!! 0) $ proc s
    mapM_ showMat $  sudoku $ (!! 48) $ proc s
    --print $ topLeft3 $ head $ sudoku $ (!! 48) $ proc s
    print $ toSnd0 sum $ map (sum . map topLeft3 . sudoku) $ proc s
