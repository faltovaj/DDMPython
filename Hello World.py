#!/usr/bin/env python
# coding: utf-8

# # Hello World
# 
# První program v Python. Vyzkoušíme si napsat, uložit a spustit makro.
# 
# Otevřete si editor (např. Idle, Visual Studio Code, Pycharm, Jupyter Notebook). Idle se nainstaluje spolu s instalací Pythonu. Pokud chcete používat jiné editory, tak se je musíte doinstalovat.

# In[1]:


print("Vítám Vás na první hodině programování!")      # vypis pomoci print
print('Vítám Vás na první hodině programování!')      # Uvozovky "" nebo '' jsou zamenne


# *Poznámka*: **Komentáře** se do kódu vpisují za znakem #.

# ## Vstup a výstup
# 
# - **Výstup** pomocí print
# 
# - **Vstup** pomocí input
# 

# In[6]:


input()


# In[5]:


vstup = input("Načítání ze vstupu: ")     # vstup s pruvodnim textem
print('Zadali jste:', vstup, '.')


# **Úkol** Připravte makro, kde:
# - se zeptáme uživatele na jméno
# - pozdravíme uživatele jeho jménem. Příklad výstupu: Ahoj, Jana.

# *Poznámka:* **input vrací typ string** Pokud chceme se vstupem pracovat např. jako s číslem, musíme ho přetypovat.

# In[10]:


vstup = input('Zadejte číslo: ')


# In[5]:


type(vstup)           # Jaky je typ promenne vstup?


# In[6]:


vstup = int(vstup)    # Pretypovani promenne vstup


# In[9]:


type(vstup)


# In[9]:


cislo = input()
cislo = int(cislo2)
cislo


# **Úkol 1** Směnárna: Uživatel by chtěl vyměnit eura na české koruny. Uživatel zadá, kolik EUR chce vyměnit. Program vypíše, kolik CZK dostane. Aktuální kurz a bankovní poplatek si uložte do proměnných.

# In[2]:


eur = int(input())
kurz = 24.1
poplatek = 50
czk = eur*kurz - poplatek
print(czk)


# **Úkol 2** Napište program, který spočítá objem vzduchu v místnosti
# - Zeptejte se uživatele na rozměry místnosti (pomocí input)
# - Spočtěte objem místnosti 
# - Výsledek vypište

# In[ ]:
