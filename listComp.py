# list comp:   [new_value for element in iterable if...]


new_list = []
for letter in 'Coding Temple':
    new_value = letter.upper()
    if new_value.isalpha():
        new_list.append(new_value)
print(new_list)

#SINGLE LINE:

new_list = [letter.upper() for letter in 'Coding Temple' if letter.upper().isalpha()]

print(new_list)

# for the MRData, get drivers fullname from Dictionary
data = ''
fullname = f"{data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][0]['Driver']['givenName']}  {data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][0]['Driver']['familyName']}"
print(fullname)

#turn into a loop to get all the drivers names
for element in data['MRData']['StandingsTable']['StandingLists'][0]['DriverStandings']:
    print('first Name:' + element['Driver']['givenName'])
    print('first Name:' + element['Driver']['familyName'])

    # --OR-------------
    names=[]
    fullname = f"{element['Driver']['givenName']} {element['Driver']['familyName']}"
    names.append(fullname)
    print(names)

    #--TRANSLATE TO LIST COMPREHENSION--
    names = [f"{element['Driver']['givenName']} {element['Driver']['familyName']}" for element in data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']]
    print(names)

#MRData DICTIONARY
fDrivers = {}
for element in data['MRData']['StandingsTable']['StandingsList'][0]['DriverStandings']:
    full_name = f"{element['Driver']['givenName']} {element['Driver']['familyName']}"
    number = element['Driver']['permanentNumber']
    print(number, full_name)
    fDrivers[number] = full_name #dict[key] = value
