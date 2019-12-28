def Riku_response(Schwi_agrees):
    """
    Replicates different portions of movie dialogue depending on input for Schwi_answer.
    See the movie, *No Game No Life Zero* (Ishizuka, 2017) for more dialogue and a spectacular movie.
    """
    print("Will Schwi return Riku's love? Read on to find out!")
    print("------------------------------------")
    Riku_one = 'Riku: "Anything can happen though. Zero or one hundred, it doesn\'t really matter. I mean that\'s why they call it a theory. Would you like me to prove it to you? Question: what are the odds that right here and right now, I would have professed my love to you?" '
    Schwi_one = 'Schwi: "Intent unclear. Estimation: near zero."'
    Riku_marriage_proposal = 'Riku: "Well, you\'re wrong. Will you marry me?" '
    print(Riku_one)
    print(Schwi_one)
    print(Riku_marriage_proposal)
    if Schwi_agrees == False:
        Schwi_declines = 'Schwi: "Cannot ... comprehend. I decline."'
        Riku_cries = 'Riku: "I\'m sorry I got carried away even though I\'m just a virgin! Please don\'t widen the wound!" '
        print(Schwi_declines)
        print(Riku_cries)
    if Schwi_agrees == True:
        Schwi_response = 'Schwi: "Cannot ... comprehend... "'
        Riku_convinces_schwi = 'Riku: "... once I knew the whole story, I fell for you... No matter your past, in the present you\'re with me. And in my future, it\'s where I want you to stay. It\'s called forever. Being with you has made me think that even in a world like this, I want to live. It\'s the only thing I can think of that makes me want to smile. So, will you throw logic out of the window and choose to walk this path with me? That is, as my wife? Schwi?"'
        Schwi_says_yes = 'Schwi: "In every sense, to all rational appearances ... it is absurd. And yet. Let me ... Let me be by your side. With you and you alone Riku, forever."'
        Riku_is_happy = 'Riku: "And I, the same with you."'
        Riku_is_ecstatic = "Riku becomes ecstatic!"
        print(Schwi_response)
        print(Riku_convinces_schwi)
        print(Schwi_says_yes)
        print(Riku_is_happy)
        print(Riku_is_ecstatic)

        
Riku_response(Schwi_agrees=True)
Riku_response(False)
