mm = [
    [False, False],
    [False, True],
    [True, False],
    [True, True]
]


def questionary():
    def print_presentation():
        print("Apresenta um ou mais desses sintomas? [s/n]")
        print("\tTosse; OU")
        print("\tDor de garganta; OU")
        print("\tCoriza")

    sm = 0
    awnsers = []
    while True:
        print_presentation()
        match input():
            case 's':
                sm += 1
                awnsers.append(True)
                break
            case 'n':
                awnsers.append(False)
                break
            case _:
                print("Resposta incorreta.")

    print("Apresenta esses sintoma em conjunto com os anteriores?")
    print("\t Dificuldade respiratoria? [s/n]")
    if input() == 's':
        sm += 1
        awnsers.append(True)
    else:
        awnsers.append(False)
    return awnsers


def calcula_suspeito(awnsers):
    sm = 0
    i = 0
    print(awnsers)
    while i < 2:
        if((mm[i][0] == awnsers[0]) and (mm[i][1] == awnsers[1])):
            sm = mm[i][0] + mm[i][1]
        i += 1
    return sm


def main():
    awnsers = questionary()
    result = calcula_suspeito(awnsers)
    if(result < 2):
        print("Sem suspeita de covid-19;")
    else:
        print("Paciente com suspeita de covid-19.")


if __name__ == '__main__':
    main()
