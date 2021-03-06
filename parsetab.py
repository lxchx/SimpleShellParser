
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "REDIRECT TOKENcommand_line : job\n                        | job ';'\n                        | job ';' command_line\n        \n        job : command\n               | job '|' command\n        command : simple_command\n                   | command REDIRECT\n                   | command REDIRECT TOKEN\n        simple_command : TOKEN\n                          | simple_command TOKEN\n        "
    
_lr_action_items = {'TOKEN':([0,4,5,6,7,8,9,],[5,9,-9,5,5,12,-10,]),'$end':([1,2,3,4,5,6,8,9,10,11,12,],[0,-1,-4,-6,-9,-2,-7,-10,-3,-5,-8,]),';':([2,3,4,5,8,9,11,12,],[6,-4,-6,-9,-7,-10,-5,-8,]),'|':([2,3,4,5,8,9,11,12,],[7,-4,-6,-9,-7,-10,-5,-8,]),'REDIRECT':([3,4,5,8,9,11,12,],[8,-6,-9,-7,-10,8,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'command_line':([0,6,],[1,10,]),'job':([0,6,],[2,2,]),'command':([0,6,7,],[3,3,11,]),'simple_command':([0,6,7,],[4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> command_line","S'",1,None,None,None),
  ('command_line -> job','command_line',1,'p_command_line','Parser.py',15),
  ('command_line -> job ;','command_line',2,'p_command_line','Parser.py',16),
  ('command_line -> job ; command_line','command_line',3,'p_command_line','Parser.py',17),
  ('job -> command','job',1,'p_job','Parser.py',34),
  ('job -> job | command','job',3,'p_job','Parser.py',35),
  ('command -> simple_command','command',1,'p_command','Parser.py',48),
  ('command -> command REDIRECT','command',2,'p_command','Parser.py',49),
  ('command -> command REDIRECT TOKEN','command',3,'p_command','Parser.py',50),
  ('simple_command -> TOKEN','simple_command',1,'p_simple_command','Parser.py',67),
  ('simple_command -> simple_command TOKEN','simple_command',2,'p_simple_command','Parser.py',68),
]
