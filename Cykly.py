#!/usr/bin/env python
# coding: utf-8

# # Cykly
# 
# ## For cyklus 
# 
# for i in range(0, 5):    
#     &nbsp; &nbsp; prikazy
# 
# *Poznámky*    
# - Při každém průchodu cyklem se zvětší index *i* o 1     
# - Index *i* v našem případě nabývá hodnot 0, 1, 2, 3, 4     
# - Odsazení je nutné pro správný běh kódu     

# In[1]:


for i in range(0, 5):
    print(i)


# Jaké hodnoty dostaneme s použitím **range**:    
# - range(x, y, n) - generuje celá čísla v rozmezí \[*x*, *y*\), *n* je krok (nepovinný parametr)    
# - range(1, 5) : 1, 2, 3, 4     
# - range(5) : 0, 1, 2, 3, 4 (pokud je zadán jenom jeden parametr, spodní mez je 0)     
# - range(4, 10, 2) : 4, 6, 8 (krok je 2)    
# - range(5, 0, -1) : 5, 4, 3, 2, 1 (krok je -1, čísla se zmenšují)    

# In[2]:


list(range(1,5))      # Pro vypis hodnot generovanych range je nutna konverze na typ list


# **Úkol** Násobilka: Uživatel zadá, násobky jakého čísla (*n*) chce vypsat. Program vypíše násobky do 1.*n* do 10.*n* (např. pro číslo 2 bude výstup 2, 4, 6, 8, 10, 12, 14, 16, 18, 20).

# In[ ]:





# **Úkol** Vypište všechna sudá čísla až do hodnoty zadané uživatelem.

# In[ ]:





# ## While cyklus
# 
# while podminka:    
#     &nbsp; &nbsp; prikazy    
#     
# *Poznámky*    
# - Cyklus probíhá, dokud je splněna *podminka*    
# - Musíme ohlídat, aby nešlo o nekonečný cyklus   
# 
# **Příkaz while-else** else definuje větev, co se provede po skončení cyklu while (bez
# přerušenı́)    
# 
# while podminka:    
#     &nbsp; &nbsp; prikazy    
# else:    
#     &nbsp; &nbsp; prikazKonec
# 
# **Příklad** Výpis čísel od 0 do 4 (včetně) s využitím while-cyklu
# 

# In[3]:


cislo = 0
while cislo < 5:
    print(cislo)
    cislo += 1          # Zkraceny zapis pro cislo = cislo + 1, plati i pro jine operatory


# In[4]:


# Ukazka pouziti while-else
cislo = 0
while cislo < 5:
    print(cislo)
    cislo += 1   
else:              
    print("Cyklus proběhl bez problémů.")


# **Příklad**
# 
# Ze vstupu načtěte posloupnost čísel. Čísla budou zadána každé na samostatné řádce, vstup bude ukončen číslem -1 
# (ta už do posloupnosti nepatří). Dopředu nevíte, kolik čísel bude. Čísla průběžně vypisujte.

# In[5]:


cislo = int(input("Zadejte číslo: "))
while cislo != -1:
    print(cislo)
    cislo = int(input("Zadejte číslo: "))


# ## Užitečné příkazy
# 
# **continue** - přeskočí na další průchod cyklem
# 
# **break** - ukončenı́ cyklu (poznámka: s použitím opatrně)
# 

# **Příklad (continue)** Uživatel zadá číslo. Vypište čísla od 1 do 10 bez čísla zadaného uživatelem.

# In[ ]:


cislo = int(input("Zadejte číslo "))
for i in range(1,11):
    if i == cislo:
        continue
    print(i)


# **Příklad (break)** Uživatel zadává čísla, vstup ukončí -1. Požadujeme, aby zadaná čísla byla menší než 100. Program čísla sečte (poznámka: čísla nebudeme ukládat, ale rovnou přičítat). Pokud uživatel zadá číslo rovno nebo větší než 100, z cyklu vyskočíme pomocí break.

# In[ ]:


cislo = int(input())
suma = 0
while cislo != -1:     # != znamena neni rovno
    if cislo >= 100:
        break
    suma += cislo
    cislo = int(input())
print("Součet čísel je ", suma)


# **Příklad (break)** Načítání řady čísel ukončených -1. Čísla postupně vypisujeme.

# In[1]:


while True:             # Nekonecna smycka
    cislo = int(input("Zadejte číslo: "))
    if cislo == -1:     # Ukonceni smycky
        break
    print(cislo)


# **Úkol** Uživatel zadává celá čísla. Vypisujte zadaná čísla, dokud jsou čísla menší než 80. Po načtení prvního čísla, které je větší nebo rovno 80, ukončete načítání a upozorněte uživatele, že výpis končí. 

# In[ ]:





# **Úkoly**
# 
# Ze vstupu načtěte posloupnost přirozených čísel. Čísla budou zadána každé na samostatné řádce, vstup bude ukončen číslem -1 (ta už do posloupnosti nepatří). Při řešení následujících úloh nepotřebujete ukládat celou číselnou řadu.   
# - Vynásobte všechna zadaná čísla     
# - Najděte nejvyšší číslo v řadě čísel (nápověda: uložte si první číslo jako kandidáta na maximum, porovnávejte aktuálně načtené číslo s kandidátem na maximum - pokud je vyšší, pak máte si uložte tuto hodnotu jako nového kandidáta, pokračujte obdobně až na konec)     
# - Najděte druhé nejvyšší číslo, vypište jeho pozici v řadě    

# In[ ]:




