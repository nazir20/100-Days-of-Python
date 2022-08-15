#
# @Quiz Project
# @imports
from question_module import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# @looping through the question_data list and retrieving items from it
# the items are going to be passed to the objects created from  the Question class
# new created objects are going to be appended to the question_bank list
for question in question_data:
    q_text = question['question']
    q_answer = question['correct_answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print('You have completed the quiz')
print(f'Your final score was: {quiz_brain.score}/{len(question_bank)}')







