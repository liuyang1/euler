(define (triangle x) (/ (* x (+ x 1)) 2))

(define (factor n)
  (define (hlp num f)
    (if (= 0 (remainder num f))
      (+ 1 (hlp (/ num f) f))
      0))
  (define (loop num f)
    (if (= num 1) '()
      (let* ((freq (hlp num f))
             (next (loop (/ num (expt f freq)) (+ f 1))))
        (if (= freq 0)
          next
          (cons (cons f freq) next)))))
  (loop n 2))

(define (factor-counter lst)
  (reduce * 1 (map (lambda (x) (+ 1 (cdr x))) lst)))

(define (loop i)
  (let* ((tri (triangle i))
         (fac (factor tri))
         (cnt (factor-counter fac)))
    (if (> cnt 500)
      (begin (display tri) (display "\t") (display cnt) (display "\t") (display fac) (newline))
      (loop (+ i 1)))))

(loop 1)
