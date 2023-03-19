puts "Enter First Number: "
num1 = gets.chomp().to_f
puts "Enter Operator: "
op = gets.chomp()
puts "Enter Second Number: "
num2 = gets.chomp().to_f

# == same as python
if op == "+"
    puts (num1 + num2)
elsif op == "-"
    puts (num1 - num2)
elsif op == "*"
    puts (num1 * num2)
elsif op == "/"
    puts (num1 / num2)
else
    puts "Invalid Operator"
end
