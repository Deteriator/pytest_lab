import fizzbuzz

def test_fizzbuzz(num):
	assert fizzbuzz(10) == "buzz"
	assert fizzbuzz(3) == "fizz"
	assert fizzbuzz(15) == "fizzbuzz"
	assert fizzbuzz(100) == "buzz"