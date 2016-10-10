def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0: #divisible by both 3 and 5
      return "FizzBuzz"
    elif number % 3==0:#divisible by just 3
      return 'Fizz'
    elif number % 5==0:#divisible by just 5
      return 'Buzz'
    else:
      return number
fizz_buzz(3)    
fizz_buzz(5)
fizz_buzz(25)
fizz_buzz(15)
fizz_buzz(105)
fizz_buzz(101)
fizz_buzz(8)
      
        
