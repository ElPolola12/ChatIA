#LIBRERIAS 

import streamlit as st
from groq import Groq

clave_de_usuario = ""
usuario=""
modelo_actual = ""
mensaje = ""
MODELOS = ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"]
mensaje = []

#CREAR USUARIO
def crear_usuario_groq():
    clave_de_usuario = st.secrets["CLAVE_API"]
    return Groq (api_key = clave_de_usuario)


def configurar_modelo (cliente, modelo, mensajeDeEntrada):
        #RETORNAMOS LA FUNCION UQUE PROCESA EL MENSAJE DEL USUARIO
        def configurar_modelo(cliente, modelo, mensajeDeEntrada):
           return cliente.chat.completions.create(
      model=modelo,
      messages=[{"role": "user", "content": mensajeDeEntrada}],
      stream=True
)
        
def actualizar_historial (rol,contenido, avatar):
    st.session_state.mensaje.apped({"role": rol, "content": contenido, "avatar": avatar})


def mostrar_historial():
    for mensaje in st.session_state.mensaje: 
        with st.chat_message(mensaje["role"], avatar=mensaje["avatar"]):
            st.markdown (mensaje)



#ESTADO DONDE EL USUARIO PODRÁ GUARDAR LOS MENSAJES
def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

#GUARDAR PROGRESO DE LA PAGINA
def configuración_de_pagina():
           #NOMBRE DE PESTAÑA
           st.set_page_config("Chat IA")
           #TITULO
           st.title ("EL PANA INTELIGENTE")
           #SIDEBAR
           st.sidebar.title("sidebar de modelos")
           m = st.sidebar.selectbox("modelos", MODELOS, index = 0) 
           return m




#BLOQUE DE EJECUCIÓN

#LLAMAMOS AL ESTADO DE MENSAJE
inicializar_estado()

#USUARIO DERIVADO DE LA CLAVE API
usuario = crear_usuario_groq()

#CONFIGURAMOS PAGINA Y ELEGIMOS EL MODELO
modelo_actual=configuración_de_pagina()

#CREAMOS EL CHAT BOT
mensaje = st.chat_input("Que piensas:")

#PROCESAMIENTO DE UNA RESPUESTA A PARTIR DE UN MODELO
if mensaje:
   configurar_modelo (usuario, modelo_actual, mensaje)
   print(mensaje)






