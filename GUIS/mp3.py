from gtts import gTTS
# สร้าง MP3

text = "ทางไป อาคารสำนักงานอาชีวศึกษาเชียงราย/ระบบทวิภาคี"
tts = gTTS(text, lang='th')
tts.save('D:\งาน\project\GUIS\Image\Qrcode/button10.mp3')
