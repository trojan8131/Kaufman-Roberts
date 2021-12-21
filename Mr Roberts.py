def roberts(n, a, t, v):
    if n < 0 or n > v:
        return 0 
    elif n == 0:
        return 1 #Nie mozna dzielić przez zero 
    else:
        suma=0
        m=len(a)
        for i in range(0,m):
            suma+=t[i]*a[i]*roberts(n-t[i],a,t,v)
        return (1/n)*suma
 
def prawdopodbienstwo(n, a, t, v):
    suma=0
    for g in range(0, v + 1):
        suma+=roberts(g,a,t,v)
    
    return roberts(n,a,t,v)/suma
def e(a, t, v, y):
    suma=0
    for n in range(v-t[y]+1,v+1):
        suma+=prawdopodbienstwo(n, a, t, v)
    return suma

a_li = []#Tablica z parametrem A - oferowanych ruch dla danej klasy
t_li = []#tablica z parametrem t- liczba adanych jednostek dla danej klasy 
m = int(input("Podaj liczbę klas M: "))
v = int(input("Pojemność systemu V: "))
for i in range(0, m):
    print("Dla M=",i+1)
    a_li.insert(i, float(input("Podaj oferowany ruch klasy M="+str(i+1)+", A: ")))
    t_li.insert(i, int(input("Podaj liczbę żądanych jednostek alokacji dla klasy M="+str(i+1)+", t: ")))
print("")
print("")
print("Rozkład zajętości, prawdopodobieństwo zajętości n")
#n-liczba zajętych jednostek systemu
for n in range(0, v + 1):
    print("P(",n,") = ",prawdopodbienstwo(n, a_li, t_li, v))  # wyswietla prawdopodobieństwo dla kazdego n
print("")

print("Prawdopodobieństwo blokady")
for y in range(0, m):  # wyswietla kazde E
    print("E(",y+1,")= ", e(a_li, t_li, v, y))
