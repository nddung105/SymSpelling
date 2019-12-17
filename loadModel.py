from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np
import json
def dictChracter():
    chracViet= ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',
            'm','n','b','v','c','x','z','â','ă','ô','ơ','ê','ư','đ','ẻ','ẽ','è','é','ẹ','ọ','ò',
            'ó','õ','ỏ','ỉ','ĩ','ì','í','ị','ả','ã','à','á','ạ','ụ','ú','ủ','ù','ũ','ẩ','ầ','ấ','ậ',
            'ẫ','ẳ','ặ','ẵ','ằ','ắ','ồ','ố','ổ','ộ','ỗ','ở','ỡ','ớ',
            'ờ','ợ','ể','ế','ề','ễ','ệ','ử','ự','ữ','ứ','ừ','ý','ỳ','ỷ','ỵ','ỹ','end']
    dictChrac = {}
    index=0
    for chractor in chracViet:
        dictChrac[chractor] = index
        index +=1
    return dictChrac
def test(Text,model,dictionary):
  key1=[]
  dictChrac = dictChracter()
  for i in Text:
    if (i == ' '):
      key1.append(94)
    if (i == '0'):
      key1.append(dictChrac['o'])
    if (i == '4'):
      key1.append(dictChrac['a'])
    if (i == '3'):
      key1.append(dictChrac['e'])
    # elif i in chracViet:
    try:
      key1.append(dictChrac[i])
    except:
        a=0
  key1.append(93)
  key1 = sequence.pad_sequences([key1], maxlen=28)
  predictNum=np.argmax(model.predict(key1))
  textReturn = dictionary[str(predictNum)]
  return textReturn
if __name__ == '__main__':
    model = load_model('./model.h5')
    ab = open("/home/dung/Desktop/codeLinhTinh/suaLoiChinhTa/IndexToWords.json","r")
    IndexToWords = json.loads(ab.read())
    print(test("bạn và toi",model,IndexToWords))
    ab.close()

