"""
FUNCTION determine_grade(score)
    IF score >= 0 AND score <= 100 THEN
        IF score >= 90 THEN
            RETURN "Excellent"
        ELSE IF score >= 80 THEN
            RETURN "Very Good"
        ELSE IF score >= 70 THEN
            RETURN "Good"
        ELSE IF score >= 50 THEN
            RETURN "Pass"
        ELSE
            RETURN "Fail"
    ELSE
        RETURN "Invalid score"

FUNCTION main()
    PROMPT user to enter their score
    READ score from user
    grade = determine_grade(score)
    DISPLAY grade

    SET random_score to a random integer between 0 and 100
    PRINT "Random score:", random_score
    PRINT "Random score result:", determine_grade(random_score)

IF __name__ EQUALS "__main__" THEN
    CALL main()
"""
import random

def determine_grade(score):
    if score >= 0 and score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 80:
            return "Very Good"
        elif score >= 70:
            return "Good"
        elif score >= 50:
            return "Pass"
        else:
            return "Fail"
    else:
        return "Invalid score"

def main():
    user_score = float(input("Enter your score: "))
    grade = determine_grade(user_score)
    print("Your grade is:", grade)

    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    print("Random score result:", determine_grade(random_score))

if __name__ == "__main__":
    main()
