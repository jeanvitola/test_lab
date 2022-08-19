from logg import log

def suma (a,b):
    log.info('suma')
    c = a + b
    return c 


 
print(suma(8,2))
log.info("Se finalizo la suma")