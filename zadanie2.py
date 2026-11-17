import re
def split_camel_case(s:str) 
  if not s:
    return []
  return re.findall(r'[A-Z] + (?=[A-Z][a-z])| [A-Z]?[a-z] + [A-Z + [0-9]+]',s)
  
