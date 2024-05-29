# Driver data
drivers = {
    'Verstappen': {'cost': 29.3, 'points': 159},
    # 'Perez': {'cost': 25.2, 'points': 151},
    'Leclerc': {'cost': 28.4, 'points': 165},
    'Norris': {'cost': 28.6, 'points': 159},
    # 'Sainz': {'cost': 26.8, 'points': 158},
    'Russell': {'cost': 23.4, 'points': 139},
    'Alonso': {'cost': 18.7, 'points': 132},
    'Hamilton': {'cost': 21.1, 'points': 131},
    # 'Piastri': {'cost': 23.7, 'points': 147},
    'Hulkenberg': {'cost': 13.4, 'points': 116},
    'Tsunoda': {'cost': 16.9, 'points': 123},
    'Albon': {'cost': 11.1, 'points': 104},
    'Stroll': {'cost': 12.9, 'points': 112},
    'Ocon': {'cost': 11, 'points': 102},
    'Gasly': {'cost': 12.5, 'points': 98},
    # 'Magnussen': {'cost': 7.4, 'points': 101},
    # 'Ricciardo': {'cost': 10.3, 'points': 102},
    'Zhou': {'cost': 8.7, 'points': 99},
    'Bottas': {'cost': 7.3, 'points': 94},
    'Sargeant': {'cost': 5.6, 'points': 86}
}

# Team data
teams = {
    'Red Bull': {'cost': 25.7, 'points': 142},
    # 'Ferrari': {'cost': 27.4, 'points': 145},
    # 'McLaren': {'cost': 26.8, 'points': 139},
    # 'Mercedes': {'cost': 21.8, 'points': 121},
    # 'Aston Martin': {'cost': 14.8, 'points': 107},
    # 'Alpine': {'cost': 13.7, 'points': 87},
    # 'Haas': {'cost': 10.9, 'points': 90},
    # 'RB': {'cost': 16.1, 'points': 98},
    # 'Williams': {'cost': 9.2, 'points': 77},
    # 'Sauber': {'cost': 7.5, 'points': 78}
}

def find_best_lineup(drivers, teams, budget, numDrivers, teamNeeded):
    best_lineup = None
    max_average_points = 0
    max_total_cost = 0
    d1c, d2c, d3c, d4c, d5c, t1c, d1p, d2p, d3p, d4p, d5p, t1p = (0,)*12

    for driver1 in drivers:
        d1c = drivers[driver1]['cost']
        d1p = drivers[driver1]['points']
        for driver2 in drivers:
            if driver2 != driver1 and numDrivers >= 2:
                d2c = drivers[driver2]['cost']
                d2p = drivers[driver2]['points']
            for driver3 in drivers:
                if driver3 != driver1 and driver3 != driver2 and numDrivers >= 3:
                    d3c = drivers[driver3]['cost']
                    d3p = drivers[driver3]['points']
                for driver4 in drivers:
                    if driver4 != driver1 and driver4 != driver2 and driver4 != driver3 and numDrivers >= 4:
                        d4c = drivers[driver4]['cost']
                        d4p = drivers[driver4]['points']
                    for driver5 in drivers:
                        if driver5 != driver4 and driver5 != driver1 and driver5 != driver2 and driver5 != driver3 and numDrivers >= 5:
                            d5c = drivers[driver5]['cost']
                            d5p = drivers[driver5]['points']
                        for team in teams:
                            if teamNeeded:
                                t1c = teams[team]['cost']
                                t1p = teams[team]['points']
                            total_cost = d1c + d2c + d3c + d4c + d5c + t1c
                            if total_cost <= budget:
                                totalToDivideBy = numDrivers + (1 if teamNeeded else 0)
                                average_points = (d1p + d2p + d3p + d4p + d5p + t1p) / totalToDivideBy
                                if average_points > max_average_points:
                                    max_average_points = average_points
                                    max_total_cost = total_cost
                                    best_lineup = (driver1, driver2, driver3, driver4, driver5, team)
    
    return best_lineup, max_average_points, max_total_cost

numDrivers = 3
budget = 49.2
teamNeeded = True
best_lineup, average_team_points, max_total_cost = find_best_lineup(drivers, teams, budget, numDrivers, teamNeeded)
print("Best lineup under budget:")
print("Driver 1:", best_lineup[0])
if numDrivers >= 2:
    print("Driver 2:", best_lineup[1])
if numDrivers >= 3:
    print("Driver 3:", best_lineup[2])
if numDrivers >= 4:
    print("Driver 4:", best_lineup[3])
if numDrivers >= 5:
    print("Driver 5:", best_lineup[4])
if teamNeeded:
    print("Team:", best_lineup[5])
print("Average Team Points:", average_team_points)
print("Total Cost:", max_total_cost)