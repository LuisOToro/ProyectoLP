
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDELLLAVE RLLAVE EQUALS COMMA NUMBER ARROBA BLOQUE PLUS MINUS TIMES DIVIDE ARTICULO AUTOR TITLE YEAR PAGE NOTE VOLUMEN JOURNAL NAME NUMERO MONTH PUBLISHER SERIES ADDRESS EDITION ISBN BOOKTITLE EDITOR ONGANIZATIONstatement : BLOQUEstatement : ARROBA ARTICULOtitulo : TITLE EQUALS LLLAVE BLOQUE RLLAVEautor : AUTOR EQUALS LLLAVE BLOQUE RLLAVEano : YEAR EQUALS NUMBERpagina : PAGE EQUALS LLLAVE BLOQUE RLLAVEnota : NOTE EQUALS LLLAVE BLOQUE RLLAVEvolumen : VOLUMEN EQUALS NUMBERjournal : JOURNAL EQUALS LLLAVE BLOQUE RLLAVEnumero : NUMERO EQUALS NUMBERmes : MONTH EQUALS NUMBERexpression : ARROBA ARTICULO LLLAVE NAME COMMAexpression : NUMBERarticulo : ARROBA ARTICULO LLLAVE NAME COMMA autor COMMA titulo COMMA journal COMMA ano COMMA numero COMMA pagina COMMA mes COMMA nota COMMA volumen COMMAexpression : expression PLUS expression\n                      | expression MINUS expression\n                      | expression TIMES expression\n                      | expression DIVIDE expression'
    
_lr_action_items = {'BLOQUE':([0,],[2,]),'ARROBA':([0,],[3,]),'$end':([1,2,4,],[0,-1,-2,]),'ARTICULO':([3,],[4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> BLOQUE','statement',1,'p_statement_bloque','A_lexico_Article_Bibtext.py',14),
  ('statement -> ARROBA ARTICULO','statement',2,'p_statement_arroba_assign','A_lexico_Article_Bibtext.py',19),
  ('titulo -> TITLE EQUALS LLLAVE BLOQUE RLLAVE','titulo',5,'p_statement_title_assign','A_lexico_Article_Bibtext.py',23),
  ('autor -> AUTOR EQUALS LLLAVE BLOQUE RLLAVE','autor',5,'p_statement_autor_assign','A_lexico_Article_Bibtext.py',27),
  ('ano -> YEAR EQUALS NUMBER','ano',3,'p_statement_year_assing','A_lexico_Article_Bibtext.py',31),
  ('pagina -> PAGE EQUALS LLLAVE BLOQUE RLLAVE','pagina',5,'p_statement_paginas_assign','A_lexico_Article_Bibtext.py',35),
  ('nota -> NOTE EQUALS LLLAVE BLOQUE RLLAVE','nota',5,'p_statement_note_assign','A_lexico_Article_Bibtext.py',39),
  ('volumen -> VOLUMEN EQUALS NUMBER','volumen',3,'p_statement_volumen_assign','A_lexico_Article_Bibtext.py',43),
  ('journal -> JOURNAL EQUALS LLLAVE BLOQUE RLLAVE','journal',5,'p_statement_journal_assign','A_lexico_Article_Bibtext.py',47),
  ('numero -> NUMERO EQUALS NUMBER','numero',3,'p_statement_number_assign','A_lexico_Article_Bibtext.py',51),
  ('mes -> MONTH EQUALS NUMBER','mes',3,'p_statement_mes_assign','A_lexico_Article_Bibtext.py',55),
  ('expression -> ARROBA ARTICULO LLLAVE NAME COMMA','expression',5,'p_expression_name','A_lexico_Article_Bibtext.py',59),
  ('expression -> NUMBER','expression',1,'p_expression_number','A_lexico_Article_Bibtext.py',63),
  ('articulo -> ARROBA ARTICULO LLLAVE NAME COMMA autor COMMA titulo COMMA journal COMMA ano COMMA numero COMMA pagina COMMA mes COMMA nota COMMA volumen COMMA','articulo',23,'p_estructura','A_lexico_Article_Bibtext.py',66),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','A_lexico_Article_Bibtext.py',71),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','A_lexico_Article_Bibtext.py',72),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','A_lexico_Article_Bibtext.py',73),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','A_lexico_Article_Bibtext.py',74),
]
