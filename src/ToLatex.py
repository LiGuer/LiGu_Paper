import re

if __name__ == '__main__':
    fileName = "信息论.tex"

    file = open(fileName,"r", encoding='utf-8')
    Str = file.read()

    Str = eval(repr(Str).replace('\\bf', '\\textbf')) 
    Str = eval(repr(Str).replace('\\def', '\\defi')) 
    Str = re.sub(r'(\n        )\\section', lambda m:m.group(1) +'\\subsubsection', Str)
    Str = re.sub(r'(\n    )\\section', lambda m:m.group(1) +'\\subsection', Str)
    Str = re.sub(r'([\s+][^\n])\\section', lambda m:m.group(1) +'\\noindent\\textbf', Str)
    
    Str = re.sub(r'\n(\s+)\$([\s\S][^\$]+)\$\n', lambda m:'\n'+ m.group(1) + '\\begin{align*}'+m.group(2)+'\\end{align*}\n', Str)
    Str = re.sub(r'\\item([\s\S][^\n]+)\n', lambda m: '\\begin{itemize}\\item' + m.group(1) + '\\end{itemize}\n', Str)
    Str = re.sub(r'\n([\s][^\n]+)\*([\s\S][^\n]+)\n', lambda m: '\n' + m.group(1) + '\\begin{itemize}\\item' + m.group(2) + '\\end{itemize}\n', Str)
    Str = re.sub(r'\n([\s][^\n]+)\*([\s\S][^\n]+)\n', lambda m: '\n' + m.group(1) + '\\begin{itemize}\\item' + m.group(2) + '\\end{itemize}\n', Str)

    file.close()
    file = open("head.tex","r", encoding='utf-8')
    Str = file.read() + Str + "\\end{document}"
    print(Str)

    file.close()
    file = open("D:/矩阵论.tex","w+", encoding='utf-8')
    file.write(Str)
    file.close()