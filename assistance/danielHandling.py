from assistance.action import action
class danielHandling(action):
    def communicate(self, inputText):
        """
        Analyze the request from the user
        """
        lst = inputText.split(" ")
        # If can recoginze the request, proceed further
        if len(lst) > 1: 
            # "Open" command is detected, must be the first or the second word 
            if lst[0] == "open" or lst[1] == "open":
                super().open(inputText)
            # "Close" command is detected, must be the first or the second word    
            elif lst[0] == "close" or lst[1] == "close":
                super().close(inputText) 
            else:
                # Check simple communication
                if not super().simplecommunication(inputText):
                    super().speaker("I don't understand")
                    # TODO: replace by the result found from Google
        else:
            super().speaker("I don't understand")

        
