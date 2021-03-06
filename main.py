from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(element["question"], element["correct_answer"]) for element in question_data]

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
