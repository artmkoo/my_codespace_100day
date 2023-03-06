class QuizBrain:
    """initialise the question_number to 0 and initialise question_list to an input"""
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    
    def still_has_questions(self):
        "check that game still has questions"
        self.number_of_questions = len(self.questions_list)
        return self.question_number <= self.number_of_questions

    def next_question(self):
        text_question_form_list = self.questions_list[self.question_number].text
        self.answer_question_from_list = self.questions_list[self.question_number].answer
        self.question_number +=1
        self.user_answer = input (f"Q.{self.question_number}: {text_question_form_list}. (True/False)?")

    def check_answer(self):
        
        if self.user_answer == self.answer_question_from_list:
            print("correct aswer")
            self.score +=1
        else:
            print("incorrect aswer")
        #print(self.answer_question_from_list)


#quiz_test = QuizBrain()
#quiz_test.next_question()