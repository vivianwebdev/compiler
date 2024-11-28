#######################################
# CONSTANTS
#######################################

DIGITS  = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_DIGITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


#######################################
# ERRORS
#######################################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

#######################################
# POSITION
#######################################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#######################################
# TOKENS
#######################################

entier      = 'nombre entier'
reel        = 'nombre réel'
snkint		= 'mot clé de declaration du type entier'
snkfloat    = 'mot clé de declaration du type réel'
snkplus     = 'PLUS'
snkminus    = 'MINUS'
snkmul      = 'MUL'
snkdiv      = 'DIV'
snkparov    = 'parenthese ouvrant'
snkparfe    = 'parenthese fermant'
snkbegin    = 'mot clé de début de programme'
snkend      = 'mot clé de fin de programme'
snkid       = 'identificateur'
snksep      = 'séparateur'
snkfini     = 'fin dinstruction'
snkset      = 'mot clé pour affection dun valeur'
snkop       = 'opérateur de comparaison'
snkcom      = 'commentaire'
snkdcon     = 'debut de condition'
snkfcon     = 'fin de condition'
snkdbloc    = 'début de bloc'
snkfbloc    = 'fin de bloc'
snkif       = 'if condition'
snkelse     = 'else condition'
snkprint    = 'affichage'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None  

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(snkplus))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(snkminus))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(snkmul))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(snkdiv))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(snkparov))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(snkparfe))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token(snksep))
                self.advance()
            elif self.current_char == '[':
                tokens.append(Token(snkdcon))
                self.advance()
            elif self.current_char == ']':
                tokens.append(Token(snkfcon))
                self.advance()        
            elif self.current_char == 'I':
                self.advance()
                if self.current_char == 'f':
                   tokens.append(Token(snkif))
                   self.advance()
                else:
                    return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
            elif self.current_char == 'E':
                 self.advance()
                 if self.current_char == 'l':
                    self.advance()
                    if self.current_char == 's':
                       self.advance()
                       if self.current_char == 'e':
                          tokens.append(Token(snkelse))
                          self.advance()     
            elif self.current_char == '$':
                 self.advance()
                 if self.current_char == '$':
                     comment_str = ''
                     while True:
                         self.advance()
                         if self.current_char == None:
                             break
                         comment_str += self.current_char
                     tokens.append(Token(snkcom, comment_str))
                     self.advance()
                 else:
                     tokens.append(Token(snkfini))
            elif self.current_char == '>':
                tokens.append(Token(snkop))
                self.advance()
            elif self.current_char == '<':
                tokens.append(Token(snkop))
                self.advance()    
                ######Set#####
            elif self.current_char == 'S':
                self.advance()
                if self.current_char == 'e':
                   self.advance()
                   if self.current_char == 't':
                      tokens.append(Token(snkset))
                      self.advance()
                else:
                    if self.current_char == 'n':
                       self.advance()
                       if self.current_char == 'k':
                          self.advance()
                          if self.current_char == '_':
                             self.advance()
                             if self.current_char == 'B':
                                self.advance()
                                if self.current_char == 'e':
                                   self.advance()
                                   if self.current_char == 'g':
                                      self.advance()
                                      if self.current_char == 'i':
                                         self.advance()
                                         if self.current_char == 'n':
                                            tokens.append(Token(snkbegin))
                                            self.advance()
                             else: 
                                if self.current_char == 'E':
                                   self.advance()
                                   if self.current_char == 'n':
                                      self.advance()
                                      if self.current_char == 'd':
                                         tokens.append(Token(snkend))
                                         self.advance()
                                else:
                                    if self.current_char == 'I':
                                       self.advance()
                                       if self.current_char == 'n':
                                          self.advance()
                                          if self.current_char == 't':
                                             tokens.append(Token(snkint))
                                             self.advance()         
                                    else:
                                        if self.current_char == 'R':
                                           self.advance()
                                           if self.current_char == 'e':
                                              self.advance()
                                              if self.current_char == 'a':
                                                 self.advance()
                                                 if self.current_char == 'l':
                                                    tokens.append(Token(snkfloat))
                                                    self.advance()  
                                        else:
                                            if self.current_char == 'P':
                                               self.advance()
                                               if self.current_char == 'r':
                                                  self.advance()
                                                  if self.current_char == 'i':
                                                     self.advance()
                                                     if self.current_char == 'n':
                                                         self.advance()
                                                         if self.current_char == 't':
                                                            tokens.append(Token(snkprint))
                                                            self.advance() 


            elif self.current_char == 'B':
                self.advance()
                if self.current_char == 'e':
                   self.advance()
                   if self.current_char == 'g':
                      self.advance()
                      if self.current_char == 'i':
                         self.advance()
                         if self.current_char == 'n':
                            tokens.append(Token(snkdbloc))
                            self.advance()
            elif self.current_char == 'e':
                 self.advance()
                 if self.current_char == 'n':
                    self.advance()
                    if self.current_char == 'd':
                       tokens.append(Token(snkfbloc))
                       self.advance()                
            elif self.current_char in LETTERS:
                 id_str = ''
                 while self.current_char != None and self.current_char in LETTERS_AND_DIGITS:
                    id_str += self.current_char
                    self.advance()
                 tokens.append(Token(snkid, id_str))
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
        

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(entier, int(num_str))
        else:
            return Token(reel, float(num_str))
        
    


#######################################
# RUN
#######################################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
