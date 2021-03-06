#Quiz options
quizMode = 1               # Mode of this quiz: can be 1,2,3 or 4. Where 3 is word spoken and displayed
repeatUntilCorrect = True  # Repeats questions if answered incorrectly
repeatImmediately = True  # Whether to repeat immediately or when all other questions are asked
randomizeOrder = False      # Whether to ask questions in a random order or as they are given

feedbackPerLetter = False  # Whether to provide feedback for every letter or for every question
readEveryLetter = False    # Whether to read each single letter out loud
contractions = False       # whether this task tests contractions
#Quiz content
quiz = ['a', 'b', 'c']





# Sanity checks to ensure way of questioning makes sense
# ========================================================


if len(max(quiz, key=len)) > 1:
    # If quiz contains words, errors must be repeated immediately and until correct if feedback is provided per letter
    if feedbackPerLetter: 
        repeatUntilCorrect = True
        repeatImmediately = True

    if contractions:            #To enable features dealing with contractions
        readEveryLetter = False
        feedbackPerLetter = True

    # Ensure mode is set for words if words are asked and for single letters if those are asked
    if quizMode == 1:
        quizMode = 3
    if quizMode == 2:
        quizMode = 4
else:
    # Only read every letter of a word if the quiz contains words
    readEveryLetter = False

    if quizMode == 3:
        quizMode = 1
    if quizMode == 4:
        quizMode = 2