import re
begin_encountered = False
results = []

def process_command(input_str):
 global begin_encountered
 if input_str.startswith('Set'): #### Set
    match = re.fullmatch(r'^Set\s*([a-zA-Z][a-zA-Z0-9]*)\s* [+-]?\d+(\.\d*)?\s*\$$', input_str)
    if match:
        id, number = match.groups()
        if '.' in (number or ''):
            print(f"affectation d'un float à un id: {id}")
        else:
            print(f"affectation d'un entier à un id: {id}")
    else:
        if not re.search(r'^Set\s*[a-zA-Z][a-zA-Z0-9]*', input_str):
            print("Erreur: Identifiant manquant")
        elif not re.search(r'^Set\s*([a-zA-Z][a-zA-Z0-9])*\s*\d+', input_str):
            print("Erreur: Nombre manquant")
        elif not re.search(r'\$$', input_str):
            print("Erreur: Le symbole $ est manquant")
        else:
            print("Erreur syntaxique")

 elif input_str.startswith('Snk_Begin'): ####Snk_begin
     print(f"debut du progarme")
 elif input_str.startswith('Snk_End'): ####Snk_End
     print(f"fin du progarme")    
 elif input_str.startswith('$$'): ###comment
   match = re.fullmatch(r'^\$\$\s*(.*)', input_str)
   if match:
    comment = match.group(1)
    print(f"comment: {comment}")
   else:
    print("erreur syntaxique")    
 elif input_str.startswith('Snk_Print'):   ### Snk_Print
        match = re.fullmatch(r'^Snk_Print\s*(?:"(.*)"|([a-zA-Z][a-zA-Z0-9]*(?:\s*,\s*[a-zA-Z][a-zA-Z0-9]*)*))\s*\$$', input_str)
        if match:
            string_value, ids = match.groups()

            if ids:
                ids = ids.split(',')
                print(f"affichage {', '.join(ids)}")
            elif string_value:
                print(f"affichage de la chaîne : {string_value}")
        else:
            if not re.search(r'^Snk_Print\s*(?:".*"|([a-zA-Z][a-zA-Z0-9]*(?:\s*,\s*[a-zA-Z][a-zA-Z0-9]*)*))', input_str):
                print("Erreur: Identifiant ou chaîne manquant")
            elif not re.search(r'\$$', input_str):
                print("Erreur: Le symbole $ est manquant")
            else:
                print("Erreur syntaxique")    

 elif input_str.startswith('Snk_Int'):    ####Snk_Int
    match = re.fullmatch(r'^Snk_Int\s*([a-zA-Z][a-zA-Z0-9]*(?:\s*,\s*[a-zA-Z][a-zA-Z0-9]*)*)\s*\$$', input_str)
    if match:
        ids = match.group(1).split(',')
        print(f"declaration d'un entier {', '.join(ids)}")
    else:
        if not re.search(r'^Snk_Int\s*[a-zA-Z][a-zA-Z0-9]*', input_str):
            print("Erreur: Identifiant manquant")
        elif not re.search(r'\$$', input_str):
            print("Erreur: Le symbole $ est manquant")
        else:
            print("Erreur syntaxique")

 elif input_str.startswith('Snk_Reel'):   ####Snk_Reel
    match = re.fullmatch(r'^Snk_Reel\s*([a-zA-Z][a-zA-Z0-9]*(?:\s*,\s*[a-zA-Z][a-zA-Z0-9]*)*)\s*\$$', input_str)
    if match:
        ids = match.group(1).split(',')
        print(f"declaration d'un réel {', '.join(ids)}")
    else:
        if not re.search(r'^Snk_Reel\s*[a-zA-Z][a-zA-Z0-9]*', input_str):
            print("Erreur: Identifiant manquant")
        elif not re.search(r'\$$', input_str):
            print("Erreur: Le symbole $ est manquant")
        else:
            print("Erreur syntaxique")

 elif input_str.startswith('Snk_String'):    ####Snk_String
    match = re.fullmatch(r'^Snk_String\s*"(.*)"\s*\$$', input_str)
    if match:
        string = match.group(1)
        print(f"string: {string}")
    else:
        if not re.search(r'^Snk_String\s*".*"', input_str):
            print("Erreur: Chaîne de caractères manquante")
        elif not re.search(r'\$$', input_str):
            print("Erreur: Le symbole $ est manquant")
        else:
            print("Erreur syntaxique")

 elif input_str.startswith('Get'):   ###Get
    match = re.fullmatch(r'^Get\s*([a-zA-Z][a-zA-Z0-9]*)\s*From\s*([a-zA-Z][a-zA-Z0-9]*)\s*\$$', input_str)
    if match:
        id1, id2 = match.groups()
        print(f"affectation de {id1} a partir de {id2}")
    else:
        if not re.search(r'^Get\s*[a-zA-Z][a-zA-Z0-9]*\s*From\s*[a-zA-Z][a-zA-Z0-9]*', input_str):
            print("Erreur: Identifiant manquant")
        elif not re.search(r'\$$', input_str):
            print("Erreur: Le symbole $ est manquant")
        else:
            print("Erreur syntaxique")

 elif input_str.startswith('If'): ##IF
   match = re.fullmatch(r'^If\s*\[(.*)\]\s*', input_str)
   if match:
     condition = match.group(1)
     process_command(input(f"condition: {condition}----ecrire une instruction dans If: "))
     print("fin If")
   else:
     print("erreur syntaxique")
 elif input_str.startswith('Begin'):
  print("debut de block")
 elif input_str.startswith('End'):
   print("fin de block")
 else:
  print("Commande non reconnue")


def main():
    global begin_encountered


    while True:
        input_command = input(". ")

        if input_command.strip().lower() == 'exit':
            break

        process_command(input_command)

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
