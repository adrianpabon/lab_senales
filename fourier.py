from re import M
from select import select
from turtle import end_fill, width
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import scipy.signal as signal
import scipy as sp

from scipy.fftpack import fft, fftfreq, fft


st.title("Laboratorio de series y transformada de fourier")
st.sidebar.title("Transformada y serie de fourier")
sub1= st.sidebar.subheader("Seleccione la operación que desee realizar: ")
option1= st.sidebar.selectbox("",("Transformada de fourier","Serie de fourier"))
#Serie de fourier
if option1=="Serie de fourier":
    Display1=st.sidebar.selectbox("Seleccione la función que desee",("Seno rectificada","Exponencial","Rampa trapezoidal","Rectangular","Triangular"))
    if Display1 == "Seno rectificada":
        amplitud = st.sidebar.number_input("Amplitud")
        w = st.sidebar.number_input("Frecuencia",min_value=0.00001,value=1.0, max_value=100000.0,step=1.0)
        dt=0.001
        t=np.arange(0, 2*(1/w), dt)
        y = abs(amplitud*np.sin(2*np.pi*w*t))
        T=1/w
        t1=t
        n=st.sidebar.number_input("Número de armónicos",value=1)
        st.subheader("Función seno rectificada")
        fig, ax = plt.subplots()
        ax.plot(t,y) 
        ax.grid(True)
        st.pyplot(fig)
    if Display1== "Exponencial":
        a = st.sidebar.number_input("Ingrese amplitud")
        b = st.sidebar.number_input("Ingrese b")
        pi= st.sidebar.number_input("Ingrese el punto de inicio del período")
        pf= st.sidebar.number_input("Ingrese el punto de fin del período")
        n=st.sidebar.number_input("Número de armónicos",value=1)
        dt=0.02
        t = np.arange(pi,pf,dt)
        y = a*(np.exp(b*t))
        T=pf-pi
        t1=np.arange(pi,pf+T,0.02)
        fig, ax = plt.subplots()
        st.subheader("Función exponencial")
        ax.plot(t,y) 
        ax.grid(True)
        st.pyplot(fig)
    if Display1 == "Rampa trapezoidal":
        a = st.sidebar.number_input("Ingrese amplitud")
        pin1=st.sidebar.number_input("Ingrese punto inicial del período")
        pf1=st.sidebar.number_input("Ingrese punto final del período")
        t = np.arange(pin1,pf1,0.02)
        y = t*0
        n=st.sidebar.number_input("Número de armónicos",value=1)
        lon=pf1-pin1
        T=lon
        dt=0.02
        t1 = np.arange(pin1,pf1+T,dt)
        pend=a/(pf1-lon*(2/3)-pin1);
        y[t <=pf1-lon*(2/3)]=(t[t<=pf1-lon*(2/3)]-pin1)*pend
        y[(t>pf1-lon*(2/3)) & (t<pf1-(lon/3))]=a
        y[t>=pf1-(lon/3)]=(t[t>=pf1-lon*(1/3)]-pf1)*(-pend)
        st.subheader("Función rampa trapezoidal")
        fig, ax = plt.subplots()
        ax.plot(t,y) 
        ax.grid(True)
        st.pyplot(fig)
    if Display1=="Rectangular":
        w = st.sidebar.number_input("Frecuencia",min_value=0.00001,value=1.0, max_value=100000.0,step=1.0)
        a = st.sidebar.number_input("Amplitud")
        t = np.arange(0, 4*(1/w), 0.00001)
        y = a*signal.square(2*np.pi*w*t)
        T=1/w
        dt=0.001
        t1 = np.arange(0, 2*(1/w), dt)
        n=st.sidebar.number_input("Número de armónicos",value=1)
        st.subheader("Función rectangular")
        fig, ax = plt.subplots()
        ax.plot(t,y) 
        ax.grid(True)
        st.pyplot(fig)
    if Display1=="Triangular":
        a = st.sidebar.number_input('amplitud:')
        simetria = 0.5
        w = st.sidebar.number_input('Frecuencia:', min_value=0.00001,value=1.0, max_value=100000.0,step=1.0)
        T=1/w
        n=st.sidebar.number_input("Número de armónicos",value=1)
        dt=0.0001
        t = np.arange(0, 2*(1/w), dt)
        t1=t
        y = a*signal.sawtooth(2 * np.pi * w * t, simetria)
        st.subheader("Función triangular")
        fig, ax = plt.subplots()
        ax.plot(t,y)
        ax.grid(True)
        st.pyplot(fig)
    ak=np.zeros(n)
    bk=np.zeros(n)
    a0=0
    m=len(t)
    w0=(2*np.pi)/T
    for i in range(m):
        a0=a0+(1/T)*y[i]*dt
    for i in range(n):
        for j in range(m):
            ak[i]=ak[i]+((2/T)*y[j]*np.cos(i*t[j]*w0))*dt
            bk[i]=bk[i]+((2/T)*y[j]*np.sin(i*t[j]*w0))*dt
    yf=t1*0+a0
    for i in range(n):
        yf=yf+ak[i]*np.cos(w0*i*t1)+bk[i]*np.sin(w0*i*t1)
    Ver1=st.sidebar.button("Ver serie de fourier")
    if Ver1:
        st.subheader("Serie de fourier")
        fig1, ax = plt.subplots()
        ax.plot(t1,yf)
        ax.grid(True)
        st.pyplot(fig1)
        ck=np.zeros(n)
        ta=ck*0
        fas=ta*0
        for i in range(n):
            ck[i]=np.sqrt((ak[i]**2)+(bk[i]**2))
            ta[i]=i+1
            if ak[i]==0:
                fas[i]=-(np.pi)/2
            else:
                fas[i]=-np.arctan(bk[i]/ak[i])
        st.subheader("Espectro en amplitud")
        fig2, ax = plt.subplots()
        ax.bar(ta,ck, width=n/150)
        ax.scatter(ta,ck)
        ax.grid(True)
        st.pyplot(fig2)
        st.subheader("Espectro en fase")
        fig3, ax = plt.subplots()
        ax.bar(ta,fas, width=n/150)
        ax.scatter(ta,fas)
        ax.grid(True)
        st.pyplot(fig3)
