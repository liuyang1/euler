(define source (open-input-file "data.008"))

(define (getall fn lst)
  (let ((c (read-char fn)))
   (if (eof-object? c)
     lst
     (if (eq? c #\newline)
       (getall fn lst)
       (getall fn (append lst (list  c)))))))

(define *seq* (map char->digit (getall source '())))

(define *num-adj* 13)

(define (left-shift seq n)
  (if (= n 0) seq
    (left-shift (cdr seq) (- n 1))))

(define (range b e p)
  (if (>= b e)
    '()
    (cons b (range (+ b p) e p))))

(define *lst*
  (apply zip
         (map (lambda (x) (left-shift *seq* x))
              (range 0 *num-adj* 1))))

(apply max
       (map (lambda (x) (reduce * 1 x))
            *lst*))
