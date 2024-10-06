key_map = {"A": "#OOO", "B": "O#OO", "C": "OO#O", "D": "OOO#"}
questions_counts = int(input())
key = input()
page_counts = int(input())


for page in range(page_counts):
    t = 0
    f = 0
    ignored = 0
    
    for question in range(questions_counts):
        student_answer = input()
        correct_answer = key_map[key[question]]

        if student_answer == correct_answer:
            t += 1
        elif student_answer == "OOOO":
            ignored += 1
        else:
            f += 1

    print(t * 3 - f)

