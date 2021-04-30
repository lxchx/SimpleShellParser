import ply.yacc as yacc
import copy
import json

from .Lexer import * 
from . import ASTTool


class Parser:
    tokens = TOKENS

    def p_command_line(self, p):
        """command_line : job
                        | job ';'
                        | job ';' command_line
        
        """
        if len(p) == 2 or len(p) == 3:
            name = 'command_line'
            attrs = {'jobs': [p[1]]}
            p[0] = ASTTool.make_node(name, attrs)
        else:
            p[0] = copy.copy(p[1])
            attrs = p[0]['attrs']
            attrs['jobs'].append(p[3])  # 注意字符token也占p的位置

    def p_empty(self, p):
        r'empty :'

    def p_job(self, p):
        """job : command
               | job '|' command
        """
        if len(p) == 2:
            name = 'job'
            attrs = {'commands': [p[1]]}
            p[0] = ASTTool.make_node(name, attrs)
        else:
            p[0] = copy.copy(p[1])
            attrs = p[0]['attrs']
            attrs['commands'].append(p[3])  # 注意字符token也占p的位置


    def p_command(self, p):
        """command : simple_command
                   | command REDIRECT
                   | command REDIRECT TOKEN
        """
        if len(p) == 2:
            name = 'command'
            attrs = {'simpleCommand': p[1], 'redirects': list()}
            p[0] = ASTTool.make_node(name, attrs)
        elif len(p) == 3:
            p[0] = copy.copy(p[1])
            attrs = p[0]['attrs']
            attrs['redirects'].append(ASTTool.make_redirect_node(p[2]))
        elif len(p) == 4:  # 重定向的文件名隔开的情况
            p[0] = copy.copy(p[1])
            attrs = p[0]['attrs']
            attrs['redirects'].append(ASTTool.make_redirect_node(p[2] + p[3])) # 把文件名补上就完事了


    def p_simple_command(self, p):
        """simple_command : TOKEN
                          | simple_command TOKEN
        """
        if len(p) == 2:
            name = 'simple_command'
            attrs = {'pathName': p[1], 'paras': list()}
            p[0] = ASTTool.make_node(name, attrs)
        else:
            p[0] = copy.copy(p[1])
            attrs = p[0]['attrs']
            attrs['paras'].append(p[2])
    def build(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = Lexer()
        self.lexer.build()

    def parse(self, data):
        return self.parser.parse(data, lexer=self.lexer.lex, tracking=True)
        # return self.parser.parse(data, lexer=self.lexer.lex, debug=True, tracking=True)

    def parse2json(self, data):
        return json.dumps(self.parse(data))

if __name__ == '__main__':
    paser = Parser()
    paser.build()
    # data = input('输入要解析的代码：')
    data = "ps -ef|grep python|awk '{print $2}' > 'file 2'"
    result = paser.parse2json(data)
    print(result)
    