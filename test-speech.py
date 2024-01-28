import speech_recognition

recognizer = speech_recognition.Recognizer()
try:
    with speech_recognition.Microphone() as mic:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic, 3, 3)
        text = recognizer.recognize_sphinx(audio)
        text.lower()
        
except Exception as e:
    print("Please say command again")
    recognizer = speech_recognition.Recognizer()
        

commands = ['precision', 'point', 'enemy', 'middle', 'vision']

for ind, command in enumerate(commands):
    if command in text:
        print(command.capitalize())
        break
    elif ind == (len(commands) - 1):
		#if not text:
			#return 'vision'
        print("Command not found. Word given: " + text)

