(ns advent-of-code.day2.day2-pt2
  (:require [clojure.string :as string]
            [clojure.set :as s]
            [clojure.edn :as edn]))

(def input-data
  (->> (slurp "/tmp/input.txt")
       string/split-lines))

(defn parse-data [data]
  (let [parsed-data (string/split data #" ")]
    {:indexes       (-> (nth parsed-data 0)
                      (string/split #"-"))
     :character   (first (concat (string/replace (nth parsed-data 1) #":" "")))
     :password-as-list (seq (nth parsed-data 2))
     }))

(defn verify-position [coll]
  (let [int-range (map edn/read-string (:indexes coll))
        actual-range (map dec int-range)
        password-list (:password-as-list coll)
        password-positions [(nth password-list(first actual-range)) (nth password-list (last actual-range))]]
    (if (not= true (apply = password-positions))
      (some #{(:character coll)} password-positions)
      nil)))

(->> input-data
     (map parse-data)
     (map verify-position)
     (filter #(not= nil %))
     count)
