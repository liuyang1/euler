(define (leap? year)
  (let ((isCentury (= 0 (remainder year 100))))
   (if isCentury (= 0 (remainder year 400))
     (= 0 (remainder year 4)))))

(define *m-d-tab* '((1 . 31) (3 . 31) (5 . 31) (7 . 31) (8 . 31) (10 . 31) (12 . 31)
                             (2 . 28)
                             (4 . 30) (6 . 30) (9 . 30) (11 . 30)))

(define (cntMonthDays year month)
  (let ((d (cdr (assv month *m-d-tab*))))
   (if (and (leap? year) (= 2 month)) (+ 1 d) d)))

(define (nextDay yy mm dd ww)
  (define (fmtData yy mm dd ww)
    (let* ((nw (remainder ww 7))
           (nextM (> dd (cntMonthDays yy mm)))
           (nd (if nextM 1 dd))
           (nm (if nextM (+ mm 1) mm))
           (nextY (> nm 12))
           (nnm (if nextY 1 nm))
           (ny (if nextY (+ yy 1) yy)))
      (list ny nnm nd nw)))
  (fmtData yy mm (+ dd 1) (+ ww 1)))

(define (all lgclst)
  (cond ((= 0 (length lgclst)) #t)
        ((car lgclst) (all (cdr lgclst)))
        (else #f)))

(define (range-days day0 day1)
  (define (same? day0 day1) (all (map (lambda (x) (= (car x) (cadr x))) (zip day0 day1))))
  (if (same? day0 day1) '()
    (cons day0 (range-days (apply nextDay day0) day1))))

(define (cond? yy mm dd ww)
  (and (>= yy 1901) (<= yy 2000) (= dd 1) (= ww 0)))

(length (filter (lambda (x) (apply cond? x))
                (range-days '(1900 1 1 1) '(2000 12 31))))
