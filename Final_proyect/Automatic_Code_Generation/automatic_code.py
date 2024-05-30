from pyswip import Prolog

""" Stay hard """

# Inicializar el motor Prolog
prolog = Prolog()

# Cargar el archivo con las reglas en Prolog
prolog.consult("family.pl")

# Realizar consultas en Prolog desde Python
for soln in prolog.query("abuelo(X, Y)"):
    print(soln["X"], "es abuelo de", soln["Y"])