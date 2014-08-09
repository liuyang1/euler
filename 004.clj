(defn digit [n base]
  (if (< n base) (list n)
    (cons (rem n base) (digit (quot n base) base))))

(defn isPanlindrome? [n]
  (let [num-digit (digit n 10)]
    (= num-digit (reverse num-digit))))

(defn prod [lst]
  (for [i lst, j lst]
       (* i j)))

(println (apply max (filter isPanlindrome? (prod (range 100 1000)))))
