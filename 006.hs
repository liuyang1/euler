square x = x * x

r = (square $ sum seq) - (sum (map square seq))
    where seq = [1..100]
