'''Math Quiz Program
By Grace LeVoir
2 - 19 - 26'''

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

'''Note:
I'm not sure if it's asking for a randomized equation every time,
but we haven't learned how to randomize on Python,
so I am just assuming it can be the same equation.'''


def display_quiz(number1, number2):
    print(f'   {number1}')
    print(f' + {number2}')
    print('---------')
    correct_answer = number1 + number2
    return correct_answer

def check_quiz():
    answer = int(input())
    if answer == correct_answer:
        print('Congratulations! You got it! Keep up the great work!!')
    else:
        print(f'FAIL! Sorry, this answer is incorrect. The correct answer is {correct_answer}.')



correct_answer = display_quiz(220, 456)
check_quiz()