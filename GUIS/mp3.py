from gtts import gTTS
# สร้าง MP3

text = "ทางไป ห้องน้ำ 2"
tts = gTTS(text, lang='th')
tts.save('D:\งาน\project\GUIS\speak/button19.mp3')
