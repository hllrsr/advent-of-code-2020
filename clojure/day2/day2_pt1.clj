(ns advent-of-code.day2.day2_pt1
  (:require [clojure.string :as string]
            [clojure.set :as s]
            [clojure.edn :as edn]))

(def input-data
  (->> (slurp "/tmp/input.txt")
       string/split-lines))

(defn parse-data [data]
  (let [parsed-data (string/split data #" ")]
    {:range       (-> (nth parsed-data 0)
                      (string/split #"-"))
     :character   (first (concat (string/replace (nth parsed-data 1) #":" "")))
     :password    (nth parsed-data 2)
     :frequencies (frequencies (nth parsed-data 2))
     }))


(defn check-frequencies [coll]
  (let [int-range (map edn/read-string (:range coll))
        actual-range (range (first int-range) (+ 1 (last int-range)))
        character-frequency (get (:frequencies coll) (:character coll))]
    (some #{character-frequency} actual-range)))


(->> input-data
     (map parse-data)
     (map check-frequencies)
     (filter #(not= nil %))
     count)
