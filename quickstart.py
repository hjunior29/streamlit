import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import functions

# Crie dados de amostra
X = [0,0,0]

st.set_option('deprecation.showPyplotGlobalUse', False)
# Exiba o gráfico usando o Streamlit
st.pyplot(functions.PLOT_BENCHMARK(functions.ACKLEY(X),"ACKLEY",-32.768,32.768))
st.pyplot(functions.PLOT_BENCHMARK(functions.SPHERE(X),"SPHERE",-5.12,5.12))
st.pyplot(functions.PLOT_BENCHMARK(functions.ROSENBROCK(X),"ROSENBROCK",-2048,2048))
st.pyplot(functions.PLOT_BENCHMARK(functions.RASTRIGIN(X),"RASTRIGIN",-5.12,5.12))
st.pyplot(functions.PLOT_BENCHMARK(functions.GRIEWANK(X),"GRIEWANK",-600,600))
st.pyplot(functions.PLOT_BENCHMARK(functions.ZAKHAROV(X),"ZAKHAROV",-5,10))
st.pyplot(functions.PLOT_BENCHMARK(functions.EASOM(X),"EASOM",-100,100))
st.pyplot(functions.PLOT_BENCHMARK(functions.MICHALEWICS(X),"MICHALEWICS",0,np.pi))


