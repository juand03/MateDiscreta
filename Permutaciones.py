"Las siguientes personas se inscribieron en una carrera :"
"Juan, Carlos, Laura, Eduardo, Roger "

"Esto va a mostrar todos los posibles resultados que se pueden dar en esta competencia"
"Es decir, el orden en que pueden llegar a la meta"

Personas=["Juan","Carlos","Laura","Eduardo","Roger"]

contador=0

for i in Personas:
    for j in Personas:
        for k in Personas:
            for m in Personas:
                for n in Personas:
                    if i !=j and i != k and i !=m and i != n and\
                        j !=k and j !=m and j !=n and \
                        k != m and k !=n and m != n:
                        orden1= [i,j,k,m,n]
                        contador += 1
                        print("{:3d} :{}". format(contador, orden1))

