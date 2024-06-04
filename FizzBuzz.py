# 1부터 100사이의 숫자를 프린트하는 프로그램을 작성
# 3의 배수이면 "Fizz"를, 5의 배수이면 "Buzz"를, 15의 배수이면 "FizzBuzz" 를 프린트

def fizzbuzz(n):
  for i in range(1, n+1):
    if i % 5 == 0:
      print('Buzz', end=' ')
