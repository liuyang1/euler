(define (square x) (* x x))
(define (isPythagorean? a b c)
  (eq? (+ (square a) (square b)) (square c)))

(define (range b e)
  (if (> b e) '()
    (cons b (range (+ b 1) e))))

; better generate function
(define (next a b c)
  (if (> a c) '()
    (if (> b (- c 2))
      (list (+ a 1) (+ a 2) (- (+ b c) a 3))
      (list a (+ b 1) (- c 1)))))

(define (next-inf v)
  (let ((n (apply next v)))
   (if (and n (apply isPythagorean? n))
     (reduce * 1 n)
     (next-inf n))))

(display (next-inf '(1 1 998)))
