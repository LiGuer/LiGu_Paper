import re

def Cut(Str):
    Str = re.sub(r'\n {' + str(int(4 * 3)) + r',}[^\n]*', r'', Str)
    Str = re.sub(r'\n\s*\n', r'\n', Str)
    return Str

def Item(Str):
    while(1):
        # a
        ans = re.search(r'\n( +)\*', Str)
        if (ans == None): 
            break
        a = ans.span()[0]
        b = ans.span()[1]
        n = 0
        for i in range(a, b):
            if(Str[i] == ' '):
                n = n + 1
        # begin
        StrA = Str[:a] + '\n' +  ' ' * n + "\\begin{enumerate}"
        Str = Str[a:]
        # c-1
        strTmp = r'\n {0,' + str(int(n-1)) + r'}\S'
        ans = re.search(strTmp, Str)
        if (ans == None): 
            c = len(Str) - 1
        else:
            c = ans.span()[0]
        # c-2
        strTmp = r'\n {0,' + str(int(n)) + r'}[^\* ]'
        ans = re.search(strTmp, Str)
        if (ans != None): 
            c = min(c, ans.span()[0])
        # end
        StrC = Str[:c+1] + ' ' * n + "\\end{enumerate}\n"
        # ans
        strTmp = r'(\n {' + str(int(n)) + r'})\* '
        StrC = re.sub(strTmp, lambda m:m.group(1) + "\\item " , StrC)
        Str = StrA + StrC + Str[c+1:]
    return Str

def Formulas(Str):
    #简单替换
    Str = re.sub(r'≥', r'\\ge ', Str)
    Str = re.sub(r'≤', r'\\le ', Str)
    Str = re.sub(r'≠', r'\\neq ', Str)
    Str = re.sub(r'∂', r'\\partial ', Str)
    Str = re.sub(r' => ', r' \\Rightarrow ', Str)
    Str = re.sub(r' <=> ', r' \\Leftrightarrow ', Str)
    Str = re.sub(r'\\sum_', r'\\sum\\limits_', Str)
    Str = re.sub(r'\\prod_', r'\\prod\\limits_', Str)
    #Str = re.sub(r'\n(\s+)\$([^\$]+)\$\n', lambda m:'\n'+ m.group(1) + '\\begin{align*}'+m.group(2)+'\\end{align*}\n', Str)

    while(1):
        # begin
        ans = re.search('\n( +)\$', Str)
        if (ans == None): 
            break
        a = ans.span()[1]
        StrA = Str[:a-1] + "\\begin{align*}"
        Str = Str[a:]
        # end
        ans = re.search('\$\n', Str)
        if (ans == None): 
            break
        c = ans.span()[1]
        StrC = "\\end{align*}\n" + Str[c:]
        # middle
        StrB = Str[:c-2]
        StrB = re.sub(r'\n', r'\\\\\n', StrB)
        StrB = re.sub(r'\(', r'\\left(', StrB)
        StrB = re.sub(r'\)', r'\\right)', StrB)
        StrB = re.sub(r'\[', r'\\left[', StrB)
        StrB = re.sub(r'\]', r'\\right]', StrB)
        # ans
        Str = StrA + StrB + StrC

    Str = re.sub(r'\n\\\\\n', r'\n', Str)
    return Str

    return Str

def ToLatex(Str):
    Str = re.sub(r'\n\s*\n', r'\n', Str)
    # 简单命令
    Str = re.sub(r'\\\.', r'\\boldsymbol', Str)
    Str = re.sub(r'--', r'---', Str)
    Str = re.sub(r'\\bf', r'\\textbf', Str)
    Str = re.sub(r'\\Example', r'\\textbf{Example. }', Str)
    Str = re.sub(r'\\Property', r'\\textbf{Property. }', Str)
    Str = re.sub(r'\\Proof', r'\\textbf{Proof. }', Str)
    Str = re.sub(r'\\def\{([\S]+)\}', lambda m: '\\textbf{Define (' + m.group(1)+ '). }', Str)
    Str = re.sub(r'\\Theorem\{([\S]+)\}', lambda m: '\\textbf{Theorem (' + m.group(1)+ ').} ', Str)
    # section
    Str = re.sub(r'(\n {8})\*', lambda m:m.group(1) +'\\subsubsection', Str)
    Str = re.sub(r'(\n {4})\*', lambda m:m.group(1) +'\\subsection', Str)
    Str = re.sub(r'\n\*', r'\n\\section', Str)
    Str = re.sub(r'section ([\s\S][^\n]+)\n', lambda m:'section{' + m.group(1) + '}\n', Str)
    # 列表
    Str = Item(Str)
    # 公式
    Str = Formulas(Str)
    # Other
    Str = re.sub(r'\n', r'\\par\n', Str)
    Str = re.sub(r'\\\\\\par', r'\\\\', Str)
    Str = re.sub(r'\\begin{enumerate}\\par', r'\\begin{enumerate}', Str)
    Str = re.sub(r'\\end{enumerate}\\par', r'\\end{enumerate}', Str)
    Str = re.sub(r'\\begin{align\*}\\par', r'\\begin{align*}', Str)
    Str = re.sub(r'\\end{align\*}\\par', r'\\end{align*}', Str)
    Str = re.sub(r'\\par(\s+)\\begin{align\*}', lambda m: m.group(1) + '\\begin{align*}', Str)
    Str = re.sub(r'\\\\(\s+)\\end{align\*}', lambda m: m.group(1) + '\\end{align*}', Str)

    file = open("head.tex","r", encoding='utf-8')
    Str = file.read() + Str + "\n\\end{document}"

    return Str

if __name__ == '__main__':
    fileName = "信息论.tex"
    file = open(fileName,"r", encoding='utf-8')
    Str = file.read()
    file.close()

    Str = ToLatex(Str)

    file = open("D:/矩阵论.tex","w+", encoding='utf-8')
    file.write(Str)
    file.close()