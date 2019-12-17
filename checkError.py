def wordError(word,dictionarry):
  try:
    a = dictionarry[word.lower()]
    return True
  except:
    k = 0
    m = 0 
    for index in range(len(word)):
      if (64<ord(word[index])<91):   #  Nếu tất cả các ký tự trong từ đều viết hoa 
        k += 1  
      elif(47<ord(word[index])<58):
        m += 1                                               #  thì đó là từ viết tắt -> đúng chính tả
    if (k == len(word)):
      return True
    elif (m == len(word)):
      return True
    else:
      return False
def notJ(text,dictionarry):
    text2 = text
    for i in range(len(text2)):
      # if (text2[i] == 'j'):
      #   text2=text2.replace('j','i')
      if (text2[i] == '4'):
        text2=text2.replace('4','a')
      if (text2[i] == '3'):
        text2=text2.replace('3','e')
      if (text2[i] == '0'):
        text2 = text2.replace('0','o')
    if('oo' in text2):
      text2 = text2.replace('oo','ô')
    if('aa' in text2):
      text2 = text2.replace('aa','â')
    if('dd' in text2):
      text2 = text2.replace('dd',"đ")
    if('ee' in text2):
      text2 = text2.replace('ee',"ê")
    if('ow' in text2):
      text2 = text2.replace('ow',"ơ")
    if('uw' in text2):
      text2 = text2.replace('uw',"ư")
    if('uow' in text2):
      text2 = text2.replace('uow',"ươ")
    if('aw' in text2):
      text2 = text2.replace('aw',"ă")
    if('af' in text2):
      text2 = text2.replace('af',"à")
    if('if' in text2):
      text2 = text2.replace('if',"ì")
    if('uf' in text2):
      text2 = text2.replace('uf',"ù")
    if('ef' in text2):
      text2 = text2.replace('ef',"è")
    if('of' in text2):
      text2 = text2.replace('of',"ò")
    if('ôf' in text2):
      text2 = text2.replace('ôf',"ồ")
    if('êf' in text2):
      text2 = text2.replace('êf',"ề")
    if('ơf' in text2):
      text2 = text2.replace('ơf',"ờ")
    if('ăf' in text2):
      text2 = text2.replace('ăf',"ằ")
    if('âf' in text2):
      text2 = text2.replace('âf',"ấ")
    if('as' in text2):
      text2 = text2.replace('as',"á")
    if('is' in text2):
      text2 = text2.replace('is',"í")
    if('us' in text2):
      text2 = text2.replace('us',"ú")
    if('es' in text2):
      text2 = text2.replace('es',"é")
    if('os' in text2):
      text2 = text2.replace('os',"ó")
    if('ôs' in text2):
      text2 = text2.replace('ôs',"ố")
    if('ês' in text2):
      text2 = text2.replace('ês',"ế")
    if('ơs' in text2):
      text2 = text2.replace('ơs',"ớ")
    if('ăs' in text2):
      text2 = text2.replace('ăs',"ắ")
    if('âs' in text2):
      text2 = text2.replace('âs',"ấ")
    if('aj' in text2):
      text2 = text2.replace('aj',"ạ")
    if('ij' in text2):
      text2 = text2.replace('ij',"ị")
    if('uj' in text2):
      text2 = text2.replace('uj',"ụ")
    if('ej' in text2):
      text2 = text2.replace('ej',"ẹ")
    if('oj' in text2):
      text2 = text2.replace('oj',"ọ")
    if('ôj' in text2):
      text2 = text2.replace('ôj',"ộ")
    if('êj' in text2):
      text2 = text2.replace('êj',"ệ")
    if('ơj' in text2):
      text2 = text2.replace('ơj',"ợ")
    if('ăj' in text2):
      text2 = text2.replace('ăj',"ặ")
    if('âj' in text2):
      text2 = text2.replace('âj',"ậ")
    if('ax' in text2):
      text2 = text2.replace('ax',"ã")
    if('ix' in text2):
      text2 = text2.replace('ix',"ĩ")
    if('ux' in text2):
      text2 = text2.replace('ux',"ũ")
    if('ex' in text2):
      text2 = text2.replace('ex',"ẽ")
    if('ox' in text2):
      text2 = text2.replace('ox',"õ")
    if('ôx' in text2):
      text2 = text2.replace('ôx',"ỗ")
    if('êx' in text2):
      text2 = text2.replace('êx',"ễ")
    if('ơx' in text2):
      text2 = text2.replace('ơx',"ỡ")
    if('ăx' in text2):
      text2 = text2.replace('ăx',"ẵ")
    if('âx' in text2):
      text2 = text2.replace('âx',"ẫ")
    if('ar' in text2):
      text2 = text2.replace('ar',"ả")
    if('ir' in text2):
      text2 = text2.replace('ir',"ỉ")
    if('ur' in text2):
      text2 = text2.replace('ur',"ủ")
    if('er' in text2):
      text2 = text2.replace('er',"ẻ")
    if('or' in text2):
      text2 = text2.replace('or',"ỏ")
    if('ôr' in text2):
      text2 = text2.replace('ôr',"ổ")
    if('êr' in text2):
      text2 = text2.replace('êr',"ể")
    if('ơr' in text2):
      text2 = text2.replace('ơr',"ở")
    if('ăr' in text2):
      text2 = text2.replace('ăr',"ẩ")
    for i in range(len(text2)):
        if (text2[i] == 'j'):
          text2=text2.replace('j','i')
    if wordError(text2,dictionarry) == True:
        # print(text)
        return text2
    else:
      for i in range(len(text2)):
          if (text2[i] == 'q'):
            text2 = text2.replace('q','g')
      if wordError(text2,dictionarry) == True:
          # print(text)
          return text2
      else :
        for i in range(len(text2)):
          if (text2[i] == 'k'):
            text2 = text2.replace('k','h')
        if wordError(text2,dictionarry) == True:
          # print(text)
          return text2
        else:
          return text2
