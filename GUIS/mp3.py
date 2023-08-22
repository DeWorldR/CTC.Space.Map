from gtts import gTTS
# สร้าง MP3

text = "ข้อมูลที่ปริ้นเอกสาร"
tts = gTTS(text, lang='th')
tts.save('D:\งาน\project\GUIS\speak/button20.mp3')
