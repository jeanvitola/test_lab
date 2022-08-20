
# EXTRACT
try:
  exec(open("dataextract.py").read())
except:
  print("Ha ocurrido un error en dataextract")
else:
  print("Ejecución correcta dataextract.py")

# TRANSFORM
try:
  exec(open("dataclean.py").read())
except:
  print("Ha ocurrido un error  dataclean.py")
else:
  print("Ejecución correcta dataclean.py")

# LOAD
try:
  exec(open("datalake.py").read())
except:
  print("Ha ocurrido un error en  datalake.py")
else:
  print("Ejecución correcta de datalake.py")