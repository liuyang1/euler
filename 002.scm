(define (fib thres)
  (define (gen lst)
    (let ((n (+ (car lst) (cadr lst))))
     (if (> n thres) lst
       (gen (cons n lst)))))
  (gen (list 2 1)))

(apply + (filter even? (fib (* 4 1000 1000))))
