(define (fact n)
  (if (= n 1) 1 (* n (fact (- n 1)))))

(define (digit n)
  (if (= n 0) '()
    (cons (remainder n 10) (digit (quotient n 10)))))

(display (apply + (digit (fact 100))))
(newline)
