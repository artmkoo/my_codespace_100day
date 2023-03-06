from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
from data2 import question_data

question_bank = []
for single_question in question_data:
    q_text = single_question['question']
    q_answer = single_question['correct_answer']
    question_object = Question(q_text, q_answer)
    question_bank.append(question_object)

print("*******************")

test_quiz = QuizBrain(question_bank)

#print(test_quiz.check_answer())

while test_quiz.still_has_questions() == True:
    test_quiz.next_question()
    test_quiz.check_answer()
    print(f"score: {test_quiz.score}")

#print(question_bank[5].text, question_bank[5].answer)