def fixAJ(text,dictionarry):
  dem = 0
  if (text == 'j'):
  
    text="gì"
    # print(text)
    return text
  elif (text == 'đc'):
  
    text="được"
    # print(text)
    return text
  elif (text == 'đk'):
  
    text="được"
    # print(text)
    return text
  elif (text == 'vs'):
  
    text="với"
    # print(text)
    return text
  elif (text == 'dc'):
  
    text="được"
    # print(text)
    return text
  elif (text == 'nc'):
  
    text="nước"
    # print(text)
    return text
  else:
    text1 = text
    for i in range(len(text1)):
      if (text1[i] == 'j'):
        text1=text1.replace('j','i')
      if (text1[i] == '4'):
        text1=text1.replace('4','a')
      if (text1[i] == '3'):
        text1=text1.replace('3','e')
      if (text1[i] == '0'):
        text1 = text1.replace('0','o')
    if('oo' in text1):
      text1 = text1.replace('oo','ô')
    if('aa' in text1):
      text1 = text1.replace('aa','â')
    if('dd' in text1):
      text1 = text1.replace('dd',"đ")
    if('ee' in text1):
      text1 = text1.replace('ee',"ê")
    if('ow' in text1):
      text1 = text1.replace('ow',"ơ")
    if('uw' in text1):
      text1 = text1.replace('uw',"ư")
    if('uow' in text1):
      text1 = text1.replace('uow',"ươ")
    if('aw' in text1):
      text1 = text1.replace('aw',"ă")
    if('af' in text1):
      text1 = text1.replace('af',"à")
    if('if' in text1):
      text1 = text1.replace('if',"ì")
    if('uf' in text1):
      text1 = text1.replace('uf',"ù")
    if('ef' in text1):
      text1 = text1.replace('ef',"è")
    if('of' in text1):
      text1 = text1.replace('of',"ò")
    if('ôf' in text1):
      text1 = text1.replace('ôf',"ồ")
    if('êf' in text1):
      text1 = text1.replace('êf',"ề")
    if('ơf' in text1):
      text1 = text1.replace('ơf',"ờ")
    if('ăf' in text1):
      text1 = text1.replace('ăf',"ằ")
    if('âf' in text1):
      text1 = text1.replace('âf',"ấ")
    if('as' in text1):
      text1 = text1.replace('as',"á")
    if('is' in text1):
      text1 = text1.replace('is',"í")
    if('us' in text1):
      text1 = text1.replace('us',"ú")
    if('es' in text1):
      text1 = text1.replace('es',"é")
    if('os' in text1):
      text1 = text1.replace('os',"ó")
    if('ôs' in text1):
      text1 = text1.replace('ôs',"ố")
    if('ês' in text1):
      text1 = text1.replace('ês',"ế")
    if('ơs' in text1):
      text1 = text1.replace('ơs',"ớ")
    if('ăs' in text1):
      text1 = text1.replace('ăs',"ắ")
    if('âs' in text1):
      text1 = text1.replace('âs',"ấ")
    if('ix' in text1):
      text1 = text1.replace('ix',"ĩ")
    if('ux' in text1):
      text1 = text1.replace('ux',"ũ")
    if('ex' in text1):
      text1 = text1.replace('ex',"ẽ")
    if('ox' in text1):
      text1 = text1.replace('ox',"õ")
    if('ôx' in text1):
      text1 = text1.replace('ôx',"ỗ")
    if('êx' in text1):
      text1 = text1.replace('êx',"ễ")
    if('ơx' in text1):
      text1 = text1.replace('ơx',"ỡ")
    if('ăx' in text1):
      text1 = text1.replace('ăx',"ẵ")
    if('âx' in text1):
      text1 = text1.replace('âx',"ẫ")
    if('ar' in text1):
      text1 = text1.replace('ar',"ả")
    if('ir' in text1):
      text1 = text1.replace('ir',"ỉ")
    if('ur' in text1):
      text1 = text1.replace('ur',"ủ")
    if('er' in text1):
      text1 = text1.replace('er',"ẻ")
    if('or' in text1):
      text1 = text1.replace('or',"ỏ")
    if('ôr' in text1):
      text1 = text1.replace('ôr',"ổ")
    if('êr' in text1):
      text1 = text1.replace('êr',"ể")
    if('ơr' in text1):
      text1 = text1.replace('ơr',"ở")
    if('ăr' in text1):
      text1 = text1.replace('ăr',"ẩ")
    if wordError(text1,dictionarry) == True:
        # print(text)
        return text1
    else:
      for i in range(len(text1)):
          if (text1[i] == 'q'):
            text1 = text1.replace('q','g')
      if wordError(text1,dictionarry) == True:
          # print(text)
          return text1
      else :
        for i in range(len(text1)):
          if (text1[i] == 'k'):
            text1 = text1.replace('k','h')
        if wordError(text1,dictionarry) == True:
          # print(text)
          return text1
        else:
          text1 = notJ(text,dictionarry)   
          if wordError(text1,dictionarry) == True:
          # print(text)
            return text1
          else:
            return text1
  # return text
