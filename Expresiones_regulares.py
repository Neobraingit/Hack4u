
#!/usr/bin/env python3

import re

texto =  ('Mi gato está en el tejado y mi otro gato está en el jardín')

matches = re.findall('gato', texto)

print (matches)

texto2 = 'Hoy estamos a 30/11/2024 y mañana estaremos a 01/12/2024'

coincidencias = re.findall('\d{2}\/\d{2}\/\d{4}', texto2)

print (coincidencias)



