(println (apply + (filter (fn [x] (or (= 0 (rem x 3)) (= 0 (rem x 5))))
                          (range 1000))))
