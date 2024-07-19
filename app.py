import streamlit as st
import pandas as pd



st.title("Quieres aprender Streamlit?")
st.subheader("Hi! I'm Subheader")
st.header("Hi! I am Header")
st.text("**Hola** este es mi primer Streamlit Web App ,\n es una aplicacion muy eficiente, "
        "puede ser utli para mostrar datos, y graficos desde un aplicativo web\n "
        "desde el punto de vista de la web puede ser muy util el empleo de esta tecnologia")
st.markdown("Hola este es mi primer Streamlit Web App")
st.markdown("**Hello** World")

st.markdown("# Hello World")
st.markdown("## Hello World")
st.markdown("### Hello World")
st.markdown("#### Hello World")
st.markdown("##### Hello World")
st.markdown("###### Hello World")

st.markdown("**bold text**")

st.markdown("*Italiziced text*")

st.markdown("> Block\n >\n >> - Blockquote anidade\n >> - B2")

st.markdown(">> - *Blockquote*")

st.markdown("1. First Item\n 2. Second Item\n 3. Third Item\n       1. Idented1\n       2. Idented2\n       3. Thirt\n 4. Four Item")

st.markdown("`st.markdown( arg )`")


st.markdown("[Google](https://www.google.com)")

st.caption(" Como hacer una Matrix en Latex con Letra Pequena")

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)

code = """ 
print("Hello World")
def funct():
    return 0;"""
st.code(code)

st.text("Se emplea el siguiente codigo para un DataFrame en Pandas:")
code_DataFrame = """
df = pd.DataFrame({
  'First column': [1, 2, 3, 4],
  'Second column': [10, 20, 30, 40]
})
df
"""
st.code(code_DataFrame)

st.text("Se obtiene la siguiente visualizacion:")
df = pd.DataFrame({
  'First column': [1, 2, 3, 4],
  'Second column': [10, 20, 30, 40]
})
df

st.write('st.write()')
