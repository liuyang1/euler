(define fin (open-input-file "013.data"))

(define (getall in lst)
  (let ((c (read-line in)))
   (if (eof-object? c)
     lst
     (getall in (append lst (list c))))))

(define *sum* (reduce + 0 (map string->number (getall fin '()))))

(define (first-digit num n)
  (define base 10)
  (define thresh (expt base n))
  (define (loop t)
    (if (< t thresh) t (loop (quotient t base))))
  (loop num))

(first-digit *sum* 10)
