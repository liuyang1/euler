(define (range start stop)
  (if (> start stop) '()
    (cons start (range (+ start 1) stop))))

; generate 3-digit number in descend order
(define *3-digit* (reverse (range 100 999)))

; loop to divide base to get every digit
(define (digit n base)
  (if (< n base) (list n)
    (cons (remainder n base) (digit (quotient n base) base))))
(define (digit10 n) (digit n 10))

; check isPanlindrome?
(define (isPanlindrome? n)
  (let ((num-digit (digit10 n)))
   (equal? num-digit (reverse num-digit)))); digit of number equal to reverse..

; sorry for this Procedural approach
(define (loop lst maxval)
  (for-each (lambda (x) (for-each (lambda (y) 
                                    ; only x >= y to save half time
                                    (if (>= x y)
                                      (let ((p (* x y)))
                                       ; only prodution bigger than maxval
                                       ; then check isPanlindrome?
                                       ; to save more time
                                       (if (and (>= p maxval) (isPanlindrome? p))
                                         (set! maxval p)
                                         #f))
                                      #f))
                                  lst))
            lst)
  maxval)

(display (loop *3-digit* 0))
(newline)
;guile -s 004.scm  0.11s user 0.00s system 96% cpu 0.116 total

; TODO
; how to get production in descend order??
