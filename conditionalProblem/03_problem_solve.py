# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = 155

if score >= 101:
    print("verify the number please its not acceptable:", score)
    exit()

if score >=90:
    print("A Grade")
elif score >= 80:
    print("B Grade")
elif score >=70:
    print("C Grade")
elif score >=60:
    print("D Grade")
else:
    print("F Grade")