(ns extproto.core
  (:gen-class))


(defprotocol Animalia (dream [this]))

(defprotocol Erinaceinae (go-fast [this]))

(extend-protocol Animalia 
  extproto.core.Erinaceinae
  (dream [this] "I dream about things."))

(defrecord Hedgehog [lovely-name]
  Erinaceinae
  (go-fast [this] (format "%s the Hedgehog has got to go fast." (get this :lovely-name))))



(defn -main
  [& args]  
  (let [my-hedgehog (Hedgehog. "Sanic")]
    (println (go-fast my-hedgehog))
    (println (dream my-hedgehog))))

;1> Sanic the Hedgehog has got to go fast.
;1> I dream about things.
