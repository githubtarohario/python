#--------------------------------------------------------
#このブログラムは<doc  ~  /doc>
#を抜き出しデータベースに入れるプログラム
#xmlで抜き出しVersion2  pip install beautifulsoup4
#----------------------------------------------------------
import sqlite3
import codecs
from bs4 import BeautifulSoup
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
def wikiwrite2(path):
    #xml=open("wiki_00","r", encoding='utf-8').read()
    xml=open(path,"r", encoding='utf-8').read()
    
    #print(xml)
    j=1
    soup=BeautifulSoup(xml,'html.parser')
    for i in soup.find_all("doc"):
        print(i['title']) 
        db(i['title'],i.string)
        j=j+1
        print(j)
        #print(i.string)



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
#No 3 AQがないのはなぜ？
#director1=["A"]
#director2=["Q","R","S","T","U","V","W","X","Y","Z"]
#No 4
#最後のデータは以下
#鈴虫 (曖昧さ回避)
#ヤルモ・レーティネン
#人の間と書いて人間
#director1=["B"]
#director2=["A","B","C","D"]


#
#Test
#あとで削除
#
#director1=["A"]
#director2=["A"]




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
            print("str2=",str2)
            print("director1,director2",director1,director2)
            directory=path+director3+str2
            print("directory",directory)
            wikiwrite2(directory)
            



