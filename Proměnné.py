#!/usr/bin/env python
# coding: utf-8

# # Proměnné
# 
# Proměnné používáme na uložení či manipulaci s daty.
# 
# Dosazení hodnoty do proměnné: V příkladu uložíme hodnotu 8 do proměnné *cislo1* a 6 do proměnné *cislo2*. S proměnnými *cislo1* a *cislo2* můžeme dále pracovat (např. provádět aritmetické operace, měnit jejich obsah).

# In[2]:


cislo1 = 8
cislo2 = 6


# *Poznámka 1*: Používejte srozumitelné názvy proměnných, aby bylo zřejmé, co v nich je. Program s proměnnými se jmény *f*, *g*, *e*, *h*, *c* je těžko čitelný.
# 
# *Poznámka 2*: V názvu proměnné nepoužívejte české ani speciální znaky. Je dobrým zvykem, aby název proměnné začínal malým písmenkem. Viz https://peps.python.org/pep-0008/ (Python Style Guide)

# In[3]:


cislo1    # Zkontrolujeme, jaka je hodnota v promenne cislo1


# In[4]:


cislo2    # Jaka je hodnota v promenne cislo2?


# In[8]:


cislo1*cislo2               # Kolik je nasobek cislo1 * cislo2


# In[11]:


soucet = cislo1 + cislo2    # Do promenne soucet ulozime soucet dvou cisel
soucet


# **Úkol** Vyzkoušejte operátory //, %, / a ** na proměnné *cislo1* a *cislo2*. 

# 
# 
# Hodnoty proměnných můžeme měnit 

# In[12]:


cislo1              # Zkontrolujeme, jaka je hodnota promenne cislo1


# In[11]:


cislo1 = 80         # Hodnotu cislo1 zmenime


# In[12]:


cislo1


# In[13]:


cislo1 - cislo2     # Pocitame s novou hodnotou cislo1


# **Úkol** Uložte si hodnotu strany čtverce v cm. Vypočtěte jeho obsah (v $m^2$) a obvod (v $m$).

# **Úkol** Prohoďte obsah dvou proměnných. Příklad: Na začátku máme *promenna1 = 80*, *promenna2 = 6*. Na konci bychom tedy chtěli *promenna1 = 6*, *promenna2 = 80*, aniž bychom "na tvrdo" psali čísla 6 a 80. Nápověda: Pro jednodušší řešení využijte pomocnou proměnnou.

# # Datové typy
# 
# Do proměnné můžeme ukládat různé datové typy. 

# In[14]:


cislo = 123               # Typ int (cele cislo)
cislo_r = 12.8            # Typ float (realne cislo)
text = 'Toto je veta.'    # Typ string (retezec)


# **Přetypování dat** (změna jejich typu):

# In[17]:


cislo = '123'          # Typ string
cislo = int(cislo)     # Typ int

