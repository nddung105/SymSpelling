from keras.layers import Dropout,Conv1D,MaxPooling1D
from keras.models import load_model
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding,TimeDistributed
from keras.layers import LSTM,Activation
chracViet= ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',
            'm','n','b','v','c','x','z','â','ă','ô','ơ','ê','ư','đ','ẻ','ẽ','è','é','ẹ','ọ','ò',
            'ó','õ','ỏ','ỉ','ĩ','ì','í','ị','ả','ã','à','á','ạ','ụ','ú','ủ','ù','ũ','ẩ','ầ','ấ','ậ',
            'ẫ','ẳ','ặ','ẵ','ằ','ắ','ồ','ố','ổ','ộ','ỗ','ở','ỡ','ớ',
            'ờ','ợ','ể','ế','ề','ễ','ệ','ử','ự','ữ','ứ','ừ','ý','ỳ','ỷ','ỵ','ỹ','end']
dictChrac = {}
# print(len(chracViet))
index=0
for chractor in chracViet:
  dictChrac[chractor] = index
  index +=1
print(dictChrac['end'])
ab = open("/content/gdrive/My Drive/wordToIn1.json","r") #  Share dữ liệu từ bộ dữ liệu toán tin về drive của mình
dictionary = json.loads(ab.read())
abc = open("/content/gdrive/My Drive/dictError1.json","r")
dataTrain = json.loads(abc.read())
arrayX = []
arrayY = []
dictValue = {}
indexValue = 6374
sample = 0
for key,value in dataTrain.items():
  sample += 1
  key1=[]
  for i in key:
    if (i == ' '):
      key1.append(94)
    if (i == '0'):
      key1.append(dictChrac['o'])
    if (i == '4'):
      key1.append(dictChrac['a'])
    if (i == '3'):
      key1.append(dictChrac['e'])
    elif i in chracViet:
      key1.append(dictChrac[i])
  key1.append(93)
  arrayX.append(key1)
  arrayY.append(dictionary[value])
# arrayY1 = np.array(arrayY).reshape((984,1,1))
arrayYTrain = np.zeros((sample,indexValue))
for i in range(len(arrayY)):
   arrayYTrain[i][arrayY[i]] = 1
arrayX = sequence.pad_sequences(arrayX, maxlen=25)
print(indexValue)
kernel_size = 5
filters = 64
pool_size = 4
# model = load_model('/content/gdrive/My Drive/modelSpell.h5')
model = Sequential()
model.add(Embedding(input_dim=95,input_length=25,output_dim=128))
model.add(Dropout(0.25))
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
model.add(MaxPooling1D(pool_size=pool_size))
model.add(LSTM(128,return_sequences=False,activation='tanh',dropout=0.2, recurrent_dropout=0.2))
# model.add(LSTM(28,return_sequences=True))
# model.add(LSTM(28,return_sequences=False))
# model.add(Dense(128, activation='sigmoid'))
# model.add(Dense(128, activation='sigmoid'))
model.add(Dense(indexValue, activation='sigmoid'))
# model.add(TimeDistributed(Dense(indexValue)))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.summary()
model.fit(arrayX, arrayYTrain,batch_size=64,epochs=10)
abc.close()
model.save("/content/gdrive/My Drive/model.h5")