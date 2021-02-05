import math

# Deze methode neemt de input lijst van (reële) getallen in en sort deze volgens de "bucket_sort" methode 
def bucket_sort(data):
    # De `data` wordt in een `postives` en `negatives` nummers lijsten verdeeld
    postives, negatives = [x for x in data if x >= 0], [-x for x in data if x < 0]
    # Beide lijsten worden gesorteerd
    sort_list(postives), sort_list(negatives)

    # De `negatives` lijst wordt omgekeerd en van elke element wordt de negatie ervan gepakt
    negatives = list(map(lambda x: -x, reversed(negatives)))
    # De 2 lijsten worden samengevoegd en toegewezen aan `data` op deze manier zodat de interne waarde veranderd 
    # (laten we naar deze manier verwijzen als "indexed assignment" voor het gemak)
    data[:] = negatives + postives

# Deze methode neemt een lijst in en sorteert deze volgens de "bucket_sort" algorithme 
def sort_list(data):
    # Een fail save als de meegegeven lijst leeg is
    if len(data) == 0:
        return

    # `k` staat voor de maximale lengte van een nummer in de lijst
    k = len(max(map(str, data), key=len))
    # `decimal` staat voor de maximale lengte van het kleinste nummer met een decimaal in de lijst
    decimal = len(max(map(str, data), key=len)) - 2

    # Loopen van 0 t/m `k` - 1
    for n in range(k):
        # Elke loop dat we met een base (units, tientallen, hondertallen, etc.) geven we de `bucket` 10 (de getallen 0 t/m 9) lijsten als rijen
        # en in elke rij een lijst als kollom 
        bucket = [[] for y in range(10)]
        # We gaan elke nummer af in de meegegeven lijst
        for number in data:
            # Hier vekrijgen we het huidige nummer in welke base we bezig zijn en slaan het op in `digit` 
            digit = get_digit(number, decimal, n)
            # De `bucket` wordt geïndexeerd met de digit om de `number` in de juiste rij te krijgen, deze wordt vervolgens aan de kolom toegevoegd 
            bucket[digit].append(number)
        # De `bucket` die bestaat uit een 2d lijst wordt samengevoegd tot een lijst met de sum functie en wordt met "indexed assignment" toegewezen
        data[:] = sum(bucket, [])

# Geeft het cijfer op plaats `n` in een `number` terug gegeven deze 2 en de `decimal` voor reële getallen 
def get_digit(number, decimal, n):
    # Doet niks met het nummer als het een type van `int` heeft, 
    # is dat niet het geval wordt deze met de onderstaande formule uitgevoerd zodat het naar een `int` waarde omgezet kan worden
    number = int(round(number * (10 ** decimal), 2)) if type(number) != int else number
    # Nadat we zeker van zijn dat we met een integer werken kunnen we gebruik maken van deze formule,
    # waarbij `n` de plaats van de digit die we willen krijgen uit een nummer is
    return number // 10 ** n % 10
