# Modules are containers where we can store groups of methods
# Naming convention- Capitalize 
# use only "include" if module is in same file
# use "require_relative" and "include" if module is in different file

require_relative "review_12_practice_module.rb" 
include Tools

say_hi("Willie")
say_bye("Willie")