#!/usr/bin/env python
# coding: utf-8

# # Funkce
# 
# Používání funkcí zvyšuje přehlednost kódu. Výhodou funkce je, že ji napíšete pouze jednou, ale spustit (volat) ji můžete vícekrát.   
# 
# Syntaxe 
# 
# def funkce():   
#     &nbsp; &nbsp; prikazy
# 
# *Poznámky*   
# - Klíčové slovo def, závorky pro definici funkce i pro volání nutné    
# - Funkce musí být definovaná před prvním voláním, typicky jsou všechny funkce uvedeny na začátku skriptu    
# - Dbejte na srozumitelné pojmenování funkcí, název funkce začíná typicky malým písmenem

# In[1]:


def helloWorld_v0():
    print("Hello!")


# In[3]:


helloWorld_v0()
helloWorld_v0()


# ## Funkce s parametrem
# 
# Funkce mohou mít parametr, se kterým se volají.
# 
# Parametry používané uvnitř funkce (v naší ukázce níže parametry *i* a *n*) jsou dostupné pouze uvnitř funkce. Zvenku se k nim nemůžeme dostat. To je obvykle požadované chování. 

# In[5]:


def helloWorld_v1(n):
    for i in range(n):
        print("Hello!")


# In[6]:


helloWorld_v1(3)
print("Dalsi volani")
helloWorld_v1(1)


# Parametr funkce může být povinný (viz výše) či nepovinný (ukázka níže). Nepovinným parametrům přiřazujeme 
# základní hodnotu.

# In[7]:


def helloWorld_v2(n=1, pozdrav="Hello"):
    for i in range(n):
        print(pozdrav)


# Možnosti volání funkce s nepovinnými parametry:

# In[8]:


helloWorld_v2()


# In[9]:


helloWorld_v2(2)


# In[10]:


helloWorld_v2(2,'Ahoj :)')


# In[11]:


helloWorld_v2(n=4, pozdrav='Nazdárek!')


# In[12]:


helloWorld_v2(pozdrav='Čau')


# **Úkoly**    
# Napište funkci, která    
# - spočítá, kolik je v seznamu sudých čísel   
# - vybere ze seznamu sudá čísla 
# - dostane dva seřazené seznamy čísel a vypíše jejich průnik   
# - vypočte alternující ciferný součet (pro čı́slo 8643 bude výsledek 8 − 6 + 4 − 3 = 3)   

# In[14]:


def kolikSudych(seznam):
    pocet = 0
    for i in seznam:
        if i%2==0:
            pocet += 1
    print(pocet)


# In[15]:


s = [3, 6, 8, 11, -4, 6]
kolikSudych(s)


# In[9]:


zoznam2=[1,2,3,4,5,6,7,8,9,10,11,12]
zoznam = [7,9,12,20,21,64,5]

def prienik():
    zoznam3 = []
    for p in zoznam:
        for h in zoznam2:
            if p == h:
                zoznam3.append(p)
                break
                
    return zoznam3

print(prienik())
print(prienik())


# In[16]:


seznam=[1,2,3,4,5,6,7,8,9,10,11,12]
seznam2 = [5,7,9,12,20,21,64]

def prienik(zoznam, zoznam2):
    zoznam3 = []
    for p in zoznam:
        for h in zoznam2:
            if p == h:
                zoznam3.append(p)
                break
                
    return zoznam3

prienik(seznam, seznam2)
prienik(seznam, seznam2)


# ## Funkce s výsledkem
# 
# Funkce může také vracet hodnotu (hodnoty). Typ proměnné, kterou funkce vrací není omezen. Může vracet např. celé číslo, řetezec, seznam.  
# 
# Klíčové slovo pro vracení hodnoty je **return** - ukončí funkci a vrátí výsledek. Pokud je použit **return** bez výsledku, vrací se typ None. 

# In[19]:


def soucet(cislo1, cislo2):
    return cislo1 + cislo2
    print('Vypis uvnitr funkce')


# In[22]:


suma = soucet(1, 100)
print(suma)


# Pokud chceme vrátit více hodnot, můžeme vrátit jednotlivé hodnoty oddělené čárkou (typ tuple).

# In[23]:


def serad(cislo1, cislo2):                
    if cislo1<cislo2:
        return cislo1, cislo2
    else:
        return cislo2, cislo1


# In[23]:


serad(2,2)


# In[25]:


a, b = serad(10,8)
print(a)
print(b)


# In[25]:


serad(8,10)


