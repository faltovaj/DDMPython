#!/usr/bin/env python
# coding: utf-8

# # Práce se soubory
# 
# Soubor: posloupnost bajtů    
# 
# Textové soubory: Znaky převedené na bajty kódováním    
# 
# Příklady kódování    
# - ACII (anglické znaky, interpunkce, 95 znaků)    
# - iso-8859-2 (ASCII rozšířené o znaky východoevropských jazyků)    
# - cp1250 (Windows, obdobné iso-8859-2)    
# - utf-8 (obsahuje znaky většiny jazyků, vícebajtové znaky)    
# 
# Znak konce řádků   
# - Různé operační systémy ukončují řádky různě     
# - znak '\n' (newline)    

# ## Posloupnost úkonů
# 
# - Otevřu soubor       
# - Provedu, co potřebuji  
# - Zavřu soubor   
# 
# Vyhledejte na Wikipedii pojem 'textový soubor'. Část si zkopírujte a uložte do souboru jménem soubor.txt. 
# 
# Pokud máte soubor uložený ve stejném adresáři jako spouštíte svá makra, stačí jmeno souboru uvést v rutině open(). Pokud máte soubor uložený v jiném adresáři, musíte uvést cestu k souboru. 

# In[1]:


f = open('soubor.txt', 'r')    # otevreni souboru ke cteni
# Pokud se dobre nenacetly ceske znaky, zadejte kodovani souboru
#f = open('soubor.txt', 'r', encoding = 'utf-8')i souboru
obsah = f.read()               # nacteni obsahu celeho souboru do promenne
f.close()                      # zavreni souboru
print(obsah)


# ### Pokud se nechcete starat o zavření souboru, použijte 'with open'

# In[4]:


# Zavreni souboru probehne v tomto pripade automaticky
with open('soubor.txt', 'r') as f:
    obsah = f.read()


# Načítání souboru po řádcích (např. příliš dlouhý soubor)

# In[5]:


with open('soubor.txt', 'r') as f:
    for line in f:
        print(line.split())


# In[ ]:





# ## Parametry open
# 
# - jméno souboru    
# - mód přístupu    
#      - r (read) – čtení    
#      - w (write) – zápis (založí nový nebo přepíše starý soubor)     
#      - a (append) – zápis na konec souboru (založí nový nebo připíše na konec souboru)    
#      - r+ /w+ – čtení i zápis    
# - encoding – nepovinný parametr, kódování (defaultně podle OS)     
# 

# In[ ]:





# ## Co můžeme dělat se soubory

# Se souborem *f* můžeme       
# - f.write(text) - zápis textu do souboru   
# - f.read(n) - přečte dalších n znaků (od místa, kde jsme zrovna skončili)   
# - f.read() - přečte všechny znaky do konce souboru (opět od místa, kde jsme skončili)     
# - f .readline() - přečte další řádek (včetně znaku konce řádku); pokud jsme na konci souboru, vrátí ""     
# 
# Dále můžete využít např.        
# - print('Ahoj!', file = f) - zápis do souboru *f* místo konzule    
# - for line in f: - cyklus přes řádky souboru   
# - line.rstrip() - zbaví řádky bílých znaků na konci řetězce (mezery, tabulátory, konce řádků) 

# In[ ]:





# ## Úkoly
# 
# Proveďte následující s textovým souborem:    
# - zjistěte počet řádku, slov a viditelných znaků (nepočítáme mezery, tabulátory, konce řádků)    
# - zkopírujte každou druhou větu do nového souboru. Předpokládejte, že všechny věty končí '.'    
# - najděte v souboru všechna čísla a zapište je do nového souboru. Při zápisu zachovejte řádky jako v původním souboru (pokud na řádku není žádné číslo, vypište prázdný řádek; pokud jsou na řádku dvě čísla, vypište je na jeden řádek atd.). Může se hodit metoda isdigit() pro řetězce.    

# In[ ]:


with open('soubor.txt', 'r') as f:
    obsah = f.read()
    radky = obsah.split('\n')
    pocetSlov = 0;
    pocetZnaku = 0;
    for r in radky:
        slova = r.split()
        if len(slova) > 0:
            pocetSlov += len(slova)
            for p in slova:
                pocetZnaku += len(p)
    
print(f'Pocet radku je {len(radky)}.')
print(f'Pocet slov je {pocetSlov}.')
print(f'Pocet znaku je {pocetZnaku}.')


# In[ ]:


with open('soubor.txt', 'r') as fr, open('novySoubor.txt', 'w') as fw:
        obsah = fr.read()
        veta = obsah.split('.')
        for i in range(len(veta)):
            if i%2 == 0 and len(veta[i].split())>0:
                # split pro odstraneni mezery za tecku
                veta[i] = " ".join(veta[i].split())
                fw.write(f'{veta[i]}.\n')


# In[ ]:


with open('soubor_v1.txt', 'r') as fr:
    with open('cisla.txt', 'w') as fw:
        for line in fr:
            cisla = []
            line = line.split()
            if len(line)>0:
                # cisla si ulozim do seznamu
                cisla = [l for l in line if l.isdigit()]
            # ze seznamu udelam string a ten zapisu
            # zapis ukoncim znakem pro konec radku
            fw.write(" ".join(cisla) + '\n')


# In[ ]:




