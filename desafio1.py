def converte(hora):
    ampm = hora[-2:]
    hora = hora[:8]
    hs = hora.split(":")

    print(hora, 'ampm', ampm)
    print(hs)

    if ampm == 'PM':
        if hs[0] == '12':
            hs[0] = '00'
        else:
            hs[0] = int(hs[0]) + 12
    else:
        if hs[0] == '12':
            hs[0] = '12'

    return print(str(hs[0]) + ":" + hs[1] + ":" + hs[2])


hora = '02:00:00PM'
converte(hora)
