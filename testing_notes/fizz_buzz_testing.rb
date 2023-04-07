def assert(condition, message)
    unless condition
        raise Exception.new message
    end
end

=begin
1 write a failing test
2 write just enough code to pass the test
3 refactor
red, green, refactor
=end 

=begin
1) if number divisable by 3 print "fizz"
2) if number is divisable by 5 print "buzz"
3) if number is divisable by both 3 and 5 return "fizzbuzz"
4) else return number
=end

# returns fizz for multiples of 3
def get_fizzbuzz_value(number)
    return "fizzbuzz" if number % 3 == 0 and number % 5 == 0
    return "fizz" if number % 3 == 0
    return "buzz" if number % 5 == 0 
    return number
end

assert(get_fizzbuzz_value(3) == "fizz", "should return fizz for multiples of 3")
assert(get_fizzbuzz_value(5) == "buzz", "should return buzz for multiples of 5")
assert(get_fizzbuzz_value(15) == "fizzbuzz", "should return fizzbuzz for multiples of 3 and 5")
assert(get_fizzbuzz_value(1) == 1, "should return number if not divisable by 3 or 5")

print "All Tests Pass"