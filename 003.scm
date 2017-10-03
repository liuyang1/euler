#lang racket

(define (square x) (* x x))

(define (defactor n)
  (define (helper n divisor factor)
    (cond ((> (square divisor) n) (cons n factor)); N is one of factor
          ((= 0 (remainder n divisor))
           (helper (/ n divisor) divisor (cons divisor factor)))
          (else
            (helper n (+ divisor 1) factor))))
  (helper n 2 '()))

(display (defactor 13195))
(newline)
(display (defactor 600851475143))
(newline)
(display (defactor 625))
(newline)
