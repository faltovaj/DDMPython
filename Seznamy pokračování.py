#!/usr/bin/env python
# coding: utf-8

# # Seznamy pokračování
# 
# Ukázka dalších možnosti při používání seznamů.
# 
# ## Řezy (slices)
# 
# Zkopírování části seznamu. Původní seznam zůstane netknutý. Vrací nový seznam.
# 
# seznam\[*i1*:*i2*\]  - vybere prvky ze seznamu od indexu *i1* (včetně) do *i2* (bez).

# In[1]:


seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# In[2]:


seznam [2:6]    # vyber ze seznamu s indexy z intervalu [2,6)


# In[3]:


seznam[:3]     # prefix - indexy [0,3)


# In[4]:


seznam[6:]     # suffix - indexy [6, len(seznam))


# In[5]:


seznam[:]      # kopie seznamu


# In[6]:


seznam[::2]    # vybirame kazdy druhy prvek (zacina od 1. prvku)


# In[7]:


seznam[::-1]   # seznam pozpatku


# ## Operace se seznamy

# In[8]:


seznam = list(range(10))
print(seznam)


# In[9]:


3 in seznam         # Je 3 obsazen v seznamu?


# In[10]:


seznam.pop()        # Odebrani posledniho prvku


# In[11]:


seznam


# In[12]:


seznam.pop(1)       # Odebrani prvku na pozici s indexem 1 (druhy prvek)


# In[13]:


seznam


# In[14]:


seznam.remove(5)    # Odebrani hodnoty 5 ze seznamu


# In[15]:


seznam


# In[16]:


seznam.insert(1, -5)     # Vlozeni hodnoty -5 na druhou pozici (index 1)


# In[17]:


seznam


# In[20]:


seznam1 = [0, 0, 0]
seznam3 = seznam + seznam1        # Seznamy muzeme scitat
print(seznam3)


# In[21]:


seznam3.sort()                   # sort: seradi seznam3
print(seznam3)


# In[22]:


ss = sorted(seznam)              # sorted: vytvori novy serazeny seznam 
print(ss)
print(seznam)


# In[ ]:


help(seznam)            # Help: co muzeme se seznamy provadet


# In[ ]:


help([])          # Jiny zpusob volani HELP


# **Úkoly**    
# Založte si seznam s položkami, které máte ve svém eshopu. Pro jednoduchost budeme uvažovat, že každá položka je na skladu pouze jednou. *Pozn.:* Pokud si chcete úlohu rozšířit, uvažujte také počty jednotlivých položek na skladu.   
# Napište funkce, které provedou následující:   
# - Vypíše seznam všech položek na skladu   
# - Zjistí, jestli je daná položka na skladu nebo ne  
# - Komunikuje se zákazníkem: Zákazník si může buď nechat vypsat seznam položek na skladu nebo si objednat položku. Objednání položky vypadá následovně: Zákazník zadá název položky. Pokud položka na skladě je, tak ji zákazníkovi prodejte (tzn. položku odeberte ze seznamu, případně snižte počet kusů na skladě). Pokud položka na skladě není, tak ji okamžitě objednejte u dodavatele (přidejte na konec seznamu).    

# In[ ]:




