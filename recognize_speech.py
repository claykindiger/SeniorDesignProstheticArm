import speech_recognition
import sounddevice as sd
print(sd.query_devices()) 

def catchAudio(commands):
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone(device_index=11) as mic:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic, 5, 5)
                text = recognizer.recognize_sphinx(audio)
                text.lower()
                break
        except Exception as e:
        	print(e)
        	print("Please say command again")
        	recognizer = speech_recognition.Recognizer()


    for ind, command in enumerate(commands):
        if command in text:
            print(command.capitalize())
            break
        elif ind == (len(commands) - 1):
            print("Command not found. Word given: " + text)

    return text

commands = ['precision', 'point', 'enemy', 'middle', 'vision']

#catchAudio(commands)

