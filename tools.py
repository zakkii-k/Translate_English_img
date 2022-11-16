import sys
from PIL import Image
import pyocr
import pyocr.builders
from nltk.tokenize import sent_tokenize
import deepl
import tqdm

def img_to_str(filename):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]
    # print("Will use tool '%s'" % (tool.get_name()))

    txt = tool.image_to_string(
        #文字認識対象の画像image.pngを用意する
        Image.open(filename),
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    #print( txt )
    return txt
    
def divide_sentence(text): #文章を1文ずつ改行する．
    a = sent_tokenize(text)
    #print(a)
    ans = ""
    for i in a:
        ans += i
        ans += "\n"
    return ans

    

def translate(text):
    translator = deepl.Translator("hogehoge") #DeepLAPIの認証コードを入力
    result = translator.translate_text(text, target_lang="JA") 
    translated_text = result.text
    return translated_text

def to_str(l): #リストで受け取った単語を繋げて文にする．
    s = ""
    set_L = set(range(119860, 119886))
    set_S = set(range(119886, 119912))

    for i in tqdm.tqdm(range(len(l))):
        tmp = list(map(ord, list(l[i])))
        if(len(set(tmp)&set_L) > 0):
            tmp_s = ""
            for j in range(len(tmp)):
                if(tmp[j] >= 119860 and tmp[j] < 119886):
                    tmp[j] = tmp[j]-119795
                tmp_s += chr(tmp[j])
            l[i] = tmp_s
        elif(len(set(tmp)&set_S) > 0):
            tmp_s = ""
            for j in range(len(tmp)):
                if(tmp[j] >= 119886 and tmp[j] < 119912):
                    tmp[j] = tmp[j]-119789
                tmp_s += chr(tmp[j])
            l[i] = tmp_s
        if(l[i][-1] == "-" and "state" not in l[i] and "of" not in l[i]):
            l[i] = l[i][:-1]
            s += l[i]
            continue
        s += l[i]
        s += " "
    return s
