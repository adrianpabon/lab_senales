from select import select
from turtle import width
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import scipy.signal as signal
st.title("Laboratorio de Señales")

st.sidebar.title("Generación de señales")
option1= st.sidebar.selectbox(
    'Ingrese la función deseada',
    ('Seno', "Pulso","Cuadrática", "Exponencial","Lineal","Triangular", "Cuadrada", "Secuencia de impulso"))

#OPCION_SENO
if option1 == "Seno":
    amplitud = st.sidebar.number_input("Amplitud")
    frecuencia = st.sidebar.number_input("Frecuencia",min_value=0.00001,value=1.0, max_value=100000.0,step=1.0)
    t = np.arange(-4*(1/frecuencia), 4*(1/frecuencia), 1/(100*frecuencia))
    y = amplitud*np.sin(2*np.pi*frecuencia*t)
    fig, ax = plt.subplots()
    ax.plot(t,y)
    st.text("Función seno")  
    ax.grid(True)
    st.pyplot(fig)
    st.sidebar.text("Función seno transformada")
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo", value=1.00)
    aes = st.sidebar.number_input("Escalamiento amplitud", value=1.00)
    y2=amplitud*np.sin(2*np.pi*frecuencia*(t+ttras))
    tfig2=t-(ttras)
    y3=amplitud*np.sin(2*np.pi*frecuencia*(tes*t+ttras))
    tfig3=(t-ttras)/tes
    ynew = (amplitud*aes)*np.sin(2*np.pi*frecuencia*(tes*t+ttras))
    fig1, ax = plt.subplots()
    ax.plot(tfig3,ynew)
    ax.legend(['Transformada'])
    st.text("Función seno transformada")
    ax.grid(True)
    the_plot= st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #escalamiento animación
            if tes !=1:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig2/(1+ i*(tes-1)/cuadros),y2, linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #amplitud
            if aes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig3,y3*(1 + i*(aes-1)/(cuadros)), linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    #print(1 + i*(aes-1)/(cuadros))
                    the_plot.pyplot(fig1)

#OPCION_LINEAL
if option1 == "Lineal":
    pendiente = st.sidebar.number_input("Ingrese pendiente")
    intercepto = st.sidebar.number_input("Ingrese intercepto")
    t = np.arange(-20,21,1)
    y = pendiente*t + intercepto
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo", value=1.00)
    y2=pendiente*(t+ttras)+intercepto
    ynew = pendiente*(tes*t + ttras) + intercepto
    fig, ax = plt.subplots()
    st.text("Función Lineal")
    ax.plot(t,y)
    ax.grid(True)
    st.pyplot(fig)
    fig1, ax = plt.subplots()
    st.text("Función lineal transformada")
    ax.plot(t,ynew) 
    ax.grid(True)
    the_plot=st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Lineal")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #escalamiento animación
            if tes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t/(1+ i*(tes-1)/cuadros),y2, linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)

#OPCION_CUADRATICA
if option1 == "Cuadrática":
    a = st.sidebar.number_input("Ingresa a",value=1.00)
    b = st.sidebar.number_input("Ingresa b")
    c = st.sidebar.number_input("Ingresa c")
    centrox=-b/(2*a)
    t = np.arange(-10+(centrox),11+(centrox),1)
    y = a*(t**2)+b*t + c
    fig, ax = plt.subplots()
    ax.plot(t,y) 
    ax.grid(True)
    st.text("Función Cuadrática")
    st.pyplot(fig)
    #Transformación
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo", value=1.00)
    ynew = a*((tes*t+ttras)**2)+b*(tes*t+ttras) + c
    tfig2=t-(ttras)
    tfig3= (t-ttras)/tes
    y2=a*((t+ttras)**2)+b*(t+ttras) + c
    fig1, ax = plt.subplots()
    ax.plot(t,ynew)
    st.text("Función cuadrática transformada")
    ax.grid(True)
    the_plot=st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función cuadrátical")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #escalamiento animación
            if tes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t/(1+ i*((tes)-1)/cuadros),y2, linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Cuadrática: Transformación")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)