#Transformada

elif option1=="Transformada de fourier":

    n = (st.sidebar.number_input(' Numero de muestras:', min_value=2))       
    ao = st.sidebar.number_input('Amplitud A0:', min_value=0)
    a1 = st.sidebar.number_input('Amplitud A1:', min_value=0)
    a2 = st.sidebar.number_input('Amplitud A2:', min_value=0)
    wo = st.sidebar.number_input('Frecuencia Wo:', min_value=1)
    w1 = st.sidebar.number_input('Frecuencia W1:', min_value=1)
    w2 = st.sidebar.number_input('Frecuencia W2:', min_value=1)
    fs = st.sidebar.number_input('Frecuencia muestreo:', min_value=4)
    if (2*wo > fs) or (2*w1 > fs) or (2*w2 > fs):
        st.warning(" Su frecuencia de muestreo no cumple con Nyquist")

    
    t1 = np.arange(0,n-1,0.1)
    x = ao * np.sin ((2*np.pi*wo*t1/fs)) + a1 * np.cos((2*np.pi*w1*t1/fs)) + a2 * np.sin((2*np.pi*w2*t1/fs))

    y = fft(x)
    ab = np.abs(y)
    sp_fft = np.fft.fftshift(ab)
    t2 = (fs*np.arange (-0.5 - (1/len(sp_fft) ), 0.5 - 1/len(sp_fft) , 1/len(sp_fft)) )
   
    fase = np.angle(y) 
    t3 = fs*np.arange( -0.5-(1/len(fase)), 0.5-(1/len(fase)), 1/len(fase) ) 

    if st.sidebar.button('Transformar'):
        #señal 
        fig, ax = plt.subplots()
        plt.title("Señal")
        ax.plot(t1,x)
        ax.grid(True)
        st.pyplot(fig)

        #amplitud
        fig2, ax2 = plt.subplots()
        plt.title("Amplitud")
        ax2.plot(t2, sp_fft)
        ax2.grid(True)
        st.pyplot(fig2)
        

        #fase
        fig3, ax3 = plt.subplots()
        plt.title("Fase")
        ax3.plot(t3, fase)
        ax3.grid(True)
        st.pyplot(fig3)

                            


       


    

