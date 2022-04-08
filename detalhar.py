from browser import document, alert

def click(event):
    h = document["input_horario"].value
    document["text_resultado"].text = detalhar_horario(h.upper())
document["btn_horario"].bind("click", click)


def detalhar_horario(h):
    ah = []
    try:
        for i in h:
            ah.append(i)

        for i in range(len(ah)):
            ah[i] = ah[i].upper()
            
            if ah[i] == 'T':
                ah[i] = 'Tarde'
                turno_pos = i
            

            elif ah[i] == 'M':
                ah[i] = 'Manhã'
                turno_pos = i

        c = 0
        teste = [[]]
        for i in ah:
            if i.isdigit():
                teste[c].append(i)
            elif i.isalpha():
                teste.append([i])
                teste.append([])
                c += 2

        for i in range(len(teste[0])):
            if teste[0][i] == '2':
                teste[0][i] = 'Segunda'
            elif teste[0][i] == '3':
                teste[0][i] = 'Terça'
            elif teste[0][i] == '4':
                teste[0][i] = 'Quarta'
            elif teste[0][i] == '5':
                teste[0][i] = 'Quinta'
            elif teste[0][i] == '6':
                teste[0][i] = 'Sexta'

        turn = ''.join(teste[1])
        for i in range(len(teste[2])):

            if turn == 'Tarde':

                if teste[2][i] == '1':
                    teste[2][i] = 'Primeiro horario: 13h'
                elif teste[2][i] == '2':
                    teste[2][i] = 'Segundo horario: 14h'
                elif teste[2][i] == '3':
                    teste[2][i] = 'Terceiro horario: 15h'
                elif teste[2][i] == '4':
                    teste[2][i] = 'Quarto horario: 16h'
                elif teste[2][i] == '5':
                    teste[2][i] = 'Quinto horario: 17h'
                elif teste[2][i] == '6':
                    teste[2][i] = 'Sexto horario: 18h'

            else:

                if teste[2][i] == '1':
                    teste[2][i] = 'Primeiro horario: 7h'
                elif teste[2][i] == '2':
                    teste[2][i] = 'Segundo horario: 8h'
                elif teste[2][i] == '3':
                    teste[2][i] = 'Terceiro horario: 9h'
                elif teste[2][i] == '4':
                    teste[2][i] = 'Quarto horario: 10h'
                elif teste[2][i] == '5':
                    teste[2][i] = 'Quinto horario: 11h'
                elif teste[2][i] == '6':
                    teste[2][i] = 'Sexto horario: 12h'

        view = f'''\n -- : 

            \t\t\t  Dia: [ {' - '.join(teste[0])} ]
            \t\t\t  Turno: [ {''.join(teste[1])} ]
            \t\t\t  Hora: [ {' - '.join(teste[2])} ]

                '''
        print(view)
        return view
    except:
        print("\nDigite o horario corretamente")
