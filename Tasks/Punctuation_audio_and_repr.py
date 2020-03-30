#Quiz options
quizMode = 4               # Mode of this quiz: can be 1,2,3 or 4. Where 3 is word spoken and displayed
repeatUntilCorrect = True  # Repeats questions if answered incorrectly
repeatImmediately = False  # Whether to repeat immediately or when all other questions are asked
randomizeOrder = True      # Whether to ask questions in a random order or as they are given

feedbackPerLetter = True  # Whether to provide feedback for every letter or for every question
readEveryLetter = True     # Whether to read each single letter out loud
contractions = False       # whether this task tests contractions

#Quiz content
quiz = ['capital indicator symbol', 'capital indicator word', 'capital indicator passage', 'italic indicator symbol', 'italic indicator word', 'italic indicator passage', 'bold indicator simbol', bold indicator word', 'bold indicator passage', 'underline indicator symbol', 'underline indicator word', 'underline indicator passage', 'comma', 'period', 'apostrophe', 'colon', 'dash', 'exclamation mark', 'question mark', 'semicolon', 'asterisk', 'forward slash', 'backward slash', 'opening single quotation',  'closing single quotation', 'opening double quotation', 'closing double quotation', 'opening round parenthesis', 'closing round parenthesis', 'plus', 'minus', 'multiplication cross', 'multiplication dot', 'division', 'equals', 'euro',  'dollar', 'pound', 'percentage', 'degree', 'hashtag', 'ampersand', 'superscript indicator', 'subscript indicator', 'bullet point']

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
