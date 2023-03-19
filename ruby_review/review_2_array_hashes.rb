#Arrays- can store any data type and can store different data types in same array
food = Array["sushi", "pizza", false , 1]
food[1] = "chicken"
print food 
puts "\n"
# you can initialize new array by:
friends = Array.new
friends.append("yes")
friends[2] = 4
print friends 
puts "\n"
# .length() .includes? .reverse() .sort()
# hashes key => value (keys have to be unique) : same as ""
states = {
    :Pennsylvania => "PA",
    "New York" => "NY",
    2 => "number"
}
puts states[:Pennsylvania]
puts states["New York"]
