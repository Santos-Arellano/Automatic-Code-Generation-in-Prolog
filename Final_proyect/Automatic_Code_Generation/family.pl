padre(juan, maria).
padre(pedro, maria).
abuelo(X, Y) :- padre(X, Z), padre(Z, Y).