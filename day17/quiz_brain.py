class QuizBrain:
    """initialise the question_number to 0 and initialise question_list to an input"""
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
    
    def next_question(self):
        text_question_form_list = self.questions_list[self.question_number].text
        self.user_answer = input (f"Q{self.question_number} {text_question_form_list}. (True/False)?")

#quiz_test = QuizBrain()
#quiz_test.next_question()