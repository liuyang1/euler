#lang racket

(define (square x) (* x x))

(define (range start stop)
  (if (> start stop) '()
    (cons start (range (+ start 1) stop))))

(define *seq* (range 1 100))

(display (- (square (apply + *seq*)) (apply + (map square *seq*))))
(newline)
