# Case Expression- Instead of if day == "mon" etc do when
def get_workday_name(day)
    day_name = ""
    case day
    when "mon"
        day_name = "Monday"
    when "tue"
        day_name = "Tuesday"
    when "wed"
        day_name = "Wednesday"
    when "thur"
        day_name = "Thursday"
    when "fri"
        day_name = "Friday"
    else
        day_name = "Invalid Abbreviation"
    end
    return day_name
end

puts get_workday_name("mon")

# while loop similar as python while loop
index = 1
while index <= 5
    puts index
    index += 1
end

#guessing game using while loop
