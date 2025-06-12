#lang racket

(define my-list '(1 2 3 4 5))

(define (add-one lst)
	(if (null? lst)
			'()
			(cons (+ 1 (car lst)) (add-one (cdr lst)))))

(add-one my-list)

(define (square lst)
	(if (null? lst)
			'()
			(cons (* (car lst) (car lst)) (square (cdr lst)))))

(square my-list)

(define (map f lst)
	(if (null? lst)
			'()
			(cons (f (car lst)) (map f (cdr lst)))))

(map (lambda (x) (+ x 1)) my-list)
(map (lambda (x) (* x x)) my-list)

(define (even? x)
  (= 0 (modulo x 2)))
(define (odd x)
  (= 1 (modulo x 2)))
(define (odd-prime x)
  (not (even? x)))

(filter even? my-list)
(filter odd? my-list)

(define (sum xs)
  ;; Locally define a helper function to encapsulate the accumulation logic
  (define (go xs acc)
    (if (null? xs)
        acc
        (go (cdr xs) (+ acc (car xs)))))
  ;; Then call that function, and return its result
  (go xs 0))

(sum my-list)


(define (sum-of-squares lst)
;; Locally define a helper function to encapsulate the accumulation logic
(define (squared-list xs)
  (if (null? xs)
    '()
    (cons (* (car xs) (car xs)) (squared-list (cdr xs)))))
  ;; Define another helper function to sum the squared values
  (define (go xs acc)
    (if (null? xs)
      acc
      (go (cdr xs) (+ acc (car xs)))))
  ;; Then call that function, and return its result
  (go (squared-list lst) 0))

(sum-of-squares my-list)

(define (reduce f init lst)
    (if (null? lst)
        init
        (reduce f (f init (car lst)) (cdr lst))))

(reduce + 0 (map (lambda (x) (* x x))  my-list))

(reduce + 0
  (map (lambda (x) (* x x))
    (filter (lambda (x) (= 0 (modulo x 2))) my-list)
    )
)
