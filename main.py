import shutil
import argparse
import pandas as pd
from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np
import json
import loadModel
import checkError
import re
import nltk
def parse_args():
    parser = argparse.ArgumentParser(description="Correcting texts in an input file")
    parser.add_argument("input_file", type=str, help="Path to the input text file")
    parser.add_argument("output_file", type=str, help="Path to the output corrected text file")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    model = load_model('./model.h5')
    ab = open("./IndexToWords.json","r")
    IndexToWords = json.loads(ab.read())
    arguments = parse_args()
    input_file = arguments.input_file
    output_file = arguments.output_file
    inputFile = open(input_file,'r')
    textInput = inputFile.read().split("\n")
    ac = open("./checkError.json","r")
    dictCheck = json.loads(ac.read())
    textOut = []
    for indexLine in range(len(textInput)):
      line = textInput[indexLine]
      line = line.split()
      for indexWord in range(len(line)):
        check = 0

        for i in line[indexWord]:
          if ( 32<ord(i)<48 or 57<ord(i)<65 or 90<ord(i)<97 or 127<ord(i)<122):
            check = 1
        if (check != 1):
          text = checkError.fixAJ(line[indexWord],dictCheck)
          if checkError.wordError(text,dictCheck)==True:
            line[indexWord] = text
          # print(line[indexWord])
          elif(checkError.wordError(line[indexWord],dictCheck)==False):
            if (indexWord == 0):
              key = line[indexWord]+" " +line[indexWord+1]
              line[indexWord] = loadModel.test(key,model,IndexToWords)
            elif( indexWord == 1):
              key = line[indexWord-1] + " " +line[indexWord]
              line[indexWord] = loadModel.test(key,model,IndexToWords)
            # elif(indexWord == len(line)):
            #   key = line[indexWord-2] + " " +line[indexWord-1] + " " +line[indexWord]
            #   line[indexWord] = loadModel.test(key,model,IndexToWords)
            else:
              key = line[indexWord-2] + " " +line[indexWord-1] + " " +line[indexWord]
              line[indexWord] = loadModel.test(key,model,IndexToWords)
      line = " ".join(line)
      textOut.append(line)
    textOut="\n".join(textOut)
    outputFile = open(output_file,"w")
    outputFile.write(textOut)
    ab.close()
    ac.close()
    inputFile.close()
    outputFile.close()
