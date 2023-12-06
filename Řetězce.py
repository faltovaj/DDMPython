#!/usr/bin/env python
# coding: utf-8

# # Řetězce (string)
# 
# Základy práce s řetězci (slova, věty, texty). 
# 
# Velmi podobné manipulaci se seznamy. Hlavní rozdíl: řetězec se nedá přepisovat znak po znaku (tzv. immutable object).
# 

# In[1]:


slovo = 'python'
slovo2 = "Python"


# In[2]:


len(slovo)       # pocet znaku


# In[3]:


slovo[2]         # znak na 3. miste


# In[4]:


slovo[:3] + 'el'        # rezy funguji, retezce muzeme scitat


# In[5]:


slovo = 'nove slovo'    # muzeme "prepsat" cely retezec
print(slovo)


# In[6]:


slovo[1] = 't'          # nemuzeme menit retezec po znacich


# In[7]:


for p in slovo:         # prochazeni retezce po jednotlivych znacich
    print(p)


# In[18]:


seznam = list(slovo)
seznam[4] = '+'
print(seznam)


# In[22]:


retezec = "".join(seznam)
print(retezec)


# In[20]:


print("-".join(seznam))


# ## Operace specifické pro řetězce
# 
# Malá ukázka, více najdete v dokumentaci (help).

# In[8]:


'kapitalky'.upper()


# In[9]:


'MALE'.lower()


# In[27]:


odpoved = input('ano/ne? ')
if odpoved.lower() == 'ano':
    print('Ano')
else:
    print('Ne')


# In[28]:


'schovavana'.find('va')       # Vraci index prvniho vyskytu


# In[11]:


'schovavana'.find('ananas')   # -1 pokud podretezec nenajde


# In[12]:


'Rozdel tuto vetu.'.split()   # rozdeleni po slovech; split: casto pouzivane ...


# In[30]:


rada = input('Zadejte cisla na jednu radku: ')
cisla = rada.split()
cisla2 = [int(p) for p in cisla]     # Priste (list comprehensions)
print(cisla2)


# In[31]:


'1+2+3'.split(sep='+')       # rozdeleni se separatorem +


# In[14]:


'+'.join(['1','2','3'])      # spojeni znakem +


# In[ ]:


help(str)


# In[ ]:


help('')


# **Úkol** Hra šibenice -- umrlce najdete níže
# 
# **Další úkoly** Napište funkci, která    
# - spočítá, kolik zadaný řetězec obsahuje slov (oddělených mezerami)    
# - spočítá, kolik různých slov se vyskytuje v zadaném řetězci. Ošetřete tak, aby např. ’Test’ a ’test’ bylo považováno za stejné slovo.    
# - vyhodnotí výraz se sčítáním. Příklad: vstup z klávesnice bude 12+34+1 (jeden výraz), výstup bude číslo 47. Použijte funkci split se separátorem.   

# In[ ]:


sibenice = [
"             \n             \n             \n             \n             \n_____________",
"             \n             \n             \n             \n             \n___|_________",
"             \n             \n             \n             \n   |         \n___|_________",
"             \n             \n             \n   |         \n   |         \n___|_________",
"             \n             \n   |         \n   |         \n   |         \n___|_________",
"             \n   |         \n   |         \n   |         \n   |         \n___|_________",
"   _         \n   |         \n   |         \n   |         \n   |         \n___|_________",
"   __        \n   |         \n   |         \n   |         \n   |         \n___|_________",
"   ___       \n   |         \n   |         \n   |         \n   |         \n___|_________",
"   ____      \n   |         \n   |         \n   |         \n   |         \n___|_________",
"   _____     \n   |         \n   |         \n   |         \n   |         \n___|_________",
"   _____     \n   |    |    \n   |         \n   |         \n   |         \n___|_________",
"   _____     \n   |    |    \n   |    O    \n   |         \n   |         \n___|_________",
"   _____     \n   |    |    \n   |    O    \n   |   -     \n   |         \n___|_________",
"   _____     \n   |    |    \n   |    O    \n   |   -|    \n   |         \n___|_________",
"   _____     \n   |    |    \n   |    O    \n   |   -|-   \n   |         \n___|_________",
"   _____     \n   |    |    \n   |    O    \n   |   -|-   \n   |   /     \n___|_________",
"   _____     \n   |    |    \n   |    O    \n   |   -|-   \n   |   / \  \n___|_________"
]


# In[ ]:




