import re

if __name__ == '__main__':
    fileName = "信息论.tex"
    file = open(fileName,"r", encoding='utf-8')
    Str = file.read()
    file.close()

    Str = ToLatex(Str)

    file = open("D:/矩阵论.tex","w+", encoding='utf-8')
    file.write(Str)
    file.close()

def Cut(Str):
    Str = re.sub(r'\n {' + str(int(4 * 3)) + r',}[^\n]*', r'', Str)
    Str = re.sub(r'\n\s*\n', r'\n', Str)
    return Str

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

def ToLatex(Str):
    #Str = re.sub(r'\n\s*\n', r'\n', Str)
    #Str = re.sub(r'(\n {4*1,})\n', r'\n', Str)
    # 简单命令
    Str = re.sub(r'\\\.', r'\\boldsymbol', Str)
    Str = re.sub(r'\\bf', r'\\textbf', Str)
    Str = re.sub(r'\\Example', r'\\textbf{例子}', Str)
    Str = re.sub(r'\\Property', r'\\textbf{性质}', Str)
    Str = re.sub(r'\\Proof', r'\\textbf{证明}', Str)
    Str = re.sub(r'\\def\{([\S]+)\}', lambda m: '\\textbf{定义(' + m.group(1)+ ')}', Str)
    Str = re.sub(r'\\Theorem\{([\S]+)\}', lambda m: '\\textbf{定理(' + m.group(1)+ ')}', Str)
    # section
    Str = re.sub(r'(\n {8})\*', lambda m:m.group(1) +'\\subsubsection', Str)
    Str = re.sub(r'(\n {4})\*', lambda m:m.group(1) +'\\subsection', Str)
    Str = re.sub(r'\n\*', r'\n\\section', Str)
    Str = re.sub(r'section ([\s\S][^\n]+)\n', lambda m:'section{' + m.group(1) + '}\n', Str)
    # 列表
    Str = Item(Str)
    # 公式
    Str = re.sub(r'≥', r'\\ge', Str)
    Str = re.sub(r'≤', r'\\le', Str)
    Str = re.sub(r'∂', r'\\partial ', Str)
    Str = re.sub(r' => ', r' \\Rightarrow ', Str)
    Str = re.sub(r' <=> ', r' \\Leftrightarrow ', Str)
    Str = re.sub(r'\\sum_', r'\\sum\\limits_', Str)
    Str = re.sub(r'\\prod_', r'\\prod\\limits_', Str)

    Str = re.sub(r'\n(\s+)\$([\s\S][^\$]+)\$\n', lambda m:'\n'+ m.group(1) + '\\begin{align*}'+m.group(2)+'\\end{align*}\n', Str)

    file.close()
    file = open("head.tex","r", encoding='utf-8')
    Str = file.read() + Str + "\n\\end{document}"

    return Str