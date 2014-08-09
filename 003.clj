(defn square [x] (* x x))
(defn defactor [n]
  (defn hlp [n divisor factor]
    (if (> (square divisor) n)
      (cons n factor)
      (if (= 0 (rem n divisor))
        (hlp (/ n divisor) divisor (cons divisor factor))
        (hlp n (+ divisor 1) factor))))
  (hlp n 2 '()))

(println (defactor 13195))
(println (defactor 600851475143))
