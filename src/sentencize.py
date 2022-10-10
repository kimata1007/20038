#関数の作成
#ファイルと列番号を受け取る。
import sys


def sentencize(file_name,row):
    with open(file_name) as f: 
        sentence = f.read() #ファイルを文字列として読み込み
    sentence = sentence.replace("\n"," ") #文字列の改行を空白に置換する
    sentence = sentence.split("  ") #"  "で区切り、リストにする。
    for sen in sentence[1:-1]:
        sen = sen.split(" ")
        sentence = [ c for num,c in enumerate(sen) if num % 4 == row]
        sentence = " ".join(sentence)
        #if sentence == "-DOCSTART-" or sentence == "-X-" or sentence == "O":
        #    sentence 
        print(sentence)

x = sys.argv[1]
y = sys.argv[2]
sentencize(str(x),int(y))
