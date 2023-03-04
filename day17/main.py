from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for single_question in question_data:
    q_text = single_question['text']
    q_answer = single_question['answer']
    question_object = Question(q_text, q_answer)
    question_bank.append(question_object)

print("*******************")

test_quiz = QuizBrain(question_bank)
test_quiz.next_question()

#print(question_bank[5].text, question_bank[5].answer)