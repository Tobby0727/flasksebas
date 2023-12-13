from flask import Flask 
app=Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>¡I dig it!</h1>"
##primer punto
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=round((nota1*30/100)+(nota2*30/100)+(nota3*40/100),1)
    return f"<h1>El resultado es: {resultado}</h1>"

##segundo punto 
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad<18:
        E="menor de edad"
    elif(edad<60):
        E="Adulto"
    else:
        E="Adulto mayor"
    return f"<h1>La persona es: {E}</h1> <hr>"

##tercer punto
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
    return f"<h1>El arreglo aleatorio es: {arreglo}</h1><hr>"


##puntos de los jercicios propuestos
##1.) Haga un programa que calcule la siguiente ecuación: Y = X * Z + Z + X.
@app.route("/calculos")
@app.route("/calculos/<int:x>/<int:z>")
def valores(x=0,z=0):
    resultado=x*z+z+x
    return f"<hr><h1>Y es = {resultado}</h1></hr>"

##2.) Realizar programa que, capturado un número, realice la tabla de multiplicar de ese número  hasta el 10.
@app.route("/multiplicacion")
@app.route("/multiplicacion/<int:num>")
def multiplicacion(num=0):
    res1=(num*1)
    res2=(num*2)
    res3=(num*3)
    res4=(num*4)
    res5=(num*5)
    res6=(num*6)
    res7=(num*7)
    res8=(num*8)
    res9=(num*9)
    res10=(num*10)
    return f"<h1>1*{num}={res1}, 2*{num}={res2}, 3*{num}={res3}, 4*{num}={res4}, 5*{num}={res5}, 6*{num}={res6}, 7*{num}={res7}, 8*{num}={res8}, 9*{num}={res9}, 10*{num}={res10}</h1>"

##3.) Realizar el programa que calcule las áreas de un círculo, cuadrado y triangulo
##area del cuadrado
@app.route("/areac/cuadrado")
@app.route("/areac/cuadrado/<int:num>")
def arec(num=0):
    res=(num*2)
    return f"<h1>El area del cuadrado es: {res}</h1>"

##area del triangulo
@app.route("/areat/triangulo")
@app.route("/areat/triangulo/<int:b>/<int:a>")
def areat(b=0,a=0):
    res=(b*a)/2
    return f"<h1>El area del triangulo es: {res}</h1>"

##area del circulo
@app.route("/areaci/circulo")
@app.route("/areaci/circulo/<int:r>")
def areaci(r=0):
    respuesta =((r*2)*3.14)
    return f"<h1>El area del circulo es: {respuesta}</h1>"
if __name__=='__main__':
    app.run(debug=True)
    
    
    
    
    

