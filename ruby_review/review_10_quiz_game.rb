class Question
    attr_accessor :question, :answer
    def initialize(q, a)
        @question = q
        @answer = a
    end
end

q1 = "Which letter comes first? \n(a)a\n(b)b\n(c)c"
q2 = "Which letter comes second? \n(a)a\n(b)b\n(c)c"
q3 = "Which letter comes third? \n(a)a\n(b)b\n(c)c"

questions = [
    Question.new(q1, "a"),
    Question.new(q2, "b"),
    Question.new(q3, "c"),
]

def run_test(questionArray)
    answer = ""
    score = 0
    for q in questionArray
        puts q.question
        answer = gets.chomp()
        if answer == q.answer
            score += 1
        end 
    end
    puts "you got #{score} right out of 3"
end

run_test(questions)