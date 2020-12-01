(ns advent-of-code.day1.day1
  (:require [clojure.edn :as edn]
            [clojure.string :as string]))

(def input-data
  (->> (slurp "/tmp/input.txt")
       string/split-lines
       (map edn/read-string)))

(defn create-subset [number entries]
  (map #(apply sorted-set (conj #{} number %)) entries))

(defn sum-equals-to-value [values]
  (if (= 2020 (reduce + values))
    values
    nil))

(->> (map #(create-subset % input-data) input-data)
     (reduce concat)
     (map sum-equals-to-value)
     (filter #(not= nil %))
     first
     (reduce *))

; implement part 2
