import re

def Item(code):
    while(1):
        # a
        ans = re.search(r'\n( +)\*', code)
        if (ans == None): 
            break
        a = ans.span()[0]
        b = ans.span()[1]
        n = 0
        for i in range(a, b):
            if(code[i] == ' '):
                n = n + 1
        # begin
        codeA = code[:a] + '\n' +  ' ' * n + "\\begin{enumerate}"
        code = code[a:]
        # c-1
        strTmp = r'\n {0,' + str(int(n-1)) + r'}\S'
        ans = re.search(strTmp, code)
        if (ans == None): 
            c = len(code) - 1
        else:
            c = ans.span()[0]
        # c-2
        strTmp = r'\n {0,' + str(int(n)) + r'}[^\* ]'
        ans = re.search(strTmp, code)
        if (ans != None): 
            c = min(c, ans.span()[0])
        # end
        codeC = code[:c+1] + ' ' * n + "\\end{enumerate}\n"
        # ans
        strTmp = r'(\n {' + str(int(n)) + r'})\* '
        codeC = re.sub(strTmp, lambda m:m.group(1) + "\\item " , codeC)
        code = codeA + codeC + code[c+1:]
    return code

if __name__ == '__main__':
    fileName = "信息论.tex"

    file = open(fileName,"r", encoding='utf-8')
    Str = file.read()
    # 简单命令
    Str = re.sub(r'\\\.', r'\\boldsymbol', Str)
    Str = re.sub(r'\\bf', r'\\textbf', Str)
    Str = re.sub(r'\\def', r'\\defi', Str)
    # section
    Str = re.sub(r'\\section ([\s\S][^\n]+)\n', lambda m:'\\section{' + m.group(1) + '}\n', Str)
    Str = re.sub(r'(\n {8})\\section', lambda m:m.group(1) +'\\subsubsection', Str)
    Str = re.sub(r'(\n {4})\\section', lambda m:m.group(1) +'\\subsection', Str)
    Str = re.sub(r'(\n +)\\section', lambda m:m.group(1) +'\\noindent\\textbf', Str)
    # 列表
    Str = Item(Str)
    # 公式
    Str = re.sub(r'\n(\s+)\$([\s\S][^\$]+)\$\n', lambda m:'\n'+ m.group(1) + '\\begin{align*}'+m.group(2)+'\\end{align*}\n', Str)

    file.close()
    file = open("head.tex","r", encoding='utf-8')
    Str = file.read() + Str + "\n\\end{document}"
    #print(Str)

    file.close()
    file = open("D:/矩阵论.tex","w+", encoding='utf-8')
    file.write(Str)
    file.close()