#naming convention for methods is lowercase and separate words with underscore
def say_hi(name= "no name", age= 27)
    puts ("Hello World " + name + " you are " + age.to_s)
end

say_hi("Alan")

#return not needed in ruby but should be used 
def cube(num)
    return num * num * num
end

puts cube(3)

# elsif instead of elif for ruby 
# ! same  
is_hungry = true
if is_hungry
    puts ("I am hungry")
else
    puts ("I am not hungry")
end

# and and or same in Ruby
def find_max(num1, num2, num3)
    if num1 >= num2 and num1 >= num3
        return num1
    elsif num2 >= num1 and num2 >= num3
        return num2
    else
        return num3
    end
end

puts find_max(15,10,20)