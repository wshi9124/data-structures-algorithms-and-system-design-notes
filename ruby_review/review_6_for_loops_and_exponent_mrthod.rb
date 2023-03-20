food = ["pizz", "sushi", "chicken", "soup"]

# similar to python 
for f in food
    puts f
end

food.each do |f|
    puts f
end

#find index
for i in 0..food.length()-1
    puts i
end

4.times do |i|
    puts i
end

# Exponent Method (no need for || after do because we do not need index in the method)
def pow(base_num, pow_num)
    result = 1
    pow_num.times do
        result = result * base_num
    end
    return result
end

puts pow(5,2)