perHour = input("Bitte gebe deinen Netto Stundenlohn ein: ")
day = 8 * int(perHour)
month = 20 * day
year = 12 * month
print(f"Du verdienst {perHour} Euro pro stunde")
print(f"Du verdienst {day} Euro pro Tag")
print(f"Du verdienst {month} Euro pro Monat")
print(f"In einem Jahr verdienst du {year} Euro")
input("Drücke eine beliebige Taste")
