def generateCalendar(days, hours):

    #Start calendar
    sb = "BEGIN:VCALENDAR\nPRODID:-//Liferay Inc//Liferay Portal 6.1.1//EN\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"

    dtstamp = "20200629T055033Z" # TODO: Pendent agafar l'hora automàticament.
    summary = "Cita prèvia"
    description = ""
    location = ""
    comment = "cita_previa_lliure"    
    
    for day in days:
        for hour in hours:
            dtstart = "2020" + day + "T" + hour[0] + "00"
            dtend = "2020" + day + "T" + hour[1] +"00"
            sb = sb + generateEvent(dtstamp, dtstart, dtend, summary, description, location, comment)

    #End calendar
    sb = sb + "END:VCALENDAR"

    return sb


def generateEvent(dtstamp, dtstart, dtend, summary, description, location, comment): 

    sb = "BEGIN:VEVENT\n"
    sb = sb + "DTSTAMP:" + dtstamp + "\n" 
    #sb = sb + "UID:\n" #UID:b04e7f6b-e05e-45e4-8f0b-d07eb5659f14
    sb = sb + "DTSTART:" + dtstart + "\n" 
    sb = sb + "DTEND:" + dtend + "\n"    
    sb = sb + "SUMMARY:" + summary + "\n"    
    sb = sb + "DESCRIPTION:" + description +"\n"    
    sb = sb + "LOCATION:" + location + "\n"    
    sb = sb + "COMMENT:" + comment + "\n"    
    sb = sb + "END:VEVENT\n"

    return sb
    