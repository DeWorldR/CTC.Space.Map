from gtts import gTTS
# สร้าง MP3

text = "ข้อมูลอาคารวิษณุพัฒนา"
tts = gTTS(text, lang='th')
tts.save('D:/งาน/project/GUIS/speak/button5.mp3')
