#Inheritance allows us to extend the functionality of one class to another class
class Chef
    def make_chicken
        puts "chef makes chicken"
    end

    def make_salad
        puts "chef makes salad"
    end

    def make_special_dish
        puts "chef makes ribs"
    end
end

# < Chef makes Itlian chef inherit all the methods of chef 
class ItalianChef < Chef
    def make_special_dish
        puts "chef makes pasta"
    end
end

chef = Chef.new()
chef.make_chicken
chef.make_special_dish

italian_chef = ItalianChef.new()
italian_chef.make_chicken
italian_chef.make_special_dish