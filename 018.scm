; also solve problems 067
(define *in* (open-input-file "018.data"))

(define (getall in)
  (define (hlp lst)
    (let ((l (read-line in)))
     (if (eof-object? l) lst
       (hlp (append lst (list l))))))
  (hlp '()))

(define (string-first s)
  (if (= (string-length s) 0) ""
    (let ((head (string-head s 1))
          (tail (string-tail s 1)))
      (if (string=? head " ")
        ""
        (string-append head (string-first tail))))))

(define (string-split s)
  (define (append-one lst one)
    (append lst (list one)))
  (define (hlp s lst)
    (let ((sl (string-length s)))
     (if (= 0 sl)
       lst
       (let* ((h (string-first s))
              (hl (string-length h)))
         (if (= sl hl) (append-one lst h)
           (hlp (string-tail s (+ 1 hl)) (append-one lst h)))))))
  (hlp s '()))

(define *data* (map (lambda (x) (map string->number (string-split x)))
                    (getall *in*)))
(define (expand lst)
  (append
    (cons (car lst)
          (map (lambda (x) (apply max x))
               (zip lst (cdr lst))))
    (list (car (last-pair lst)))))

(define (maxsum h lst)
  (if (null? lst)
    (apply max h)
    (let ((newh (map (lambda (x) (+ (car x) (cadr x)))
                     (zip (expand h) (car lst)))))
      (maxsum newh (cdr lst)))))

(maxsum (car *data*) (cdr *data*))
