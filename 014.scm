(load-option 'format)

(define (collatz n)
  (if (= 0 (remainder n 2))
    (/ n 2)
    (+ (* 3 n) 1)))

(define (collatz-cnt n)
  (define (hlp n c)
    (if (= n 1) c
      (hlp (collatz n) (+ c 1))))
  (hlp n 1))

(define (max-collatz thresh)
  (define (hlp n nm m)
    (if (> n thresh) nm
    (let ((t (collatz-cnt n))
          (n1 (+ n 1)))
      (format #t "~a\t~a\t~a\t~a~%" n t nm m)
     (if (> m t)
       (hlp n1 nm m)
       (hlp n1 n t)))))
  (hlp 2 2 2))

(max-collatz (expt 10 6))
