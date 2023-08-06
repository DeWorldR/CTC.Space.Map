from gtts import gTTS
# สร้าง MP3

text = "ทางไปอาคารปฎิบัติการอเนกประสงค์"
tts = gTTS(text, lang='th')
tts.save('D:\งาน\project\GUIS\Maps\index/button9.mp3')
