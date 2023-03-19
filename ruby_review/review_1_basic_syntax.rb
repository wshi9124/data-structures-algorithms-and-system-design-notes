# print- does not append a new line automatically (same line)
# puts- treats array differently (new line)

puts [1,2]
print [1,2]

#naming convention- all lowercase and words split by underscore
character_name = "Bob"
character_age = "20"

puts (character_name + " is " + character_age + " years old")

#string, interger, float, boolean (true, false), nil (no value)

# \" for quotation mark, \n for new line 

# .upcase() .downcase() .length() .index() 
# name[i] same as python
# .abs() .round() .ceil .floor
# .strip() removes leading and trailing white space
puts "   yes   ".strip() 
# .include? "" will return a boolean 
puts "phrase".include? "hr"
# .to_s changes number to string (.to_int / .to_float)
puts ("to string " + 40.to_s)
# Math.sqrt() square root
puts Math.sqrt(36).to_int
# gets is same as input in python (.chomp() keeps everything in same line)
puts "Enter Name:"
name = gets.chomp()
puts ("Hello " + name + " welcome")
#string interpolation
name = "String Interpolation"
puts "This is #{name}"

#nil(Ruby) and None(Python) are similar except for Ruby returns nil in situations and Python raises an exception
