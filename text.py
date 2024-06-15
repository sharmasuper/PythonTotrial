# # import re module for regular expression

import re
pattern = r"[A-Z]+his"    # raw string
text = '''This project has currently been taken over by Tung Luong as a 
graduate project and would love to get feedback on any of the information as well as would love contributions. So please feel 
free to edit appropriately as well as let me know how I am doing.
This is a textbook for teaching the principles and practice of proteomics for 
undergraduate students in the life sciences. The focus is on the analytical methods and 
data analysis for protein separation, quantitation and identification. We will begin with older
 methods (chromatography, electrophoresis) and move 
to more modern approaches (chips, for example) that are being used for high throughput proteomics.'''

# match = re.search(pattern,text)
# print(match)

# but yai frist accurance hu return kartha h


matches = re.finditer(pattern,text)
# print(matches)

for match in matches :
    print(match)
    print(match.span())
    # print(match.span()[0])
    print(text[match.span()[0]:match.span()[1]])









