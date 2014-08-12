; only for small number
; for big number will stack overflow
(defn sieve [s]
  (cons (first s)
        (lazy-seq (sieve (filter #(not= 0 (mod % (first s)))
                                 (rest s))))))

(println (last (take 1001 (sieve (iterate inc 2)))))
