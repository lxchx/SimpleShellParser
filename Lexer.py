import ply.lex as lex

from .SimpleShellSyntaxError import *
from . import ASTTool

TOKENS = (
    'TOKEN',
    'REDIRECT',  # 在这处理一下重定向符
    'SPACE'
)

class Lexer:
    # List of token names.   This is always required
    tokens = TOKENS

    literals = [';', '|']

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_REDIRECT(self, t):
        """(<|[12]?>{1,2})(([^ "';\|\t\n]+)|("[^"\t\n]+")|('[^'\t\n]+'))?"""
        return t

    def t_TOKEN(self, t):
        """([^ "';\|\t\n]+)|("[^"\t\n]+")|('[^'\t\n]+')"""
        ASTTool.del_single_quo(t.value) # 把包围的单引号删掉，如果有，这样就不用后续处理单引号的情况了
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self, t):
        raise SimpleShellSyntaxError("Illegal character '%s'" % t.value[0])
        # print("Illegal character '%s'" % t.value[0])
        # t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lex = lex.lex(module=self, **kwargs)


if __name__ == '__main__':
    lexer = Lexer()
    lexer.build()
    data = input('输入要解析的代码：')
    lexer.lex.input(data)
    for tok in lexer.lex:
        print(tok)