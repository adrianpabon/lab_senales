from select import select
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import scipy.signal as signal
st.title("Laboratorio Señales")

st.sidebar.title("Generación de señales")
option1= st.sidebar.selectbox(
    'Ingrese la función deseada',
    ('Seno', "Pulso","Cuadrática", "Exponencial","Lineal","Triangular", "Cuadrada", "Secuencia de impulso"))

#OPCION_SENO
if option1 == "Seno":
    amplitud = st.sidebar.number_input("Amplitud")
    frecuencia = st.sidebar.number_input("Frecuencia",min_value=0.00001,value=1.0, max_value=100000.0,step=1.0)
    t = np.arange(-4*(1/frecuencia), 4*(1/frecuencia), 0.00001)
    y = amplitud*np.sin(2*np.pi*frecuencia*t)
    fig, ax = plt.subplots()
    ax.plot(t,y)
    st.text("Función seno")  
    ax.grid(True)
    st.pyplot(fig)
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo", value=1)
    aes = st.sidebar.number_input("Escalamiento amplitud")
    ynew = (amplitud*aes)*np.sin(2*np.pi*frecuencia*(tes*t+ttras))
    fig1, ax = plt.subplots()
    ax.plot(t,ynew)
    st.text("Función seno transformada")
    ax.grid(True)
    st.pyplot(fig1)
    if st.sidebar.button("Animación"):
            fig1,ax=plt.subplots()
            cuadros = 10
            #para realizar traslación
            for i in range(cuadros+1):
                #ax.plot(t,y, "indigo", t,ynew, "darkred") #this shows our two functions
                fig1,ax=plt.subplots()
                ax.plot(t,y,"indigo", t-i*(ttras)/cuadros,y,linestyle="dashed")
                ax.legend(['Original', 'Desplazada'])
                ax.set_title("Función Seno")
                ax.set_xlabel("Eje x")
                ax.set_ylabel("Eje y")
                ax.grid(True)
                st.pyplot(fig1)
#OPCION_LINEAL
if option1 == "Lineal":
    pendiente = st.sidebar.number_input("Ingrese pendiente")
    intercepto = st.sidebar.number_input("Ingrese intercepto")
    t = np.arange(-20,20,1)
    y = pendiente*t + intercepto
    fig1, ax = plt.subplots()
    ax.plot(t,y,) 
    ax.grid(True)
    st.text("Función Lineal")
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo")
    ynew = pendiente*(tes*t + ttras) + intercepto
    fig, ax = plt.subplots()
    ax.plot(t,ynew)
    st.text("Función seno transformada")
    ax.grid(True)
    st.pyplot(fig1)
    st.pyplot(fig)

#OPCION_CUADRATICA
if option1 == "Cuadrática":
    a = st.sidebar.number_input("Ingresa a")
    b = st.sidebar.number_input("Ingresa b")
    c = st.sidebar.number_input("Ingresa c")
    t = np.arange(-10,10,1)
    y = a*(t**2)+b*t + c
    fig, ax = plt.subplots()
    ax.plot(t,y,) 
    st.text("Función Cuadrática")
    st.pyplot(fig)
    #Transformación
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo", value=1)
    ynew = a*((tes*t+ttras)**2)+b*(tes*t+ttras) + c
    fig1, ax = plt.subplots()
    ax.plot(t,ynew)
    st.text("Función cuadrática transformada")
    ax.grid(True)
    st.pyplot(fig1)

#OPCION_EXPONENCIAL
if option1=="Exponencial":
    a = st.sidebar.number_input("Ingrese amplitud")
    b = st.sidebar.number_input("Ingrese b")
    t = np.arange(-1,1,0.1)
    y = a*(np.exp(b*t))
    fig, ax = plt.subplots()
    ax.plot(t,y) 
    st.text("Función Exponencial")
    ax.grid(True)
    st.pyplot(fig)
    #Transformación
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo",value=1)
    aes = st.sidebar.number_input("Escalamiento amplitud")
    ynew = (a*aes)*(np.exp(b*(tes*t+ttras)))
    fig1, ax = plt.subplots()
    tnew = np.arange(-1-ttras,1-ttras,0.1)
    ax.plot(tnew,ynew)
    st.text("Función exponencial transformada")
    ax.grid(True)
    st.pyplot(fig1)
    
    

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
    #trans
    ttras = st.sidebar.number_input("Traslación")
    tes = st.sidebar.number_input("Escalamiento en el tiempo",value=1)
    aes = st.sidebar.number_input("Escalamiento amplitud")
    ynew = (a*aes)*signal.square(2*np.pi*w*(tes*t+ttras))
    fig1, ax = plt.subplots()
    ax.plot(t,ynew)
    st.text("Función seno transformada")
    ax.grid(True)
    st.pyplot(fig1)

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
    ttras = st.sidebar.number_input("Traslación")
    aes = st.sidebar.number_input("Escalamiento amplitud",)
    t = np.arange(-w-ttras, w-ttras, 0.01)
    ynew = t*0
    ynew[(t> -w/2-ttras)& (t< (w/2)-ttras) ] = a*aes
    fig1, ax = plt.subplots()
    ax.plot(t,ynew)
    ax.grid(True)
    st.pyplot(fig1)

#opcion_triangular
if option1 == "Triangular":
    a = st.sidebar.number_input('amplitud:')
    simetria = 0.5
    w = st.sidebar.number_input('Frecuencia:', 1, 15)
    t = np.arange(-4*(1/w), 4*(1/w), 0.00001)
    y = a*signal.sawtooth(2 * np.pi * w * t, simetria)
    fig, ax = plt.subplots()
    ax.plot(t,y)
    st.pyplot(fig)

#opcion_secuencia_de_impulso 
if option1=="Secuencia de impulso":
 x = st.text_input("Ingrese el valor de los vectores de x: ",args=None)
 y = st.text_input("Ingrese el valor de los vectores de y: ",args=None)
if len(x) != len(y):
    st.write("Ingrese vectores equivalentes")

else:
    fig,ax=plt.subplots()
    ax.set_xlim(-1,11)
    ax.set_ylim(0,10)
    ax.stem(x,y)
    ax.set_title("Función secuencia de impulsos")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True)
    st.pyplot(fig)
