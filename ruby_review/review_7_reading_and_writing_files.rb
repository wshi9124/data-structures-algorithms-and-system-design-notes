#https://stackoverflow.com/questions/3682359/what-are-the-ruby-file-open-modes-and-options for all the modes for opening files 

# You can open files with different modes "r" is read, |file| is storing file that is open inside file variable 
File.open("review_7.txt", "r") do |file|
    #metadata about file
    puts file
    #read entire file
    puts file.read()
    #read by line or read by char
    # puts file.readline()
    #puts file.readchar()
end    

#looping through each line
File.open("review_7.txt", "r") do |file|
    #readlines() returns an array of of all the lines 
    for line in file.readlines()
        puts line
    end

end

#Make sure to close lines (you don't want to leave files open and in memory)
file = File.open("review_7.txt", "r")
puts file.read
file.close()

#Writing Files 
