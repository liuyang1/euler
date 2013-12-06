; self defined range
(define (range end)
  (let ((prior (- end 1)))
   (if (< prior 0) '()
     (append (range prior) (list prior)))))

(display (apply + (filter (lambda (x) (or (= 0 (remainder x 3))
                                          (= 0 (remainder x 5))))
                          (range 1000))))
(newline)
