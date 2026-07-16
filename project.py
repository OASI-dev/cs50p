import sys


def main():
    print("Welcome to the PyQuiz!")
    level = get_level()
    questions = load_questions(level)
    score = run_quiz(questions)
    print(f"Your score is: {score}/{len(questions)}")


def get_level():
    while True:
        choice = input("Select difficulty: 1=easy, 2=medium, 3=hard\n")
        if choice in ["1", "2", "3"]:
            return {"1": "easy", "2": "medium", "3": "hard"}[choice]


def load_questions(level):
    questions = {
        "easy": [
            {"text": "1. Which keyword is used to define a function in Python?\n a) func\n b) define\n c) def\n d) function\n", "answer": "c"},
            {"text": "2. What is the output=> print(5+3)\n a) 53\n b) 8\n c) 15\n d) Error\n", "answer": "b"},
            {"text": "3. Which function is used to display output on the screen?\n a) display()\n b) print()\n c) show()\n d) output()\n", "answer": "b"},
            {"text": "4. Which of the following is a valid variable name?\n a) 2name\n b) my-name\n c) my_name\n d) class\n", "answer": "c"},
            {"text": "5. what is the output=> print('Hello')\n a) Hello\n b) 'Hello'\n c) Error\n d) Nothing\n", "answer": "a"},
            {"text": "6. Which symbol is used to write a comment in Python?\n a) //\n b) #\n c) /* */\n d) --\n", "answer": "b"},
            {"text": "7. What is the output=>\nx = 10\nprint(x)\n a) x\n b) 10\n c) Error\n d) Nothing\n", "answer": "b"},
            {"text": "8. Which data type is used to store text?\n a) int\n b) float\n c) str\n d) bool\n", "answer": "c"},
            {"text": "9. What is the output=> print(len('Python'))?\n a) 5\n b) 6\n c) 7\n d) Error\n", "answer": "b"},
            {"text": "10. Which loop is commonly used to iterate over a list?\n a) repeat\n b) loop\n c) for\n d) do\n", "answer": "c"},
        ],
        "medium": [
            {"text": "1. What is the output=>\nx = [1, 2, 3]\nprint(x[-2])\n a) 1\n b) 2\n c) 3\n d) Error\n", "answer": "b"},
            {"text": "2. What is the output=>\nx = 'Python'\nprint(x[1:4])\n a) Pyt\n b) yth\n c) tho\n d) ytho\n", "answer": "b"},
            {"text": "3. What will this code print?=>\na = [1, 2]\nb = a\nb.append(3)\nprint(a)\n a) [1, 2]\n b) [1, 2, 3]\n c) [3]\n d) Error\n", "answer": "b"},
            {"text": "4. Which of the following is not a valid Python data type?\n a) List\n b) Dictionary\n c) Array\n d) Tuple\n", "answer": "c"},
            {"text": "5. What is the output=>\nprint(2 ** 3 ** 2)\n a) 64\n b) 512\n c) 36\n d) 256\n", "answer": "b"},
            {"text": "6. What is the output=>\nx = {1, 2, 2, 3}\nprint(len(x))\n a) 4\n b) 3\n c) 2\n d) Error\n", "answer": "b"},
            {"text": "7. Which keyword is used to handle exceptions?\n a) catch\n b) error\n c) finally\n d) except\n", "answer": "d"},
            {"text": "8. print('7' + '3')\n a) 10\n b) 21\n c) 73\n d) Error\n", "answer": "c"},
            {"text": "9. What is the output=>\nfor i in range(2 ,6):\n\tprint(i, end=' ')\n a) 2 3 4 5\n b) 2 3 4 5 6\n c) 1 2 3 4 5\n d) 3 4 5 6\n", "answer": "a"},
            {"text": "10. What is the output=>\nx = [10, 20, 30]\nx.pop()\nprint(x)\n a) [10, 20, 30]\n b) [10, 20]\n c) [20, 30]\n d) Error\n", "answer": "b"},
        ],
        "hard": [
            {"text": "1. What is the output=>\nx = [1, 2, 3]\ny = x[:]\ny.append(4)\nprint(x)\n a) [1, 2, 3, 4]\n b) [1, 2, 3]\n c) [4]\n d) Error\n", "answer": "b"},
            {"text": "2. What is the output=>\nprint(type({}))\n a) <class 'list'>\n b) <class 'dict'>\n c) <class 'set'>\n d) <class 'tuple'>\n", "answer": "b"},
            {"text": "3. What is the output=>\nprint(3 * 'Hi')\n a) HiHiHi\n b) 3Hi\n c) Hi3\n d) Error\n", "answer": "a"},
            {"text": "4. What is the output=>\na = [10, 20,30]\nprint(a[-2])\n a) 20\n b) 30\n c) 10\n d) Error\n", "answer": "a"},
            {"text": "5. Which statement is correct?\n a) Tuples are mutable\n b) Lists are immutable\n c) Sets do not allow duplicate values\n d) Dictionaries cannot store strings\n", "answer": "c"},
            {"text": "6. What is the output=>\nx = [1, 2]\ny = x\nx = x + [3]\nprint(y)\n a) [1, 2, 3]\n b) [3]\n c) [1, 2]\n d) Error\n", "answer": "c"},
            {"text": "7. What is the output=>\nprint(bool(\"\"))\n a) True\n b) False\n c) None\n d) Error\n", "answer": "b"},
            {"text": "8. What is the output=>\nprint(list(range(1, 6, 2)))\n a) [1, 2, 3, 4, 5]\n b) [2, 4, 6]\n c) [1, 3, 5]\n d) [1, 3]\n", "answer": "c"},
            {"text": "9. What is the output=>\nx = {1, 2, 3}\nx.add(2)\nprint(len(x))\n a) 4\n b) 2\n c) 3\n d) 1\n", "answer": "c"},
            {"text": "10. What is the output=>def func(a, b=5):\n\treturn a + b\n\nprint(func(3))\n a) 3\n b) 5\n c) 8\n d) Error\n", "answer": "c"},
        ],
    }
    return questions[level]


def check_answer(question, user_answer):
    return user_answer.strip().lower() == question["answer"]


def run_quiz(questions):
    score = 0
    for question in questions:
        while True:
            user_answer = input(question["text"])
            if user_answer.strip().lower() in ["a", "b", "c", "d"]:
                break
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! Correct answer is {question['answer']}")
    return score


if __name__ == "__main__":
    main()
