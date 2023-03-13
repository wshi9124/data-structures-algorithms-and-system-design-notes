class Book
    attr_accessor :title, :author, :pages 
end

#object
book1 = Book.new()
book1.title = "Harry Potter"
book1.author = "JK Rowling"
book1.pages = 400

puts book1.pages
puts book1.title