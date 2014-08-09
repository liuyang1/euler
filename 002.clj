(defn fib [thresh]
  (defn gen [lst]
    (let [n (+ (nth lst 0) (nth lst 1))]
      (if (> n thresh) lst
        (gen (cons n lst)))))
  (gen '(2 1)))

(println (apply + (filter even? (fib (* 4 1000 1000)))))
