(require '[clojure.string :as string])
(def data (slurp "data.008"))

(defn preProcess [data]
  (map #(- (int %) (int \0))
       (reduce concat '() (map seq (string/split data #"[\s+]")))))

(defn maxAdjProd [a n]
  (def s (range 0 n))
  (apply max
         (map (fn [i] (reduce * (map #(nth a %) (map #(+ i %) s))))
              (range 0 (- (count a) n)))))

(println (maxAdjProd (preProcess data) 13))
