(defn square [x] (* x x))

(def lst (range 1 101))

(println (- (square (apply + lst)) (apply + (map square lst))))
