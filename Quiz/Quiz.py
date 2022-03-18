import json




totalAmountOfQuestions = int(0)
amountOfRightAnswers = int(0)


def StartQuiz(quizCategory):
    global totalAmountOfQuestions
    global amountOfRightAnswers


    with open('QuizQuestions.json','r') as file:
        
        allQuizQuestions = json.load(file)
        categoryQuizQuestions = allQuizQuestions[quizCategory]
        totalAmountOfQuestions = len(categoryQuizQuestions)
        

        for question in categoryQuizQuestions :
            exampleAnswers = ""
            
            for possibleAnswer in question["ExampleAnswers"] :
                exampleAnswers += "\u2022 " + possibleAnswer + "\n"

            questionAnswer = input("\n" + question["Question"] + " Answers: \n" + exampleAnswers + "\nYour answer: "
            
            
            )

            if(questionAnswer.lower() == question["Answer"].lower()) :

                print("Good job! Right answer")
                amountOfRightAnswers += 1

            else :
                print("Sorry, wrong answer!")



def ChooseQuizCategory() :

    quizCategory = int(input("\n Which of these categories do you want to play?\n" +
    "1. Sport\n"
    "2. Programming\n"
    "3. Food\n"
    ))

    match quizCategory :
        case 1 :
            StartQuiz("Sport")
        case 2:
            StartQuiz("Programming")
        case 3:
            StartQuiz("Food")



print("Welcome to the Quiz game!")


ChooseQuizCategory()

print("\nYour score was " + str(amountOfRightAnswers) + "/" + str(totalAmountOfQuestions) + ". Hope to see you next time!\n")




