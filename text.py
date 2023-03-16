import streamlit as st

textAckley = "A função Ackley tem várias características desafiadoras, como múltiplos mínimos locais e uma " \
             "superfície de erro complexa. A função tem um mínimo global em f(x) = 0, que é atingido " \
             "quando xi = 0 para todo i. Além de ser usada em testes de algoritmos, a função Ackley " \
             "também tem algumas aplicações práticas, como em controle de qualidade e modelagem estatística."
codeAckley = "def ACKLEY(X):" \
             "\n    DIM = len(X)" \
             "\n    SUM1 = 0" \
             "\n    SUM2 = 0" \
             "\n    A = 20" \
             "\n    B = 0.2" \
             "\n    C = 2 * np.pi" \
             "\n    for I_COUNT in range(DIM):" \
             "\n        X_I = X[I_COUNT]" \
             "\n        SUM1 += X_I ** 2" \
             "\n        SUM2 += np.cos(C * X_I)" \
             "\n    TERM_1 = -A * np.exp(-B * np.sqrt(SUM1 / DIM))" \
             "\n    TERM_2 = -np.exp(SUM2 / DIM)" \
             "\n    OF = TERM_1 + TERM_2 + A + np.exp(1)" \
             "\n    return OF"

textSphere = "A função Sphere é utilizada como um problema de teste para algoritmos de otimização, " \
             "pois é relativamente simples e bem conhecida. A função tem um mínimo global em x = 0," \
             " onde f(x) = 0. É uma função unimodal, o que significa que tem apenas um mínimo global," \
             " mas pode ter muitos mínimos locais. A função Sphere é comumente utilizada como " \
             "benchmark para comparar o desempenho de diferentes algoritmos de otimização"
codeSphere = "def SPHERE(X):" \
            "\n   DIM = len(X)" \
            "\n   SUM = 0 " \
            "\n   for I_COUNT in range(DIM):" \
            "\n      X_I = X[I_COUNT]" \
            "\n      SUM += X_I ** 2" \
            "\n   OF = SUM" \
            "\n   return OF"

textRosenbrock = "A função de Rosenbrock, também conhecida como 'função da banana', é uma função matemática" \
                 " contínua, não-linear e unimodal. A forma geral da função é dada pela seguinte equação: " \
                 "f(x, y) = (a - x)^2 + b(y - x^2)^2, onde a e b são constantes positivas que afetam a " \
                 "forma da função. A função de Rosenbrock tem uma forma de vale alongado, com um mínimo " \
                 "global em (a, a^2). O problema de otimização é encontrar o valor mínimo global, o que " \
                 "pode ser difícil para algoritmos de otimização devido a seus muitos mínimos locais."
codeRosenbrock = "def ROSENBROCK(X):" \
            "\n    DIM = len(X)" \
            "\n    SUM = 0" \
            "\n    for I_COUNT in range(DIM - 1):" \
            "\n        X_I = X[I_COUNT]" \
            "\n        X_NEXT = X[I_COUNT + 1]" \
            "\n        NEW = 100 * (X_NEXT - X_I ** 2) ** 2 + (X_I - 1) ** 2" \
            "\n        SUM += NEW" \
            "\n    OF = SUM" \
            "\n    return OF"

textRastrigin = "A função Rastrigin é caracterizada por ter uma superfície com muitas oscilações e " \
                "picos, o que a torna mais difícil de otimizar do que funções mais simples. Ela tem " \
                "vários mínimos locais e é definida em termos de várias variáveis. A função Rastrigin " \
                "é comumente usada em testes de algoritmos de otimização para avaliar sua capacidade de " \
                "encontrar o mínimo global em um espaço de busca altamente dimensional."
codeRastrigin = "def RASTRIGIN(X):" \
            "\n    DIM = len(X)" \
            "\n    SUM = 0" \
            "\n    for I_COUNT in range(DIM):" \
            "\n        X_I = X[I_COUNT]" \
            "\n        SUM += (X_I ** 2 - 10 * np.cos(2 * np.pi * X_I))" \
            "\n    OF = 10 * DIM + SUM" \
            "\n    return OF"

