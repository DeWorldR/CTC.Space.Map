from gtts import gTTS
# สร้าง MP3

text = "ทางไป อาคารวิทยบริการ"
tts = gTTS(text, lang='th')
tts.save('D:\งาน\project\GUIS\speak/button16.mp3')
