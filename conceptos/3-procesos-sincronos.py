from subprocess import run, PIPE

print("Empiezo")
programa=('ping', '-c', '5', 'localhost')
salida=run( programa, stdout=PIPE, stderr=PIPE )
# El run hace llamada sincrona
print("Acabó")

print(salida)
print(salida.args)
print(salida.returncode)
print(salida.stdout)
print(salida.stderr)