# Classses are essentially a customized data type
# All starting words in a class should be capitalized   

class BookTour
    attr_accessor :title, :author, :pages
    #initialize- gives it default information (everytime BookTour.new() is called, the initialize method is also getting called)
    def initialize(t="", a="", p=0)
        @title = t
        @author = a
        @pages = p
    end
    # instance method or object methods or class methods 
    def long_book
        if @pages > 600
            return true
        else
            return false
        end
    end

    def add_page
        self.pages += 1
    end

end

book1 = BookTour.new()
book1.title = "Harry Potter"
book1.author = "JK"
book1.pages = 400
book1.add_page
puts book1.pages
puts book1.long_book

book2 = BookTour.new("Lord of the Rings", "JRR", 1000)
puts book2.pages
puts book2.long_book