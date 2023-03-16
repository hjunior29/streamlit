import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from functions import *
from text import *

st.set_page_config(
    page_title="Iniciação Científica",
    page_icon=":book:"
)

# Crie dados de amostra
X = [0,0,0]

# Título
st.title("INICIAÇÃO CIENTÍFICA")
st.write("Orientador: Wanderlei Nascimento\n"
         "\nAluno: Helder Lima")

funcaoSelecionada = st.selectbox('Selecione uma Função',['ACKLEY','SPHERE','ROSENBROCK','RASTRIGIN','GRIEWANK','ZAKHAROV','EASOM','MICHALEWICS'])

if funcaoSelecionada == 'ACKLEY':
    x = st.slider('Valor ideal é aproximadamente: 32',10,50)
    if x == 32:
        x = 32.768
    st.pyplot(PLOT_BENCHMARK(ACKLEY(X),"ACKLEY",-x,x))
    st.write(textAckley)
    st.subheader("Exemplo de código  da função ACKLEY:")
    st.code(codeAckley)

elif funcaoSelecionada == 'SPHERE':
    x = st.slider('Valor ideal é aproximadamente: 5',1,10)
    if x == 5:
        x = 5.12
    st.pyplot(PLOT_BENCHMARK(SPHERE(X),"SPHERE",-5.12,x))
    st.write(textSphere)
    st.subheader("Exemplo de código  da função SPHERE:")
    st.code(codeSphere)

elif funcaoSelecionada == 'ROSENBROCK':
    x = st.slider('Valor ideal é: 2048',1500,2500)
    st.pyplot(PLOT_BENCHMARK(ROSENBROCK(X),"ROSENBROCK",-x,x))
    st.write(textRosenbrock)
    st.subheader("Exemplo de código  da função ROSENBROCK:")
    st.code(codeRosenbrock)

elif funcaoSelecionada == 'RASTRIGIN':
    x = st.slider('Valor ideal é aproximadamente: 5',1,10)
    if x == 5:
        x = 5.12
    st.pyplot(PLOT_BENCHMARK(RASTRIGIN(X),"RASTRIGIN",-x,x))
    st.write(textRastrigin)
    st.subheader("Exemplo de código  da função RASTRIGIN:")
    st.code(codeRastrigin)

elif funcaoSelecionada == 'GRIEWANK':
    x = st.slider('Valor ideal é: 600',300,900)
    st.pyplot(PLOT_BENCHMARK(GRIEWANK(X),"GRIEWANK",-600,600))
    st.write(textGriewank)
    st.subheader("Exemplo de código  da função Griewank:")
    st.code(codeGriewank)

elif funcaoSelecionada == 'ZAKHAROV':
    x = st.slider('Valor ideal é: 10',1,20)
    st.pyplot(PLOT_BENCHMARK(ZAKHAROV(X),"ZAKHAROV",-5,x))
    st.write(textZakharov)
    st.subheader("Exemplo de código  da função ZAKHAROV:")
    st.code(codeZakharov)

elif funcaoSelecionada == 'EASOM':
    x = st.slider('Valor ideal é: 100',1,200)
    st.pyplot(PLOT_BENCHMARK(EASOM(X),"EASOM",-x,x))
    st.write(textEasom)
    st.subheader("Exemplo de código  da função EASOM:")
    st.code(codeEasom)

elif funcaoSelecionada == 'MICHALEWICS':
    x = st.slider('Valor ideal é aproximadamente: 3',1,10)
    if x == 3:
        x = np.pi
    st.pyplot(PLOT_BENCHMARK(MICHALEWICS(X),"MICHALEWICS",0,np.pi))
    st.write(textMichalewics)
    st.subheader("Exemplo de código  da função MICHALEWICS:")
    st.code(codeMichalewics)