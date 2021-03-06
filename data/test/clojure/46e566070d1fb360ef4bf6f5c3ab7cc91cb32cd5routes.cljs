(ns dizzy.routes
    (:require-macros [secretary.core :refer [defroute]])
    (:import goog.History)
    (:require [secretary.core :as secretary]
              [goog.events :as events]
              [goog.history.EventType :as EventType]
              [re-frame.core :as re-frame]))

(defn hook-browser-navigation! []
  (doto (History.)
    (events/listen
     EventType/NAVIGATE
     (fn [event]
       (secretary/dispatch! (.-token event))))
    (.setEnabled true)))

(defn app-routes []
  (secretary/set-config! :prefix "#")
  ;; --------------------
  ;; define routes here
  (defroute "/" []
    (re-frame/dispatch [:set-active-page :landing-page]))

  (defroute "/features" []
    (re-frame/dispatch [:set-active-page :features-page]))

  (defroute "/livia-charman-interview" []
    (re-frame/dispatch [:set-active-page :interview-page]))


  ;; --------------------
  (hook-browser-navigation!))