#OPCION_EXPONENCIAL
if option1=="Exponencial":
    a = st.sidebar.number_input("Ingrese amplitud")
    b = st.sidebar.number_input("Ingrese b")
    t = np.arange(-2,2,0.02)
    y = a*(np.exp(b*t))
    fig, ax = plt.subplots()
    ax.plot(t,y) 
    st.text("Función Exponencial")
    ax.grid(True)
    st.pyplot(fig)
    #Transformación
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo",value=1.00)
    aes = st.sidebar.number_input("Escalamiento amplitud",value=1.00)
    tfig2=t-(ttras)
    tfig3=(t-ttras)/tes
    y2= a*(np.exp(b*(t+ttras)))
    y3 = a*(np.exp(b*(tes*t+ttras)))
    ynew = (a*aes)*(np.exp(b*(tes*t+ttras)))
    fig1, ax = plt.subplots()
    # tnew = np.arange(-1-ttras,1-ttras,0.1)
    ax.plot(t,ynew)
    st.text("Función exponencial transformada")
    ax.grid(True)
    the_plot=st.pyplot(fig1)
    #escalamiento animación
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            if tes !=1:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t/(1+ i*(tes-1)/cuadros),y2, linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
                    #amplitud
            if aes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig3,y3*(1 + i*(aes-1)/(cuadros)), linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    #print(1 + i*(aes-1)/(cuadros))
                    the_plot.pyplot(fig1)
    
#opcion_cuadrado
if option1=="Cuadrada":
    w = st.sidebar.number_input("Frecuencia",min_value=0.00001,value=1.0, max_value=100000.0,step=1.0)
    a = st.sidebar.number_input("Amplitud")
    t = np.arange(-4*(1/w), 4*(1/w), 0.00001)
    y = a*signal.square(2*np.pi*w*t)
    fig, ax = plt.subplots()
    ax.plot(t,y) 
    ax.grid(True)
    st.text("Función cuadrada")
    st.pyplot(fig)
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo",value=1.00)
    aes = st.sidebar.number_input("Escalamiento amplitud", value=1.00)
    tfig2=t-(ttras)
    tfig3=(t-ttras)/tes
    y2= (a)*signal.square(2*np.pi*w*(t+ttras))
    y3=a*signal.square(2*np.pi*w*(tes*t+ttras))
    ynew = (a*aes)*signal.square(2*np.pi*w*(tes*t+ttras))
    fig1, ax = plt.subplots()
    ax.plot(t,ynew)
    st.text("Función seno transformada")
    ax.grid(True)
    the_plot=st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 5
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función cuadrada: Transformación")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #escalamiento animación
            if tes !=1:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig2/(1+ i*(tes-1)/cuadros),y2, linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función cuadrada: Transformación")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #amplitud
            if aes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig3,y3*(1 + i*(aes-1)/(cuadros)), linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función cuadrada: Transformación")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    #print(1 + i*(aes-1)/(cuadros))
                    the_plot.pyplot(fig1)


#opcion_pulso 
if option1=="Pulso":
    w = st.sidebar.number_input("Ingrese ancho de pulso")
    a = st.sidebar.number_input("Ingrese amplitud ")
    st.text("Funcion Pulso")
    t = np.arange(-w, w, 0.01)
    y = t*0
    y[(t> -w/2)& (t< w/2) ] = a
    fig, ax = plt.subplots()
    ax.plot(t,y)
    ax.grid(True)
    st.pyplot(fig)
    ttras = st.sidebar.number_input("Traslación",value=0.0)
    tes=st.sidebar.number_input("Escalamiento en el tiempo",value=1.00)
    aes = st.sidebar.number_input("Escalamiento amplitud",value=1.00)
    tfig2=np.arange((-w-ttras) ,(w-ttras), 0.01)
    y2=tfig2*0
    y2[(tfig2> (-w/2-ttras)) & (tfig2< ((w/2)-ttras)) ] = a
    tfig3 = np.arange((-w-ttras)/tes ,(w-ttras)/tes, 0.01)
    y3 = tfig3*0
    y3[(tfig3> (-w/2-ttras)/tes) & (tfig3< ((w/2)-ttras)/tes) ] = a
    ynew = tfig3*0
    ynew[(tfig3> (-w/2-ttras)/tes) & (tfig3< ((w/2)-ttras)/tes) ] = a*aes
    fig1, ax = plt.subplots()
    ax.plot(tfig3,ynew)
    ax.grid(True)
    the_plot=st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #escalamiento animación
            if tes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig2/(1+ i*(tes-1)/cuadros),y2, linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #amplitud
            if aes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig3,y3*(1 + i*(aes-1)/(cuadros)), linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    #print(1 + i*(aes-1)/(cuadros))
                    the_plot.pyplot(fig1)
           

