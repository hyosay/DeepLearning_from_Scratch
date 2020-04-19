def centuryFromYear(year):
    cen = year / 100
    if int(cen) < float(cen):
        print(int(cen) + 1)
    elif int(cen) == float(cen):
        print(int(cen))
centuryFromYear(int(input()))