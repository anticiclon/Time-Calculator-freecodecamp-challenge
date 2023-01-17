# -*- coding: utf-8 -*-

dia_semana = {'monday' : 0 , 'tuesday' : 1 , 'wednesday' : 2 , 'thursday' : 3 , 
              'friday' : 4 , 'saturday' : 5, 'sunday' : 6}

def es_dia_semana(var):
    var =str(var)
    var = var.lower()
    return var in dia_semana

def dame_dia(var):
    var = var % 7
    for key, value in dia_semana.items():
        if var == value:
            return key.capitalize()



def dime_dia(var):
    return dia_semana.get(var.lower())



digitos = set('0123456789')

def es_digito(var):
    return var in digitos

def dame_numero(varstr):
    s = ""
    for c in varstr:
        s += c
    return (int(s))


def lector_tiempo(hora):
    hora_completa = hora.split()
    hora_parcial = hora_completa[0].split(":")
    horas = dame_numero(hora_parcial[0])
    minutos = dame_numero(hora_parcial[1])
    try:
        if hora_completa[1] == "PM":
            horas = horas + 12
    except IndexError:
        pass
    return (horas, minutos)



def suma_tiempo(hora1, hora2):
    h_total = hora1[0]+ hora2[0]
    m_total = hora1[1]+hora2[1]
    dias = 0
    if m_total > 59:
        m_total = m_total - 60
        h_total = h_total + 1
    if h_total > 24:
        dias = h_total // 24
        h_total = h_total % 24
    return (h_total, m_total, dias)


    
def dame_resultado(tiempo, tiempo_adicional, dia_semana = "ninguno"):
    tiempo_inicial = lector_tiempo(tiempo)
    tiempo_adicional = lector_tiempo(tiempo_adicional)
    (hora, minuto, dias) = suma_tiempo(tiempo_inicial, tiempo_adicional)
    if es_dia_semana(dia_semana):
        nuevo_dia = dime_dia(dia_semana) + dias
        resultado = (hora, minuto, dias, nuevo_dia)
    else:
        resultado = (hora, minuto, dias)
    return resultado



def add_time(start, duration, weekday = "ninguno"):
    if es_dia_semana(weekday):
        (hora, minuto, dias, nuevo_dia) = dame_resultado(start, duration, weekday)
        if hora < 12:
            if hora == 0:
                hora = 12
                new_time = ["%2d:%02d" % (hora, minuto) + " AM"]
            elif hora < 10:
                new_time = ["%1d:%02d" % (hora, minuto) + " AM"]
            else:
                new_time = ["%2d:%02d" % (hora, minuto) + " AM"]
        else:
            hora = hora-12
            if hora == 0:
                hora = 12
                new_time =  ["%2d:%02d" % (hora, minuto) +" PM"]
            elif hora < 10:
                new_time =  ["%1d:%02d" % (hora, minuto) +" PM"]
            else:
                new_time =  ["%2d:%02d" % (hora, minuto) +" PM"]
        new_time.append(dame_dia(nuevo_dia))
        if dias == 0:
            new_time = new_time[0] + ', ' + new_time[1]
        elif dias == 1:
            new_time = new_time[0] + ', ' + new_time[1] + ' (next day)'
        else:
            new_time = new_time[0] + ', ' + new_time[1] + " ("+ str(dias)+ " days later)"
        return new_time
    else:
        (hora, minuto, dias) = dame_resultado(start, duration)
        if hora < 12:
            if hora == 0:
                hora = 12
                new_time = ["%2d:%02d" % (hora, minuto) + " AM"]
            elif hora < 10:
                new_time = ["%1d:%02d" % (hora, minuto) + " AM"]
            else:
                new_time = ["%2d:%02d" % (hora, minuto) + " AM"]
        else:
            hora = hora-12
            if hora == 0:
                hora = 12
                new_time =  ["%2d:%02d" % (hora, minuto) +" PM"]
            elif hora < 10:
                new_time =  ["%1d:%02d" % (hora, minuto) +" PM"]
            else:
                new_time =  ["%2d:%02d" % (hora, minuto) +" PM"]
        if dias == 0:
            pass
        elif dias == 1:
            new_time.append('(next day)')
        else:
            new_time.append("("+ str(dias)+ " days later)")
        resultado = ' '.join(new_time)
    return resultado