#opcion_triangular
if option1 == "Triangular":
    a = st.sidebar.number_input('amplitud:')
    simetria = 0.5
    w = st.sidebar.number_input('Frecuencia:', min_value=0.00001,value=1.0, max_value=100000.0,step=1.0)
    t = np.arange(-2*(1/w), 2*(1/w), 0.00001)
    y = a*signal.sawtooth(2 * np.pi * w * t, simetria)
    fig, ax = plt.subplots()
    ax.plot(t,y)
    st.text("Función triangular")
    st.pyplot(fig)
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo", value=1.00)
    aes = st.sidebar.number_input("Escalamiento amplitud",value=1.00)
    y2=(a)*signal.sawtooth(2 * np.pi * w * (t+ttras), simetria)
    tfig2=t-(ttras)
    y3=(a)*signal.sawtooth(2 * np.pi * w * (tes*t+ttras), simetria)
    tfig3=(t-ttras)/tes
    ynew=(a*aes)*signal.sawtooth(2 * np.pi * w * (tes*t+ttras), simetria)
    fig1, ax = plt.subplots()
    ax.plot(tfig3,ynew)
    st.text("Función triangular transformada")
    ax.grid(True)
    the_plot=st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #escalamiento animación
            if tes !=1:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig2/(1+ i*(tes-1)/cuadros),y2, linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    the_plot.pyplot(fig1)
            #amplitud
            if aes != 1:
                for i in range(cuadros+1):
                    fig1,ax=plt.subplots()
                    ax.plot(t,y,"indigo", tfig3,y3*(1 + i*(aes-1)/(cuadros)), linestyle="dashed")
                    ax.legend(['Original', 'Desplazada'])
                    ax.set_title("Función Seno")
                    ax.set_xlabel("Eje x")
                    ax.set_ylabel("Eje y")
                    ax.grid(True)
                    #print(1 + i*(aes-1)/(cuadros))
                    the_plot.pyplot(fig1)


#opcion_secuencia_de_impulso 
if option1=="Secuencia de impulso":
    st.text('Tren de impulsos')
    t = st.sidebar.text_input('x []:')
    y = st.sidebar.text_input('y []:')
    t = np.array(np.matrix(t)).ravel()
    y = np.array(np.matrix(y)).ravel()
    fig, ax = plt.subplots()
    ax.bar(t,y, width=0.03)
    ax.scatter(t,y)
    st.pyplot(fig)
    ttras = st.sidebar.number_input("Traslación",value=0)
    aes = st.sidebar.number_input("Escalamiento amplitud", value=1.00)
    tfig2=t-ttras
    ynew=aes*y
    fig1, ax = plt.subplots()
    ax.bar(tfig2,ynew, width=0.03)
    ax.scatter(tfig2,ynew)
    the_plot=st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            if ttras != 0:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.bar(t,y, width=0.03)
                    ax.bar( t-i*(ttras)/cuadros,y, width=0.03)
                    ax.scatter(t,y, t-i*(ttras)/cuadros,y)
                    the_plot.pyplot(fig1)
            if aes != 1:
                for i in range(cuadros+1):
                    #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                    fig1,ax=plt.subplots()
                    ax.bar(t,y, width=0.03)
                    ax.bar(  tfig2,y*(1 + i*(aes-1)/(cuadros)), width=0.03)
                    ax.scatter(t,y,  tfig2,y*(1 + i*(aes-1)/(cuadros)))
                    the_plot.pyplot(fig1)
          



