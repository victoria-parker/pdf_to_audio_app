import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('networking_for_introverts.pdf', 'rb'))
# print(pdfreader.metadata.title)
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ').replace(';', ',')

speaker.save_to_file(clean_text, 'networking_for_introverts.mp3')
speaker.runAndWait()

speaker.stop()