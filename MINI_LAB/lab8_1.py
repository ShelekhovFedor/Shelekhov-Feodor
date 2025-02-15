#1. В заданном тексте определить частоту, с которой встречаются
# в тексте различные буквы русского алфавита
# (в долях от общего коли-
#чества букв).

q='Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, jy crois)  je ne vous connais plus, vous nêtes plus mon ami, vous nêtes plus мой верный раб, comme vous dites. Ну, здравствуйте, здравствуйте. Je vois que je vous fais peur'
q=q.replace(' ','')
q=q.replace('.','')
q=q.replace(',','')
q=q.replace('(','')
q=q.replace(')','')
w=' а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'
e=w.upper()
r=0
for i in range(len(w)):
    r=r+q.count(w[i])
for i in range(len(e)):
    r=r+q.count(e[i])
t=r/len(q)
print(t)