import tkinter as tk
import pyttsx3

def text_to_speech_function():
    text = entry.get()
    if not text.strip():
        return
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # slower rate for clarity
    engine.say(text)
    engine.runAndWait()

# Create GUI window
window = tk.Tk()
window.title("Text to Speech")
window.geometry("400x200")

# Label
label = tk.Label(window, text="Enter text to speak:")
label.pack(pady=10)

# Entry field
entry = tk.Entry(window, width=40)
entry.pack(pady=5)

# Speak button
speak_button = tk.Button(window, text="Speak", command=text_to_speech_function)
speak_button.pack(pady=10)

# Run the GUI loop
window.mainloop()
