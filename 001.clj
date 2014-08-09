(defn isCond
  [x]
  (or (= 0 (mod x 3)) (= 0 (mod x 5))))
(println (apply + (filter isCond
                          (range 1000))))
