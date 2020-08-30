import pyttsx3
import speech_recognition as sr
class ioinput:
    def speaker(self, inputText):
        """
        This function translate text to speech
        """
        speaker = pyttsx3.init()
        print(f"Bot: {inputText}")
        speaker.say(inputText)
        speaker.runAndWait()
    @property
    def getInputSpeech(self):
        """
        Get the input speech of human and translate it to text
        """
        inputspeech = sr.Recognizer()
        with sr.Microphone() as source:
            print("Me: ",end="")
            audio_data = inputspeech.listen(source, phrase_time_limit=5)
            try:
                text = inputspeech.recognize_google(audio_data)
                text = text.lower()
                print(text)
                return text
            except:
                print("...")
                return "..."
