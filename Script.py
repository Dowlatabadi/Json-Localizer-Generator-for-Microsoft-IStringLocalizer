import googletrans
from googletrans import Translator
translator = Translator()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
cultures=['en','de']
res1=[]
for line in Lines:
    translation={}
    for culture in cultures:
        translation[culture]=translator.translate(line, dest=culture).text
    LocalizedValue=f"""
    {{
    "Key": "{line.strip()}",
        "LocalizedValue":{{
         {
      ",".join([f'"{key}-{key.upper()}" : "{translation[key]}"' for key in translation])
        }
        }}
    }}
    """
    res1.append(LocalizedValue)
result=f"""
[
    {','.join([LocalizedValue for LocalizedValue in res1])}
]
"""

print (result)

