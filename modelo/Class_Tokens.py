import ply.lex as lex
class AnalizadorLexico:
    errorl = ""
    listaT = ""

    t_LLLAVE = r'{'
    t_RLLAVE = r'}'
    t_EQUALS = r'\='
    t_COMMA = r','
    t_ARROBA = r'\@'
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_ignore = " \t+"
    t_STRING = r'([a-zA-Z0-9][a-zA-Z0-9 ]+)'

    def __init__(self,tokens,reservadas):
        self.tokens = tokens
        self.reservadas = reservadas



    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_error(self,t):
        print("Error Lexico\nCaracter ilegal '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_ARTICULO(self,t):
        r'article'
        return t

    def t_AUTOR(self,t):
        r'author'
        return t

    def t_TITLE(self,t):
        r'title'
        return t

    def t_JOURNAL(self,t):
        r'journal'
        return t

    def t_YEAR(self,t):
        r'year'
        return t

    def t_NUMERO(self,t):
        r'number'
        return t

    def t_PAGE(self,t):
        r'pages'
        return t

    def t_MONTH(self,t):
        r'month'
        return t

    def t_NOTE(self,t):
        r'note'
        return t

    def t_VOLUMEN(self,t):
        r'volume'
        return t

    def t_PUBLISHER(self,t):
        r'publisher'
        return t

    def t_SERIES(self,t):
        r'series'
        return t

    def t_ADDRESS(self,t):
        r'address'
        return t

    def t_EDITION(self,t):
        r'edition'
        return t

    def t_ISBN(self,t):
        r'isbn'
        return t

    def t_BOOKTITLE(self,t):
        r'booktitle'
        return t

    def t_EDITOR(self,t):
        r'editor'
        return t

    def t_ONGANIZATION(self,t):
        r'organization'
        return t

    def t_BOOK(self,t):
        r'book'
        return t

    def t_CONFERENCE(self,t):
        r'conference'
        return t

    def t_MANUAL(self,t):
        r'manual'
        return t

    def t_UNPUBLISHED(self,t):
        r'unpublished'
        return t

    def build(self, **kwargs):
        """Builds the lexer with the respective kwargs."""
        self.lexer = lex.lex(module=self, **kwargs)

    def tokenize(self, data):
        """Reads the input and matches the symbols to the defined tokens."""
        self.lexer.input(data)

    def print_tokens(self, print_tokens=False):
        """Prints the list of tokens found."""
        if print_tokens:
            if (self.listaT != ""): self.listaT = ""
            while True:
                token = self.lexer.token()
                if not token:
                    break
                if(token.type=="NEWLINE"):
                    self.listaT+="\n\n"
                else:
                    self.listaT+="<"+str(token.type)+">"+" \n"