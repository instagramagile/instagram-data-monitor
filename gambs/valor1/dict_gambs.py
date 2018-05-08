import re

d = {}

d['\\u00c7'] = 'Ç'
d['\\u00e7'] = 'ç'


d['\\u00c0'] = 'À'
d['\\u00c1'] = 'Á'
d['\\u00c2'] = 'Â'
d['\\u00c3'] = 'Ã'
d['\\u00c4'] = 'Ä'


d['\\u00e0'] = 'à'
d['\\u00e1'] = 'á'
d['\\u00e2'] = 'â'
d['\\u00e3'] = 'ã'
d['\\u00e4'] = 'ä'



d['\\u00c8'] = 'È'
d['\\u00c9'] = 'É'
d['\\u00ca'] = 'Ê'
d['\\u00cb'] = 'Ë'

d['\\u00e8'] = 'è'
d['\\u00e9'] = 'é'
d['\\u00ea'] = 'ê'
d['\\u00eb'] = 'ë'



d['\\u00cc'] = 'Ì'
d['\\u00cd'] = 'Í'
d['\\u00ce'] = 'Î'
d['\\u00cf'] = 'Ï'

d['\\u00ec'] = 'ì'
d['\\u00ed'] = 'í'
d['\\u00ee'] = 'î'
d['\\u00ef'] = 'ï'


d['\\u00d2'] = 'Ò'
d['\\u00d3'] = 'Ó'
d['\\u00d4'] = 'Ô'
d['\\u00d5'] = 'Õ'
d['\\u00d6'] = 'Õ'

d['\\u00f2'] = 'ò'
d['\\u00f3'] = 'ó'
d['\\u00f4'] = 'ô'
d['\\u00f5'] = 'õ'
d['\\u00f6'] = 'õ'




d['\\u00d9'] = 'Ù'
d['\\u00da'] = 'Ú'
d['\\u00db'] = 'Û'
d['\\u00dc'] = 'Ü'

d['\\u00f9'] = 'ù'
d['\\u00fa'] = 'ú'
d['\\u00fb'] = 'û'
d['\\u00fc'] = 'ü'

dic = d # apenas um alias, para ficar mais mnempnico

# constante para somar com o inicio: 6

def utf8_to_utf8_right(string):
	global dic
	idx = []
	iterator = re.finditer('\\\\u....', string)
	idx = [i.start() for i in iterator]
	if len(idx) == 0:
		return string  # se nao tem utf8 zuado, a string jah estah certa
	i = 0
	right_string = ''
	for j in idx: # onde começa o slice
		fatia = string[j:j+6]
		utf_right = dic[fatia]
		right_string = right_string + string[i:j] + utf_right		
		i = j+6
	right_string = right_string + string[ j+6 : ]
	return right_string
