from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_list = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    new_question = Question(text, answer)
    questions_list.append(new_question)

quiz = QuizBrain(questions_list)

while quiz.still_has_questions():
    quiz.next_question()
print("Quiz completed!")
print(f"You're final score was: {quiz.score}/{quiz.index}")