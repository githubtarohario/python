#-------------------------------------
#このブログラムは<doc  ~  /doc>
#を抜き出しデータベースに入れるプログラム
#----------------------------------------
import sqlite3

def db(title,contents):
    # D:\work\wikiextractor>
    #conn = sqlite3.connect(r'C:\Users\User\iCloudDrive\wikipedia.db')
    conn = sqlite3.connect(r'D:\work\wikiextractor\wikipedia.db')


    c = conn.cursor()
    #d=contents.strip("'")
    #d=contents.strip("\")
    #d=contents.strip("\\")
    #sql = "INSERT INTO graph(id,date) VALUES('1',?)"
    #connector.execute(sql, [newtitle])  # 追記部分をご覧ください
    sql='insert into wikipedia(title,contents) values(?,?)'
    #print(sql)
    c.execute(sql,[title,contents])
    conn.commit()
    conn.close()
def wikiwrite(path):
    filepositiuon=path
    
    #すべてのデータを読み込んでするため以下一行をコメント
    #f=open(filepositiuon,"r",encoding="UTF-8")

    #-----------------------------------------------
    # ファイルをオープンする すべてを読み込んで改行キーでsplit?がいい？
    wiki_data = open("test_data", "r")
    # 行ごとにすべて読み込んでリストデータにする
    f = wiki_data.readlines()
    #-----------------------------------------------
    line=""
    title=""
    line2=""
    for line in f:
        """
        if (line.find('<doc') != -1):
            print("この文字列には'be,'という文字が含まれています。")
        else:
            print("この文字列には'be,'という文字は含まれていません。")
        """
        num=line.find(r'<doc')
        if (line.find('url') > 0): 
            f=1
            #DBに入れる
            if title!='':
                print(title)
                #print(line2)
                db(title,line2)
            title=""
            line2=""
            continue
        if (line.find('/doc') > 0):
            f=0
            continue
        else:
            if(line != ""):
                if(f == 1):
                    title=line
                    f=f+1
                else:
                    line2=line2+line

#---------------
#BD28まで
#---------------  
# ALL
#director1=["A","B"]
#director2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#データが多いので分割
#No 1
director1=["A"]
director2=["A","B","C","D","E","F","G"]
#No 2
director1=["A"]
director2=["H","I","J","K","L","M","N","O","P"]
#No 3
director1=["A"]
director2=["Q","R","S","T","U","V","W","X","Y","Z"]
#No 4
#最後のデータは以下
#鈴虫 (曖昧さ回避)
#ヤルモ・レーティネン
#人の間と書いて人間
#director1=["B"]
#director2=["A","B","C","D"]


path = "D:/work/wikiextractor/"
for i in director1:
    for j in director2:
        director3=i+j
        print("dir="+director3)
        for k in range(0,100):
            if k<10:
                ii='0'+str(k)
            else:
                ii=str(k)    
            str2="/wiki_"+ii+""
            print(str2)
            directory=path+director3+str2
            print(directory)
            wikiwrite(directory)
            



