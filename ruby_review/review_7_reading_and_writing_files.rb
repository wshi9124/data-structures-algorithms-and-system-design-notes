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
    file.close()
end    

# looping through each line
File.open("review_7.txt", "r") do |file|
    #readlines() returns an array of of all the lines 
    for line in file.readlines()
        puts line
    end
    file.close()
end

# Make sure to close lines (you don't want to leave files open and in memory)
file = File.open("review_7.txt", "r")
puts file.read
file.close()

# Writing Files 
# "a"-Append mode- Write-only, starts at end of file if file exists, otherwise creates a new file for writing.
# warning if we keep runnning it will keep appending same line

=begin
File.open("review_7.txt","a") do |file|
    file.write("\nOscar, Accounting")
end
=end

# "w" - Write-only, overites the entire file or create new file if it doesnt exist (don't uncomment)
=begin
File.open("index.html","w") do |file|
    file.write("<h1>Hello World</h1>")
end
=end

# "r+" - Read-write, you can read and overide lines
=begin
File.open("review_7.txt","r+") do |file|
    file.readline()
    file.write("Overide name, Overide position")
end
=end