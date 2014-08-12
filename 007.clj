(def prime-gen
     (let [primes (atom [])]
       (for [n (iterate inc 2)
             :when (not-any? #(zero? (rem n %))
                             (filter #(<= (* % %) n)
                                     @primes))]
            (do (swap! primes conj n)
              n))))

(println (last (take 10001 prime-gen)))
