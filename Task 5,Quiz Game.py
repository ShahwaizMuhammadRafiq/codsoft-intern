print("\t\t\t Welcome To The Quiz Game")
print("\t\t Rules")
print("1. Answer each question correctly to earn a point.")
print("2. Type your answers exactly as they should appear (case insensitive).")
print("3. Have fun!")

def quiz():
    score = 0
    
    ques2 = input("Who is Known as the Father Of Computer? ")
    if ques2.lower() == 'charles babbage':
        print("Excellent: Correct Answer")
        score += 1
    else:
        print("Oops: Incorrect Answer")

    ques3 = input("What is the brain of the computer system? ")
    if ques3.lower() == 'cpu':
        print("Excellent: Correct Answer")
        score += 1
    else:
        print("Oops: Incorrect Answer")

    ques4 = input("What does CPU stand for? ")
    if ques4.lower() == 'central processing unit':
        print("Excellent: Correct Answer")
        score += 1
    else:
        print("Oops: Incorrect Answer")

    ques5 = input("What does RAM stand for? ")
    if ques5.lower() == 'random access memory':
        print("Excellent: Correct Answer")
        score += 1
    else:
        print("Oops: Incorrect Answer")

    print("You got", str(score), "question(s) correct")

ch = 'y'
while ch == 'y':
    quiz()
    ch = input("Do You want to play again? (y/n) ")
    
print("Thanks for playing!")

