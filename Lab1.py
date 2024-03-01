

def reflexive(rel):
    for i in range(len(rel)):
        if rel[i][i] == 1:
            return("Reflexive")        
        return("Not reflexive")

def antireflexive(rel):
    for i in range(len(rel)):
        if rel[i][i] != 0:
            return("Not antireflexive")
        return ("Antireflexive")

def symmetric(rel):
    for i in range(len(rel)):
        for j in range(len(rel)):
            if rel[i][j] != rel[j][i]:
                return "Not symmetric"
    return "Symmetric"

def asymmetric(rel): 
    for i in range(len(rel)):
        for j in range(len(rel)):
            if rel[i][j] == 1 and rel[j][i] == 1:
                return "Not unsymmetric"
    return "Asymmetric"

def antisymmetric(rel):
    for i in range(len(rel)):
        for j in range(len(rel)):
            if i != j and rel[i][j] == 1 and rel[j][i]:
                return "Not antisymmetric"
    return "Antisymmetric"
                    
def transitive(rel):
    for i in range(len(rel)):
        for j in range(len(rel)):
            for k in range(len(rel)):
                if rel[i][j] == 1 and rel[j][k] == 1 and rel[i][k] != 1:
                    return "Not transitive"
    return "Transitive" 

def the_best(rel):
    best_elements = [row_index for row_index in range(len(rel)) if all(element == 1 for element in rel[row_index])] 
    
    if not best_elements or len(best_elements) > 1:
        return "No best element"  
    return f"Best element: {best_elements[0]}"

def the_worst(rel):
    worst_elements = [col_index for col_index in range(len(rel[0]) - 1, -1, -1) 
            if all(row[col_index] == 1 for row in rel)]
    
    if not worst_elements or len(worst_elements) > 1:
       return "No worst element"
    return f"Worst element: {worst_elements[0]}"

def rel_strict(rel):
    strict_rel = [[element for element in row] for row in rel]

    for i in range(len(strict_rel)):
        for j in range(len(strict_rel)):
            if strict_rel[i][j] == 1 and strict_rel[j][i] == 1:
                strict_rel[i][j] = 0
                strict_rel[j][i] = 0

    return strict_rel           
            
def min(strict_rel):

    min_elements = []
    for row_index, row in enumerate(strict_rel):
        if all(element == 0 for element in row):
            min_elements.append(row_index + 1)

    if min_elements:
        return f"Min elements: {min_elements}"
    return "No min elements"

def max(strict_rel):

  max_elements = []

  for col_index in range(len(strict_rel[0])):
    if all(row[col_index] == 0 for row in strict_rel):
      max_elements.append(col_index + 1)

  if max_elements:
    return f"Max elements: {max_elements}"
  return "No max elements"

def converse(rel):
    converse_rel = [[element for element in row] for row in rel]

    for i in range(len(converse_rel)):
        for j in range(i + 1, len(converse_rel)):  
            if converse_rel[i][j] != converse_rel[j][i]:
                converse_rel[i][j], converse_rel[j][i] = converse_rel[j][i], converse_rel[i][j]

    return f"Converse: {converse_rel}"

def complementary_rel(rel):
    complementary = [[element for element in row] for row in rel]

    for i in range(len(complementary)):
        for j in range(len(complementary)):
            complementary[i][j] = 1 - complementary[i][j]  

    return  f"Complementary: {complementary}"

relation = [[1, 0, 0, 1, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1]]

print(reflexive(relation))
print(antireflexive(relation))
print(symmetric(relation))
print(asymmetric(relation))
print(antisymmetric(relation))
print(transitive(relation))

print(the_worst(relation))
print(the_best(relation))

strict_rel = rel_strict(relation) 
print(min(strict_rel))
print(max(strict_rel))

print(converse(relation))

print(complementary_rel(relation))



