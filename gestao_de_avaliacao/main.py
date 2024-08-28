import csv
import os
from tabulate import tabulate
def pausa():
    pausar = input('Pressione ENTER para continuar...')

def limpar():
    os.system('cls')

path = 'turma01.csv'
i = 0
while path[i] != '.':
    i += 1
    new_path = path[0:i] + '_avaliacoes.csv'
try:
    file = open(path,"r")
    read = csv.reader(file)

    names = []
    emails = []
    dates = []
    grades = []

    for value in read:
        names.append(value[0])
        emails.append(value[1])
        dates.append(value[2])
        grades.append(int(value[3]))

    while True:    
        print("""
    GESTÃO DE CLASSIFICAÇÕES
    C - Converter classificações
    E - Exportar classificações
    T - Terminar 
        """)
        option = input('Escolha uma opção: ')
        limpar()

        table = [
            ['Nome','Avaliação','Qualitativa']
        ]
        if option == 'C' or  option == 'c':
            i = 0
            list_grades = []
            info = []
            convert_grades = ''
            while ( i< len(grades)):
                if grades[i] < 90:
                    convert_grades = 'Insuficiente'

                elif grades[i] > 90 and grades[i] < 130:
                    convert_grades = 'Suficiente'

                elif grades[i] > 130 and grades[i] < 170:
                    convert_grades = 'Bom'

                elif grades[i] > 170 and grades[i] <= 190:
                    convert_grades = 'Muito Bom'

                elif grades[i] > 190:
                    convert_grades = 'Excelente'

                list_grades.append(convert_grades)

                info = [names[i],grades[i],list_grades[i]]
                table.append(info)
                i+=1

            print(tabulate(table,headers="firstrow",tablefmt="pretty"))    
            pausa()
            limpar()



        elif option == 'E' or option == 'e':
            try:
                cabecalho = ['Nomes', 'Emails','Data de Nascimento','Notas','Avaliacoes']
                file = open(new_path,'w',newline='')
                write = csv.writer(file)
                write.writerow(cabecalho)
                i = 0
                while (i < len(names)): 
                    info = []
                    info.append(names[i])
                    info.append(emails[i])
                    info.append(dates[i])
                    info.append(grades[i])
                    info.append(list_grades[i])

                    file = open(new_path,'a+',newline='')
                    write = csv.writer(file)
                    write.writerow(info)

                    i+=1
                print('Avaliações exportadas com sucesso')
            except:
                print('Precisa de converter as avaliações')    
        elif option == 'T' or option == 't':
            break
        else:
            print('Opção Inválida')
except:
    print("Não foi possível encontrar o ficheiro")