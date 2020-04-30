from picamera import PiCamera,Color
import time
import demjson
from pygame import mixer 
from aip import AipBodyAnalysis
from aip import AipSpeech

hand={'One':'数字1','Five':'数字5','Fist':'拳头','Ok':'OK',
      'Prayer':'祈祷','Congratulation':'作揖','Honour':'作别',
      'Heart_single':'比心心','Thumb_up':'点赞','Thumb_down':'Diss',
      'ILY':'我爱你','Palm_up':'掌心向上','Heart_1':'双手比心1',
      'Heart_2':'双手比心2','Heart_3':'双手比心3','Two':'数字2',
      'Three':'数字3','Four':'数字4','Six':'数字6','Seven':'数字7',
      'Eight':'数字8','Nine':'数字9','Rock':'Rock','Insult':'竖中指','Face':'脸'}
# 下面的key要换成自己的 
""" 人体分析 APPID AK SK """
APP_ID = '19676828'
API_KEY = 'GNLabnfhn1quPlaPED5c6YaK'
SECRET_KEY = 'u1xY6WxB1C23nHrLqAuj9ycUTGqZ2lGl'

camera = PiCamera()
client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)


'''cam config'''
camera.resolution = (1280, 720)
camera.annotate_text = "xuehu96 !" #图片上加水印
#camera.annotate_background = Color('blue')
camera.annotate_text_size = 20
camera.annotate_foreground = Color('white')
camera.brightness = 55

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
mixer.init()
while True:
    """1.拍照 """
    camera.start_preview()
    time.sleep(2)
    mixer.music.stop()
    camera.capture('./image.jpg')
    camera.stop_preview()

    image = get_file_content('./image.jpg')

    """ 2.调用手势识别 """
    raw = str(client.gesture(image))
    text = demjson.decode(raw)
    try:
        res = text['result'][0]['classname']
    except:
        print('识别结果：什么也没识别到哦~' )
    else:
        print('识别结果：' + hand[res])

#            time.sleep(3)
        