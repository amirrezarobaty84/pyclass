#dar in tamrin bayad mavared zir ra hesab konim :
#ejtema
#eshtrak
#tafazol

physic1 = {'Ali','Hassan', 'Saman', 'Sina', 'Ahmad'}
math1 = {'Saman', 'Mohammadreza', 'Ahmad', 'Aria'}

union = physic1.union(math1)
len_union = len(union)

intersection = physic1.intersection(math1)
len_intersection =len(intersection)

tafazol = physic1 - math1
len_tafazol = len(tafazol)

print(f"ejtema in 2 kelas barabar ba {len_union} \n\
va asami daneshjo ha barabar ba {union}\n")

print(f"eshterak in 2 kelas barabar ba {len_intersection} \n\
va asami daneshjo ha barabar ba {intersection}\n")

print(f"tedad daneshjo haye ke fghat dar physic1 hastand barabar ba {len_tafazol} \n\
va asami daneshjo ha barabar ba {tafazol}\n")
