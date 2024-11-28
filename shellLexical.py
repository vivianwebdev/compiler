import basicLexical

lines = []
while True:
   text = input('expression > ')
   if text == '':
       # Process all collected lines
       for line in lines:
           result, error = basicLexical.run('<stdin>', line)
           if error: 
               print(error.as_string())
           else: 
               print(result)
       # Clear the lines list
       lines = []
   else:
       # Add the line to the list
       lines.append(text)
