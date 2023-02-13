Autor: Alisson Schimitt e Lucas Thomas
Disciplina: Linguagens Formais e Autômatos

Lista de Dependências, Tecnologias Utilizadas:

    - Linguagem de Programação: python 3.8.2

    - Editor: Visual Studio Code

    - Extensões do editor:  Python - microsoft
                            Python Preview - dongli
                            MagicPython - MagicStack Inc
                            GitLens - Eric Amodio

    -APIs, bibliotecas: -sys
                        -nenhuma API foi Utilizadas
                        -outras bibliotecas utilizadas foram desenvolvidas como parte do projeto

    -Controle do código:    -Git
                            -GitHub (@schimittalisson, repositório(Trabalho-LFA))


Para execução do programa:
    - É necessário ter o python instalado em seu sistema, de preferencia a versão utilizada (3.8.2), mas deve funcionar nas demais também.
    
    -Após a instalação do python, deve-se abrir o CMD, e acessar onde o programa foi salvo, após acessar o diretório certo, basta digita "python main.py", e o programa será executado. Ou apenas abrir a pasta do projeto e clicar duas vezes em  "main.py"
    
Como o programa funciona:

    A classe NFA possui cinco funções, sendo elas: read_string()，fecho_e()，next_state()，match_final_state() e print_quint().

    A função read_string(input_str): le o input de uma fita e avalia se ela pode ou não ser lida pelo automato

    A função fecho_e(state): procura uma transição epsilon usando a ideia de uma BFS(Breadth-first search)

    A função next_state(current_states, c): procura o proximo estado dado por uma transição c

    A função match_final_state(final_current_states): verifica se o estado final corresponde com a quintupla

    A função print_quint(): Escreve no terminal a quintupla do automato

Regras para usar o programa:
    O character 'e' é reservado para representar o Epsilon no programa, recomendavel não usa-lo como elemento no alfabeto;

    Foi colocado 3 exemplos de automatos no main do programa, cada um representando um AFD, AFN e AFe, respectivamente   
