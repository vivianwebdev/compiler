import re
begin_encountered = False
results = []
arrayInt = []
arrayReel = []

def process_command(input_str):
 global begin_encountered
 if input_str.startswith('Set'): #### Set
    match = re.fullmatch(r'^Set\s*([a-zA-Z][a-zA-Z0-9]*)\s* [+-]?\d+(\.\d*)?\s*\$$', input_str)
    if match:
        id, number = match.groups()
        if id not in arrayInt + arrayReel:
            print(f"Erreur: Identifiant '{id}' non déclaré.")
        elif '.' in (number or ''):
                if id not in arrayReel:
                    print(f"Erreur : {id} n'est pas déclaré comme Reel")
                else:
                   print(f"affectation d'un float à un id: {id}")    
        else:
            if id not in arrayInt:
                    print(f"Erreur : {id} n'est pas déclaré comme entier")
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
 elif input_str.startswith('Snk_Print'): ## Print
        match = re.fullmatch(r'^Snk_Print\s*(?:"(.*)"|([a-zA-Z][a-zA-Z0-9]*(?:\s*,\s*[a-zA-Z][a-zA-Z0-9]*)*))\s*\$$', input_str)
        if match:
            string_value, ids = match.groups()

            if ids:
                ids = ids.split(',')
                for id in ids:
                    if id not in arrayInt + arrayReel:
                        print(f"Erreur: Identifiant '{id}' non déclaré.")
                        return 

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
        arrayInt.extend(ids)
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
        arrayReel.extend(ids)
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
        arrayString.append(string)
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
        if id1 not in arrayInt + arrayReel:
                print(f"Erreur: Identifiant '{id1}' non déclaré.")
        elif id2 not in arrayInt + arrayReel:
                print(f"Erreur: Identifiant '{id2}' non déclaré.")
        elif (id1 in arrayInt and id2 in arrayInt) or (id1 in arrayReel and id2 in arrayReel):
            print(f"affectation de {id1} a partir de {id2}.")
        else:
            print("Erreur: L'affectation doit impliquer des variables du même Type.")

    else:
        if not re.search(r'^Get\s*[a-zA-Z][a-zA-Z0-9]*\s*From\s*[a-zA-Z][a-zA-Z0-9]*', input_str):
            print("Erreur: Identifiant manquant")
        elif not re.search(r'\$$', input_str):
            print("Erreur: Le symbole $ est manquant")
        else:
            print("Erreur syntaxique")

 elif input_str.startswith('If'): ## IF
        match = re.fullmatch(r'^If\s*\[(.*)\]\s*', input_str)
        if match:
            condition = match.group(1)
            if '/0' not in condition and ' / 0' not in condition:
                variables = re.findall(r'\b([a-zA-Z][a-zA-Z0-9]*)\b', condition)
                undeclared_variables = [var for var in variables if var not in arrayInt and var not in arrayReel and var not in arrayString]

                if not undeclared_variables:
                    process_command(input("ecrire une instruction dans If: "))
                    print("end If")
                else:
                    print(f"Erreur: variable {', '.join(undeclared_variables)} ne sont pas déclarées.")
            else:
                print("Error: Division sur zero nest pas autoriser.")
        else:
            print("erreur syntaxique")
 elif input_str.startswith('Begin'): ##begin
  if begin_encountered:
   print("Debut de bloc")
   begin_encountered = True
  while True:
   command = input("")
   if command.strip().lower() == 'End':
      break
   process_command(command)
 elif input_str.startswith('End'): ##End
  if begin_encountered:
   print("End of block reached")
   begin_encountered = False
   process_command(input(""))
  else: 
   print("Erreur: 'End' doit être précédé par un 'Begin'")   
 else:
  print("Commande non reconnue")


def main():
    global begin_encountered, arrayInt, arrayReel, arrayString

    first_instruction = input("")
    if not first_instruction.startswith('Snk_Begin'):
        print("Error: Le programme doit commencer par 'Snk_Begin'")
        return

    begin_encountered = True
    process_command(first_instruction)

    while True:
        input_command = input("")

        process_command(input_command)

        if input_command.startswith('Snk_End') and begin_encountered:
            print("")
            break

        if input_command.startswith('End') and not begin_encountered:
            print("Error: « End » doit être précédé de « Begin »")
            break

    print("\n")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
