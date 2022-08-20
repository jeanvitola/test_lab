# EXECTUTE ETLS

# EXTRACT
try:
  exec(open("dataextract.py").read())
except:
  print("Ha ocurrido un error en dataextract")
else:
  print("Ejecución correcta de codigo01")

# TRANSFORM
try:
  exec(open("dataclean.py").read())
except:
  print("Ha ocurrido un error en codigo02")
else:
  print("Ejecución correcta de codigo02")

# LOAD
try:
  exec(open("datalake.py").read())
except:
  print("Ha ocurrido un error en codigo03")
else:
  print("Ejecución correcta de codigo03")