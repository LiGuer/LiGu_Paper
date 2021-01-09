import re

def readData():
    f = open("../artist.txt", "r",encoding ='utf-8')
    data = f.read()
    f.close()
    return data

def genHtml(data):
    f = open("../index.html", "w+",encoding ='utf-8')
    f.write('''<!DOCTYPE html>
<meta charset=\"UTF-8\">
<html>
    <head>
            <link rel="stylesheet" type="text/css" href=".html/style.css" />
            <script src=".html/jquery-3.3.1.min.js"></script>
            <script src=".html/Read.js"></script>
    </head>
    <body>
            <img id="imgs" src="" style="height: 300px; z-index:1;">
            <style>img[src=""],img:not([src]){ opacity:0;}</style>
''')

    f.write("<table>")
    for i in range(len(data)):
        f.write("<tr><td>"+data[i][0]+'</td>')
        f.write("<td>"+data[i][1]+'</td>')
        imgs = data[i][2].split(' · ')
        f.write("<td>")

        for j in range(len(imgs)):
            a = data[i][0]
            a = re.sub(" ","",a)
            a = a+"/"+imgs[j]
            a = re.sub(" ","_",a)
            a = re.sub("\((\S+)\)","",a)
            a = "art-data/"+a+".jpg"
            f.write("<a onmouseover=\"on('"+a+"')\" onmouseout=\"off()\" href=\""+a+"\">"+imgs[j]+"</a>"+' · ')

        f.write('</td></tr>\n')

    f.write("</table></body></html>")
    f.close()

if __name__ == '__main__':
    data = readData()
    data = data.split('\n')
    for i in range(len(data)):
        data[i] = data[i].split('\t')
    print(data)
    genHtml(data)