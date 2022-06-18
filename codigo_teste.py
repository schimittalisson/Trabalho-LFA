import string
from collections import deque

class NFA:
    def __init__(self, estados, alfabeto, f_prog, start_state, final_state):
        self.estados = estados                    # Conjunto de estados
        self.alfabeto = alfabeto                  # Alfabeto
        self.f_prog = f_prog                      # Função programa
        self.start_state = start_state            # Estado inicial
        self.final_state = final_state            # Estado(s) final

    def read_string(self, input_str):             # Le a fita e verifica na quintupla do automato
        for c in input_str:                       # Verifica se a fita bate com os simbolos do alfabeto
            if c not in self.alfabeto:
                print('Possui simbolo que não pertence ao alfabeto!')
                return

        next_states = [self.start_state]
        for i in str:
            next_states = self.next_state(next_states, i)

        result = self.match_final_state(next_states)
        if result == True:
            print('Essa fita é aceita!')
        else:
            print('Essa fita não é aceita!')

    def fecho_e(self, state):                 # Procura um possivel Epsilon no automato
        d_state = deque()                       # Usa uma Double ended queue, armazenando o estado que chega Epsilon
        empty_bag = []
        d_state.append(state)
        empty_bag.append(state)

        while (len(d_state)):
            current_state = d_state[0]
            if current_state in self.f_prog.keys():  # Se o estado atual existe
                if 'e' in self.f_prog[current_state].keys():  # Checa se existe uma transição epsilon
                    for s in self.f_prog[current_state]['e']:
                        if s not in empty_bag:
                            d_state.append(s)   # Enfilera o estado que veio de uma transição epsilon
                            empty_bag.append(s)
            d_state.popleft()
        return empty_bag



    def next_state(self, current_states, c):    # A função retorna o conjunto de estados que o estado atual pode alcançar via um elemento do alfabeto
        next_states = []                        # Incluindo transições epsilon!
        for state in current_states:
            if state in self.f_prog.keys():
                if c in self.f_prog[state].keys():
                    n_states = self.f_prog[state][c]
                    for s in n_states:
                        s_closure = self.fecho_e(s)
                        for s_c in s_closure:
                            if s_c not in next_states:
                                next_states.append(s_c)
        print('Transição de estados:')
        print(current_states, end=' ')
        print('-' + c + '->', end=' ')
        print(next_states)
        return next_states       



    def match_final_state(self, final_current_states: list) ->bool :
        for state in final_current_states:
            if state in self.final_state:
                return True
        return False

    def print_quint(self):
        """Mostra a quintupla do automato """
        print("----5-TUPLA do AFD----")
        print("M = ({"+ ', '.join(self.alfabeto) +"},{"+ ', '.join(self.estados) +"}, P,"+ self.start_state +",{"+ ', '.join(self.final_state) +"})")




if __name__ == '__main__':
    print("Primeiro automato AFD")
    estados1 = ['q1', 'q2']   # Estados do automato
    alfabeto1 = ['0', '1']    # Alfabeto do automato
    f_prog1 = {
        'q1': {
            '0': ['q1'],
            '1': ['q2']
        }
    }                     # Função programa
    start_state1 = 'q1'                  # Estado inicial
    final_state1 = ['q2']                # Conjunto dos estados finais

    nfa1 = NFA(estados1, alfabeto1, f_prog1, start_state1, final_state1)
    nfa1.print_quint()

    str = input("Entre com a fita:")    
    nfa1.read_string(str)

    print("Segundo automato AFN")
    estados2 = ['q1', 'q2','q3']   # Estados do automato
    alfabeto2 = ['0', '1', '2']    # Alfabeto do automato
    f_prog2 = {
        'q1': {
            '0': ['q1'],
            '1': ['q1','q2']
        },
        'q2': {
            '0': ['q1'],
            '1': ['q2'],
            '2': ['q3']
        },
        'q3': {
            '0': ['q1','q3']
        }
    }                     # Função programa
    start_state2 = 'q1'                  # Estado inicial
    final_state2 = ['q2','q3']                # Conjunto dos estados finais

    nfa2 = NFA(estados2, alfabeto2, f_prog2, start_state2, final_state2)
    nfa2.print_quint()

    str2 = input("Entre com a fita:")    
    nfa2.read_string(str2)


    print("terceiro automato AFe")
    estados3 = ['q1', 'q2', 'q3', 'q4']   
    alfabeto3 = ['0', '1']                
    f_prog3 = {
        'q1': {
            '0': ['q1'],
            '1': ['q1', 'q2']
        },
        'q2': {
            'e': ['q3'],
            '0': ['q3']
        },
        'q3': {
            '1': ['q4']
        },
        'q4': {
            '0': ['q4'],
            '1': ['q4']
        }
    }                     
    start_state3 = 'q1'                  
    final_state3 = ['q4']

    nfa3 = NFA(estados3, alfabeto3, f_prog3, start_state3, final_state3)
    nfa3.print_quint()

    str3 = input("Entre com a fita:")    
    nfa3.read_string(str3)