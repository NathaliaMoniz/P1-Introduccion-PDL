
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BIN CADENACON CADENASIN COMA EQ FL GE GT HEX INT LE LLAVEA LLAVEC LT NCIENT NULL OCT PUNTOS REAL TR axioma : LLAVEA contenido LLAVEC \n                   | LLAVEA LLAVEC contenido : asignacion\n                      | asignacion COMA\n                      | asignacion COMA contenido  asignacion : CADENACON PUNTOS valor\n                       | CADENASIN PUNTOS valor  valor : numero\n                | comparacion\n                | NULL\n                | TR\n                | FL\n                | CADENACON \n                | axiomanumero : INT\n                | REAL\n                | NCIENT\n                | BIN\n                | OCT\n                | HEX  comparacion : numero LT numero\n                        | numero GT numero\n                        | numero EQ numero\n                        | numero LE numero\n                        | numero GE numero '
    
_lr_action_items = {'LLAVEA':([0,10,11,],[2,2,2,]),'$end':([1,4,8,],[0,-2,-1,]),'LLAVEC':([2,3,4,5,8,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,33,34,35,36,37,],[4,8,-2,-3,-1,-4,-5,-13,-6,-8,-9,-10,-11,-12,-14,-15,-16,-17,-18,-19,-20,-7,-21,-22,-23,-24,-25,]),'CADENACON':([2,9,10,11,],[6,6,13,13,]),'CADENASIN':([2,9,],[7,7,]),'COMA':([4,5,8,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,33,34,35,36,37,],[-2,9,-1,-13,-6,-8,-9,-10,-11,-12,-14,-15,-16,-17,-18,-19,-20,-7,-21,-22,-23,-24,-25,]),'PUNTOS':([6,7,],[10,11,]),'NULL':([10,11,],[17,17,]),'TR':([10,11,],[18,18,]),'FL':([10,11,],[19,19,]),'INT':([10,11,28,29,30,31,32,],[21,21,21,21,21,21,21,]),'REAL':([10,11,28,29,30,31,32,],[22,22,22,22,22,22,22,]),'NCIENT':([10,11,28,29,30,31,32,],[23,23,23,23,23,23,23,]),'BIN':([10,11,28,29,30,31,32,],[24,24,24,24,24,24,24,]),'OCT':([10,11,28,29,30,31,32,],[25,25,25,25,25,25,25,]),'HEX':([10,11,28,29,30,31,32,],[26,26,26,26,26,26,26,]),'LT':([15,21,22,23,24,25,26,],[28,-15,-16,-17,-18,-19,-20,]),'GT':([15,21,22,23,24,25,26,],[29,-15,-16,-17,-18,-19,-20,]),'EQ':([15,21,22,23,24,25,26,],[30,-15,-16,-17,-18,-19,-20,]),'LE':([15,21,22,23,24,25,26,],[31,-15,-16,-17,-18,-19,-20,]),'GE':([15,21,22,23,24,25,26,],[32,-15,-16,-17,-18,-19,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'axioma':([0,10,11,],[1,20,20,]),'contenido':([2,9,],[3,12,]),'asignacion':([2,9,],[5,5,]),'valor':([10,11,],[14,27,]),'numero':([10,11,28,29,30,31,32,],[15,15,33,34,35,36,37,]),'comparacion':([10,11,],[16,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> axioma","S'",1,None,None,None),
  ('axioma -> LLAVEA contenido LLAVEC','axioma',3,'p_axioma','ajson_parser.py',14),
  ('axioma -> LLAVEA LLAVEC','axioma',2,'p_axioma','ajson_parser.py',15),
  ('contenido -> asignacion','contenido',1,'p_contenido','ajson_parser.py',26),
  ('contenido -> asignacion COMA','contenido',2,'p_contenido','ajson_parser.py',27),
  ('contenido -> asignacion COMA contenido','contenido',3,'p_contenido','ajson_parser.py',28),
  ('asignacion -> CADENACON PUNTOS valor','asignacion',3,'p_asignacion','ajson_parser.py',39),
  ('asignacion -> CADENASIN PUNTOS valor','asignacion',3,'p_asignacion','ajson_parser.py',40),
  ('valor -> numero','valor',1,'p_valor','ajson_parser.py',45),
  ('valor -> comparacion','valor',1,'p_valor','ajson_parser.py',46),
  ('valor -> NULL','valor',1,'p_valor','ajson_parser.py',47),
  ('valor -> TR','valor',1,'p_valor','ajson_parser.py',48),
  ('valor -> FL','valor',1,'p_valor','ajson_parser.py',49),
  ('valor -> CADENACON','valor',1,'p_valor','ajson_parser.py',50),
  ('valor -> axioma','valor',1,'p_valor','ajson_parser.py',51),
  ('numero -> INT','numero',1,'p_numero','ajson_parser.py',55),
  ('numero -> REAL','numero',1,'p_numero','ajson_parser.py',56),
  ('numero -> NCIENT','numero',1,'p_numero','ajson_parser.py',57),
  ('numero -> BIN','numero',1,'p_numero','ajson_parser.py',58),
  ('numero -> OCT','numero',1,'p_numero','ajson_parser.py',59),
  ('numero -> HEX','numero',1,'p_numero','ajson_parser.py',60),
  ('comparacion -> numero LT numero','comparacion',3,'p_comparacion','ajson_parser.py',65),
  ('comparacion -> numero GT numero','comparacion',3,'p_comparacion','ajson_parser.py',66),
  ('comparacion -> numero EQ numero','comparacion',3,'p_comparacion','ajson_parser.py',67),
  ('comparacion -> numero LE numero','comparacion',3,'p_comparacion','ajson_parser.py',68),
  ('comparacion -> numero GE numero','comparacion',3,'p_comparacion','ajson_parser.py',69),
]
