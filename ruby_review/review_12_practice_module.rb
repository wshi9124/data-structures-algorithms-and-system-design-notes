# modules are generally created with a capital letter
module Tools
    def say_hi(name)
        puts "Hello #{name}"
    end

    def say_bye(name)
        puts "Bye #{name}"
    end

end

# include used if module is in same file
include Tools

Tools.say_hi("Willie")
Tools.say_bye("Willie")

