(define (isPrime? x)
  (define (helper i)
    (cond ((> (* i i) x) #t)
          ((= 0 (remainder x i)) #f)
          (else (helper (+ i 1)))))
  (helper 2))

(define (prime-nth n)
  (define (iter i num)
    (if (isPrime? num)
      (if (= i n) num
        (iter (+ i 1) (+ num 1)))
      (iter i (+ num 1))))
  (iter 1 2))

(display (prime-nth 10001))
(newline)
