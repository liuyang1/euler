(define (isPrime? x)
  (define (helper i)
    (cond ((> (* i i) x) #t)
          ((= 0 (remainder x i)) #f)
          (else (helper (+ i 1)))))
  (helper 2))

(define (range low high)
  (define (iter i ret)
    (if (> i high) ret
      (iter (+ i 1) (cons i ret))))
  (iter low '()))

(define (sum-thresh n)
  (apply + (filter isPrime? (range 2 n))))

(display (sum-thresh (* 2 1000 1000)))
(newline)
