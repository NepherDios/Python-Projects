def fizzBuzz(n):
	i = 1

	while i <= n:
		if not (i % 3) and not (i % 5):
			print("FizzBuzz")
		elif i % 3:
			print("Fizz")
		elif i % 5:
			print("Buzz")
		i+=1

fizzBuzz(20)
