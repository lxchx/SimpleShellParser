import ply.lex as lex

from .SimpleShellSyntaxError import *
from . import ASTTool

TOKENS = (
    'TOKEN',
    'REDIRECT' # 在这处理一下重定向符
)

class Lexer:
    # 设定捕捉的tokens的列表
    tokens = TOKENS

    literals = [';', '|']

    # 定义捕捉分词的函数，使用正则表达式捕捉，并进行一些简单的预处理
    # 重定向符
    def t_REDIRECT(self, t):
        """(<|[12]?>{1,2})(([^ "';\|\t\n]+)|("[^"\t\n]+")|('[^'\t\n]+'))?"""
        return t
    # 一般的token，包括命令、参数、路径
    def t_TOKEN(self, t):
        """([^ "';\|\t\n]+)|("[^"\t\n]+")|('[^'\t\n]+')"""
        ASTTool.del_single_quo(t.value) # 把包围的单引号删掉，如果有，这样就不用后续处理单引号的情况了
        return t

    # 定义一个捕捉\n的函数，用来做行数统计
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # 设置忽略空格和tab键
    t_ignore  = ' \t'

    # 错误处理
    def t_error(self, t):
        raise SimpleShellSyntaxError("Illegal character '%s'" % t.value[0])
        # print("Illegal character '%s'" % t.value[0])
        # t.lexer.skip(1)

    # 构建分词器
    def build(self, **kwargs):
        self.lex = lex.lex(module=self, **kwargs)


if __name__ == '__main__':
    lexer = Lexer()
    lexer.build()
    data = input('输入要解析的代码：')
    lexer.lex.input(data)
    for tok in lexer.lex:
        print(tok)