# **Úkoly**   
# Napište funkci, která     
# - vrátí n-té Fibonacciho číslo (F (0) = 0, F (1) = 1, F (n) = F (n − 1) + F (n − 2))
# - vrátí n-faktoriál (n! = n\*(n-1)\*(n-2)\*....\*2\*1)   
# - dostane koeficienty kvadratické rovnice ax^2 + bx + c = 0 a vrátí seznam jejích kořenů (na množině reálných čísel)
# 

# In[23]:


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fn_2 = 0
    fn_1 = 1
    for i in range(n-1):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn


# In[25]:


fibonacci(8)


# In[27]:


def kvadraticka(a,b,c):
    D = b**2 - 4*a*c
    if D < 0:
        return("Rovnice nema v R reseni.")
    else:
        return((-b+D**0.5)/(2*a),(-b-D**0.5)/(2*a))

print(kvadraticka(1,-5,6))


# ## Globální proměnné
# 
# Funkce může načíst i proměnné vně funkce, ale pouze pokud do nich nic nepřiřazuje (nemění je).
# 
# Pokud potřebujeme, aby se při běhu funkce změnil parametr definovaný mimo funkci, použijeme klíčové slovo **global**. 
# 
# **UPOZORNĚNÍ** S globálními proměnnými opatrně, ať si nepřepíšete proměnnou, kde to nečekáte....
# 
# **Příklad**:
# - Funkce načte globální proměnnou *jmeno*   
# - Proměnnou *pocetClenu* potřebujeme definovat jako globální    

# In[10]:


jmeno = 'Novak'
pocetClenu = 12

def pridaniClena():
    print(jmeno)                                      # promennou jmeno funkce zna
    print('Počet členů před změnou', pocetClenu)      # promennou pocetClenu funkce zna
    pocetClenu += 1                                   # hodnotu promenne pocetClenu funkce nemuze menit
    print('Počet členů pro změně', pocetClenu)  
        
pridaniClena()


# In[11]:


jmeno = 'Novak'
pocetClenu = 12

def pridaniClena(jmeno):
    global pocetClenu                                 # promenna pocetClenu jako globalni promenna
    print(jmeno)                                      # promennou jmeno funkce zna
    print('Počet členů před změnou', pocetClenu)      # promennou pocetClenu funkce zna
    pocetClenu += 1                                   # hodnotu promenne pocetClenu funkce uz menit muze
    print('Počet členů pro změně', pocetClenu)  
    
pridaniClena(jmeno)
print('Kontrola: Počet členů', pocetClenu)


# **Řešení bez globálních proměnných:**

# In[32]:


jmeno = 'Novak'
pocetClenu = 12

def pridaniClena(name):                                 
    print(name)
    return 1
    
pocetClenu += pridaniClena(jmeno)
print('Kontrola: Počet členů', pocetClenu)


# ## Další
# 
# Vracení více hodnot

# In[14]:


def aritmetika(a, b):
    soucet = a + b
    rozdil = a - b
    nasobek = a*b
    return soucet, rozdil, nasobek

pocitani = aritmetika(8,10)
print(pocitani)
print(f'rozdil: {pocitani[1]}.')
    


# In[17]:


#Ukazka: Prohozeni dvou hodnot
cislo1 = 10
cislo2 = 100

print('Pred prohozenim: ', cislo1, cislo2)
cislo1, cislo2 = cislo2, cislo1
print('Po prohozeni: ', cislo1, cislo2)


# # Úkoly   
# 
# Napište funkci, která    
# - vrátí počet sudých čísel v seznamu (parametr funkce bude seznam)    
# - vrátí seznam sudých čísel v seznamu (parametr funkce bude seznam, vrátí se nový seznam)    
# - zjistí, zda je dané číslo prvočíslo (vratí True-False)    
# - vypíše všechna prvočísla do zadaného čísla (včetně)    

# **Další úkoly**   
# 
# Napište funkci, která    
# - vypočítá obsah obdélníka (parametry funkce budou strany obdélníka)    
# - rozmění částku na drobné (parametr funkce bude částka na rozměnění, výstup bude počet 50-ti korun, 20-ti korun, ..., 1 korun)    
# - vypočte průměrnou známku ze seznamu známek (parametr funkce bude seznam známek)   
# - načte seznam čísel zadávaných po jednom uživatelem do seznamu. Načítání je ukončeno -1, ta už do seznamu nepatří (funkce nebude mít vstupní parametr, bude vracet seznam čísel)  
# - převede teplotu v Kelvinech nebo Fahrenheitech na teplotu ve stupních Celsia (funkce bude mít dva parametry - číselnou hodnotu teploty a údaj, jestli jde o teplotu v Kelvinech či Fahrenheitech)    

# In[ ]:




