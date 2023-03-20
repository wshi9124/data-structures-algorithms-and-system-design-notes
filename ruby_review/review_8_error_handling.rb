# use begin rescue for error handling 
# in Ruby it is good practice to be specific on what type of errors you want to catch
lucky_nums = [4,8,15,16,23,42]

begin 
    lucky_nums["yes"]
    num = 10/0
rescue ZeroDivisionError
    puts "Division by zero error"
# you can store the error in a variable and return it
rescue TypeError => error
    puts error
end