def printError(dataTxt,dictionarry,dataTest,):
  dataTxt = dataTxt.split("\n")[:1000]
  # lenS = dataTest.split("\n")
  # print(len(lenS))
  dataTest = dataTest.split("\n")[:1000]
  de = 0
  sai = 0
  cong = 0
  for index in range(len(dataTxt)):
    line = dataTxt[index]
    line =re.split(r'\W+', line)
    line2 = dataTest[index]
    line2 =re.split(r'\W+', line2)
    for indexWord in range(len(line)-2):
      indexWord =indexWord +2
      if wordError(line[indexWord],dictionarry) == False:
        sai +=1
        # print(line[indexWord])
        # if fixAJ(line[indexWord],dictionarry) == 1:
        text=fixAJ(line[indexWord],dictionarry)
        text1=notJ(line[indexWord],dictionarry)
        testData = [test(line[indexWord-2]+" "+line[indexWord-1]+" "+line[indexWord])]
        testData = sequence.pad_sequences(testData , maxlen=28)
        predictNum=np.argmax(model.predict(testData))
        predictText=''
        for key,value in dictValue.items():
          if value == predictNum:
            predictText = key  
        if text.lower() == line2[indexWord].lower():
          de += 1

        elif (predictText == line2[indexWord].lower()):
          de += 1
  print(de)
  print(sai)
  print(de/sai)