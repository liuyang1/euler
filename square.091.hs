{-# LANGUAGE TupleSections #-}
newtype Point = Point (Integer, Integer) deriving Show

vec (Point (x0, y0)) (Point (x1, y1)) = Point (x0 - x1, y0 - y1)

nrm2 (Point (x, y)) = x * x + y * y

r a b c
  | c > a && c > b = c == a + b
  | a > c && a > b = a == b + c
  | b > c && b > a = b == a + c
  | otherwise = False

-- right triangles
isRight a b = r (nrm2 a) (nrm2 b) (nrm2 (vec a b))

-- drop first (0,0)
grid n m = tail [Point (x, y) | x <- [0..n], y <- [0..m]]

comb2 [x,y] = [(x, y)]
comb2 (x:xs) = map (x,) xs ++ comb2 xs

rightTri n m = filter (uncurry isRight) $ comb2 $ grid n m

main = print $ length $ rightTri 50 50
