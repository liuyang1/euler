(defn digit [base n]
  (if (< n base) (list n)
    (cons (rem n base) (digit base (quot n base)))))

(def digit10 (partial digit 10))

(defn isPanlindrome? [n]
  (let [num-digit (digit10 n)]
    (= num-digit (reverse num-digit))))

(defn prod [lst]
  (for [i lst, j lst]
       (* i j)))

(println (apply max (filter isPanlindrome? (prod (range 100 1000)))))
