class QuizBrain:

    def __init__(self, q_list):
        self.list = q_list
        self.index = 0
        self.score = 0
        
    def still_has_questions(self):
        return self.index < len(self.list)
    
    def next_question(self):
        current_q = self.list[self.index]
        self.index += 1
        ans = input(f"Q.{self.index}: {current_q.text}? (True / False): ")
        if current_q.answer.lower() == ans.lower():
            print("You're Correct!")
            self.score += 1
        else:
            print("That's not right")
        print(f"You're current score is: {self.score}/{self.index}")
        print(f"The correct answer is: {current_q.answer}.")
        