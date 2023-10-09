#!/usr/bin/env python
# coding: utf-8

# # Podmínky
# 
# Podmínky if-else
# 
# **Syntaxe**
# 
# if podminka:   
#    &nbsp; &nbsp; prikazy1  
# else:     
#    &nbsp; &nbsp; prikazy2  
#     
# *Poznámky*
# - Odsazení (typicky 4 mezery) je nutné, aby se příkaz správně přečetl
# - Větev else není nutná, větev if ano

# In[1]:


pozdrav = 'Hello'
# Zeptame se uzivatele na jmeno
jmeno = input('Jak se jmenuješ? ')
# Zeptame se, jestli chce vypsat pozdrav se svym jmenem nebo ne
dotaz = input('Chceš pozdravit jménem (ano/ne)? ')
if dotaz == 'ano':          # == porovnani rovnosti
    print(pozdrav, jmeno)
else:
    print(pozdrav + '!')    # Poznamka: promenne typu string muzeme scitat


# **Úkol 1** Napište program, který bude převádět m na mm, cm a dm
# - Zeptejte se uživatele na počet metrů, které chce převést
# - Dále se zeptejte, na kterou jednotku chce hodnotu převést
# - Pomocı́ podmı́nek if-else určete hodnotu v požadovaných jednotkách (nápověda níže)
# - Výsledek vypište

# In[ ]:


if jednotka == 'm':
    print(metr)
elif jednotka == 'mm':
    print(milimetr)
else:
    print('Jednotku neznam')


# **Úkol 2** Upravte program směnárna tak, aby převáděl z různých měn na CZK. Zeptejte se uživatele, z jaké měny chce převádět. Vypište, kolik CZK uživatel dostane.
