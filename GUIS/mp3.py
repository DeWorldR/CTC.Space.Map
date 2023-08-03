from gtts import gTTS
# สร้าง MP3

text = "กรุณาพิมพ์สิ่งที่ต้องการค้นหา"
tts = gTTS(text, lang='th')
tts.save('D:/งาน/project/GUIS/speak/button4.mp3')
