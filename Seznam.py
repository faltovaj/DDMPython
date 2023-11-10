#!/usr/bin/env python
# coding: utf-8

# # Seznamy (lists)
# 
# Seznamy jsou další datový typ, který se používá pro uchování kolekcí dat.
# 
# Seznamy se zadávají do hranatých závorek, jednotlivé prvky jsou odděleny čárkou.
# K jednotlivým prvkům seznamu se dostaneme indexem v \[\], index prvního prvku je 0,
# druhého 1, třetího 2. Poslední prvek seznamu můžeme získat jako prvek s indexem -1.

# In[1]:


cisla = [10, 14, 22, 16 , 8]
print("První prvek ", cisla[0])
print("Třetí prvek ", cisla[2])
print("Poslední prvek ", cisla[-1])


# Prvky seznamu nemusí být stejného typu. Prvek seznamu může být také další seznam.

# In[2]:


mix = [1.3, "hruska", 8, [1, 2]]


# ## Základní příkazy
# 
# Příkazy
# - len(seznam) - vrací počet prvků seznamu
# - seznam.append - přídání prvku na konec seznamu

# In[4]:


seznam = ['chleba', 'jablka', 'jogurt']


# In[5]:


len(seznam)       # pocet prvku seznamu


# In[6]:


seznam.append('ananas')      # pridani prvku na konec seznamu
seznam


# In[7]:


len(seznam)


# **Příklad** Uživatel zadává posloupnost čísel ukončených číslem -1. Načtěte zadaná čísla do seznamu.

# In[8]:


seznam = []       # vytvoreni prazdneho seznamu
while True:
    cislo = int(input())
    if cislo == -1:
        break
    seznam.append(cislo)
print(seznam)


# ## Procházení seznamu
# 
# Procházení seznamu prvek po prvku

# In[9]:


# prochazeni primo pres jednotlive prvky (bez vyuziti indexu) 
seznam = ['chleba', 'jablka', 'jogurt', 'ananas']
for p in seznam:      
    print(p)


# In[ ]:


# prochazeni s vyuzitim indexu
seznam = ['chleba', 'jablka', 'jogurt', 'ananas']
for i in range(len(seznam)):     # index bezi od 0 do poctu prvku seznamu -1      
    print(seznam[i])


# **Úkoly**
# Připravte si seznam přirozených čísel a proveďte následující:    
# - Vypište každé druhé číslo   
# - Vypište násobky čísla 3 v seznamu    
# - Najděte první (druhé) minimum, vypište jeho pozici v seznamu    
# - Určete počet čísel menších než 100

# In[ ]:





# ## POZOR: seznamy v Pythonu fungují jako odkazy
# 
# Ukázka níže

# In[4]:


# Cisla funguji jak predpokladame
cislo1 = 10
cislo2 = cislo1    # Vytvori se nove misto v pameti
print(cislo1)
print(cislo2)


# In[5]:


cislo1 = 10000
print(cislo1)
print(cislo2)


# In[2]:


seznam1 = ['chleba', 'jablka', 'jogurt', 'ananas']
seznam2 = seznam1                 # Do promenne seznam2 ulozim seznam1 (odkaz)
print("První seznam ", seznam1)
print("Druhý seznam ", seznam2)


# In[3]:


seznam1[2] = "šunka"             # Zmena v seznam1 zmeni obsah seznam2
print("První seznam ", seznam1)
print("Druhý seznam ", seznam2)


# *Poznámka* Jak zkopírovat hodnoty? Využijte deepcopy (budete potřebovat importovat modul copy).

# In[6]:


import copy
seznam1 = ['chleba', 'jablka', 'jogurt', 'ananas']
seznam2 = copy.deepcopy(seznam1)
print("První seznam ", seznam1)
print("Druhý seznam ", seznam2)

seznam1[2] = "šunka"             # Zmena v seznam1 nezmeni obsah seznam2
print("Po změně seznam1:")
print("První seznam ", seznam1)
print("Druhý seznam ", seznam2)


# **Úkoly**
# Je zadaná posloupnost čísel ve formě seznamu. Proveďte následující:    
# - Sečtěte zadaná čísla
# - Vyměňte první a poslední člen posloupnosti
# - Vypište posloupnost pozpátku
# - Připravte dva nové seznamy. Do jednoho uložte všechna sudá čísla původní posloupnosti, do druhého všechna lichá. 

# In[ ]:




