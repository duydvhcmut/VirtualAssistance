from assistance.danielHandling import danielHandling

ai = danielHandling()
botname = "daniel"
while True:
    inputspeech = ai.getInputSpeech
    # Input command must have the bot's name in the beginning
    if inputspeech == botname:
        # Loop until the real command is received
        while inputspeech == botname:
            ai.speaker("How can I help you?")
            # After the this, the command without the bot's name is accepted
            inputspeech = ai.getInputSpeech
            if inputspeech != "..." and inputspeech != botname and inputspeech != "close":
                ai.communicate(inputspeech)
        if inputspeech == "close":
            ai.speaker("See you next time!")
            break
    # Only activate if bot's name is called in the first word
    elif inputspeech != "..." and inputspeech[0:6] == botname:
        if inputspeech == botname + " close":
            ai.speaker("See you next time!")
            break
        # Run the command
        ai.communicate(inputspeech)