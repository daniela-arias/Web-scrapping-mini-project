import re
def limpiar(x):
    diccionario = {"Sombrero":re.search(".*[Ss](ombrero|OMBRERO).*",str(x)),
                   "Mochila":re.search(".*[Mm](ochila|OCHILA).*",str(x)),
                   "Bolso":re.search(".*[Bb](olso|OLSO).*",str(x)),
                   "Gorro":re.search(".*[Gg](orro|ORRO).*",str(x)),
                   "Botas":re.search(".*[Bb](otas|otas).*",str(x)),
                   "Anillos":re.search(".*[Aa](nillos|NILLOS).*",str(x)),
                   "Zapatillas":re.search(".*[Zz](apatillas|APATILLAS).*",str(x)),
                   "Botines":re.search(".*[Bb](otines|OTINES).*",str(x)),
                   "Guantes":re.search(".*[Gg](uantes|UANTES).*",str(x)),
                   "Bufanda":re.search(".*[Bb](ufanda|UFANDA).*",str(x)),
                   "Paraguas":re.search(".*[Pp](araguas|ARAGUAS).*",str(x)),
                   "Pendientes":re.search(".*[Pp](endientes|ENDIENTES).*",str(x)),
                   "Bailarinas":re.search(".*[Bb](ailarinas|AILARINAS).*",str(x)),
                   "Fundas Movil":re.search(".*[Ff](undas|UNDAS).*",str(x)),
                   "Boina":re.search(".*[Bb](oina|OINA).*",str(x)),
                   "Accesorios cabello":re.search(".*[Pp](elo|ELO).*",str(x)),
                   "Mules":re.search(".*[Mm](ules|ULES).*",str(x)),
                   "Cinturon":re.search(".*[Cc](inturon|INTURON).*",str(x)),
                  }

    for key,values in diccionario.items():
        if values:
            return key
    return 'Otros Accesorios'