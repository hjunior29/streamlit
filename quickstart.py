import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import functions

st.set_option('deprecation.showPyplotGlobalUse', False)

# Crie dados de amostra
X = [0,0,0]

# Título
st.title("INICIAÇÃO CIENTÍFICA")
st.write("Professor: Wanderlei Nascimento\n"
         "\nAluno: Helder Lima")

funcaoSelecionada = st.selectbox('Selecione uma Função',['ACKLEY','SPHERE','ROSENBROCK','RASTRIGIN','GRIEWANK','ZAKHAROV','EASOM','MICHALEWICS'])

if funcaoSelecionada == 'ACKLEY':
    x = st.slider('Valor ideal é aproximadamente: 32',10,50)
    if x == 32:
        x = 32.768
    st.pyplot(functions.PLOT_BENCHMARK(functions.ACKLEY(X),"ACKLEY",-x,x))
    st.write("A função Ackley é uma função matemática usada para testar algoritmos "
            "de otimização. Ela tem várias características desafiadoras, como "
            "múltiplos mínimos locais e uma superfície de erro complexa. A função "
            "tem um mínimo global em f(x) = 0, que é atingido quando xi = 0 para "
            "todo i. Além de ser usada em testes de algoritmos, a função Ackley "
            "também tem algumas aplicações práticas, como em controle de qualidade "
            "e modelagem estatística.")
    st.subheader("Exemplo de código  da função ACKLEY:")
    st.code("def ACKLEY(X):"
            "\n    DIM = len(X)"
            "\n    SUM1 = 0"
            "\n    SUM2 = 0"
            "\n    A = 20"
            "\n    B = 0.2"
            "\n    C = 2 * np.pi"
            "\n    for I_COUNT in range(DIM):"
            "\n        X_I = X[I_COUNT]"
            "\n        SUM1 += X_I ** 2"
            "\n        SUM2 += np.cos(C * X_I)"
            "\n    TERM_1 = -A * np.exp(-B * np.sqrt(SUM1 / DIM))"
            "\n    TERM_2 = -np.exp(SUM2 / DIM)"
            "\n    OF = TERM_1 + TERM_2 + A + np.exp(1)"
            "\n    return OF")

elif funcaoSelecionada == 'SPHERE':
    x = st.slider('Valor ideal é aproximadamente: 5',1,10)
    if x == 5:
        x = 5.12
    st.pyplot(functions.PLOT_BENCHMARK(functions.SPHERE(X),"SPHERE",-5.12,x))

    st.subheader("Exemplo de código  da função SPHERE:")
    st.code("def SPHERE(X):"
            "\n   DIM = len(X)"
            "\n   SUM = 0 "
            "\n   for I_COUNT in range(DIM):"
            "\n      X_I = X[I_COUNT]"
            "\n      SUM += X_I ** 2"
            "\n   OF = SUM"
            "\n   return OF")

elif funcaoSelecionada == 'ROSENBROCK':
    x = st.slider('Valor ideal é: 2048',1500,2500)
    st.pyplot(functions.PLOT_BENCHMARK(functions.ROSENBROCK(X),"ROSENBROCK",-x,x))

    st.subheader("Exemplo de código  da função ROSENBROCK:")
    st.code("def ROSENBROCK(X):"
            "\n    DIM = len(X)"
            "\n    SUM = 0"
            "\n    for I_COUNT in range(DIM - 1):"
            "\n        X_I = X[I_COUNT]"
            "\n        X_NEXT = X[I_COUNT + 1]"
            "\n        NEW = 100 * (X_NEXT - X_I ** 2) ** 2 + (X_I - 1) ** 2"
            "\n        SUM += NEW"
            "\n    OF = SUM"
            "\n    return OF")

elif funcaoSelecionada == 'RASTRIGIN':
    x = st.slider('Valor ideal é aproximadamente: 5',1,10)
    if x == 5:
        x = 5.12
    st.pyplot(functions.PLOT_BENCHMARK(functions.RASTRIGIN(X),"RASTRIGIN",-x,x))

    st.subheader("Exemplo de código  da função RASTRIGIN:")
    st.code("def RASTRIGIN(X):"
            "\n    DIM = len(X)"
            "\n    SUM = 0"
            "\n    for I_COUNT in range(DIM):"
            "\n        X_I = X[I_COUNT]"
            "\n        SUM += (X_I ** 2 - 10 * np.cos(2 * np.pi * X_I))"
            "\n    OF = 10 * DIM + SUM"
            "\n    return OF")

elif funcaoSelecionada == 'GRIEWANK':
    x = st.slider('Valor ideal é: 600',300,900)
    st.pyplot(functions.PLOT_BENCHMARK(functions.GRIEWANK(X),"GRIEWANK",-600,600))

elif funcaoSelecionada == 'ZAKHAROV':
    x = st.slider('Valor ideal é: 10',1,20)
    st.pyplot(functions.PLOT_BENCHMARK(functions.ZAKHAROV(X),"ZAKHAROV",-5,x))

elif funcaoSelecionada == 'EASOM':
    x = st.slider('Valor ideal é: 100',1,200)
    st.pyplot(functions.PLOT_BENCHMARK(functions.EASOM(X),"EASOM",-x,x))

elif funcaoSelecionada == 'MICHALEWICS':
    x = st.slider('Valor ideal é aproximadamente: 3',1,10)
    if x == 3:
        x = np.pi
    st.pyplot(functions.PLOT_BENCHMARK(functions.MICHALEWICS(X),"MICHALEWICS",0,np.pi))

