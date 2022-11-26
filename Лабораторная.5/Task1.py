# TODO решить с помощью list comprehension и распечатать его
import pprint
tmp = []
for i in range(16):
    tmp.append({'bin:': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)})

pprint.pprint([{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)])
pprint.pprint({key: val for key, val in enumerate(range(10))})

