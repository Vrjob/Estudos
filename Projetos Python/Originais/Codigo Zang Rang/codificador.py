a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8

i = 9
j = 9

k = 10
l = 11

m = 12
n = 12

o = 13

p = 14
q = 14

r = 15
s = 16
t = 17
u = 18

v = 19
w = 19

x = 20
y = 21
z = 22
class Letter:
    def __init__(self,letra,id_letra):
        self.letra = letra
        self.id_letra = id_letra
    def contadorzinho(self):
        if self.letra == " ":
            contadorID = -1
        else:
            contadorID += 1        
#self.slipt() ajuda a separar nomes
a = Letter ("a",1)
contadorID = 0
space = Letter(' ',0)

contador = 0
texto = "caixas azuis"

while contador < len(texto):
    if texto[contador] == a.letra:
        print(texto[contador])
    contador += 1










