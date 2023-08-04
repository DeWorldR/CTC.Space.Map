from gtts import gTTS
# สร้าง MP3

text = "ข้อมูลอาคารปฎิบัติการชั้น4"
tts = gTTS(text, lang='th')
tts.save('D:/งาน/project/GUIS/speak/button13.mp3')
