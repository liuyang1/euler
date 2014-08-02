(define (range b e)
  (if (> b e) '()
    (cons b (range (+ b 1) e))))

(define (fact b e)
  (reduce * 1 (range b e)))

(define (com m n)
  (/ (fact (+ 1 n) m) (fact 1 n)))

(define (route m n)
  (com (+ n m) n))

(route 20 20)
