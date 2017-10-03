import System.IO
import Data.Char

headn n xs = fst $ splitAt n xs

-- 求其长度为n的连续子串
sublst n xs
    | length xs <= n = [xs]
    | otherwise = (headn n xs): (sublst n (tail xs))

process = maximum . map product . sublst 13

processFile fn = do fd <- openFile fn ReadMode
                    ls <- hGetContents fd
                    print $ process $ map digitToInt $ concat $ lines ls

main = processFile "data.008"