textGriewank = "A função Griewank é uma função não-linear e contínua, e sua forma é caracterizada por " \
               "um grande número de pequenos vales. O objetivo da otimização é encontrar o mínimo global " \
               "da função, que é igual a zero quando todas as variáveis são igualmente iguais a zero. " \
               "No entanto, o grande número de pequenos vales torna a busca pelo mínimo global desafiadora " \
               "para muitos algoritmos de otimização."
codeGriewank = "def GRIEWANK(X):" \
            "\n    DIM = len(X)" \
            "\n    SUM = 0" \
            "\n    for I_COUNT in range(DIM):" \
            "\n        X_I = X[I_COUNT]" \
            "\n        SUM += (X_I ** 2) / 4000" \
            "\n    PROD = np.cos(X_I / np.sqrt(X_I))" \
            "\n    OF = SUM - PROD + 1" \
            "\n    return OF"

textZakharov = "A função Zakharov é uma função de otimização que possui um mínimo global em zero. É uma " \
               "função não linear e multimodal que contém termos quadráticos e cúbicos. Essa função é " \
               "bastante desafiadora para algoritmos de otimização devido à sua superfície de resposta " \
               "complexa, com muitas oscilações e muitos mínimos locais. A função Zakharov é frequentemente " \
               "usada como um problema de teste em problemas de otimização de múltiplas dimensões."
codeZakharov = "def ZAKHAROV(X):" \
           "\n    DIM = len(X)" \
           "\n    SUM_1 = 0" \
           "\n    SUM_2 = 0" \
           "\n    for I_COUNT in range(DIM):" \
           "\n        X_I = X[I_COUNT]" \
           "\n        SUM_1 += X_I ** 2" \
           "\n        SUM_2 += (0.5 * I_COUNT * X_I)" \
           "\n    OF = SUM_1 + SUM_2**2 + SUM_2**4" \
           "\n    return OF"

textEasom = "A função Easom é uma função de otimização com duas variáveis, que tem como objetivo encontrar " \
            "o mínimo global. Ela é utilizada como um problema de teste para algoritmos de otimização. " \
            "Seu formato apresenta um pico central, cercado por áreas com valores mais altos, o que a " \
            "torna uma função desafiadora de se otimizar. A solução ótima para essa função é f(x,y) = -1, " \
            "onde x e y são números reais que satisfazem a equação cos(x)*cos(y)*exp(-((x-pi)^2+(y-pi)^2))."
codeEasom = "def EASOM(X):" \
            "\n    X_1 = X[0]" \
            "\n    X_2 = X[1]" \
            "\n    FACT_1 = - np.cos(X_1) * np.cos(X_2)" \
            "\n    FACT_2 = np.exp(- (X_1 - np.pi) ** 2 - (X_2 - np.pi) ** 2)" \
            "\n    OF = FACT_1 * FACT_2" \
            "\n    return OF"

textMichalewics = "A função de Michalewicz é uma função não-linear usada como um problema de otimização " \
                  "global. A função é caracterizada por apresentar várias mínimas locais e um único mínimo " \
                  "global em um intervalo limitado. A função possui um comportamento altamente oscilatório " \
                  "e a sua superfície é fortemente não-linear. O objetivo da otimização é encontrar a " \
                  "localização do mínimo global."
codeMichalewics = "def MICHALEWICS(X):" \
          "\n    DIM = len(X)" \
          "\n    SUM = 0" \
          "\n    M = 10" \
          "\n    for I_COUNT in range(DIM):" \
          "\n        X_I = X[I_COUNT]" \
          "\n        SUM += np.sin(X_I) * (np.sin((I_COUNT * X_I ** 2) / np.pi)**(2 * M))" \
          "\n    OF = - SUM" \
          "\n    return OF"
