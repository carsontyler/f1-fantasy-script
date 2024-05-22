# Driver data
drivers = {
    'Verstappen': {'cost': 30.3, 'points': 161},
    'Perez': {'cost': 29.2, 'points': 161},
    # 'Leclerc': {'cost': 28.2, 'points': 159},
    'Norris': {'cost': 28.7, 'points': 156},
    # 'Sainz': {'cost': 26.3, 'points': 155},
    'Russell': {'cost': 22.2, 'points': 139},
    'Alonso': {'cost': 21.6, 'points': 139},
    'Hamilton': {'cost': 20.1, 'points': 129},
    'Piastri': {'cost': 19.7, 'points': 141},
    # 'Hulkenberg': {'cost': 15.2, 'points': 121},
    # 'Tsunoda': {'cost': 14.9, 'points': 117},
    'Albon': {'cost': 9.1, 'points': 100},
    'Stroll': {'cost': 13.5, 'points': 114},
    'Ocon': {'cost': 12.7, 'points': 107},
    'Gasly': {'cost': 10.8, 'points': 97},
    'Magnussen': {'cost': 9.4, 'points': 107},
    'Ricciardo': {'cost': 9.6, 'points': 103},
    'Zhou': {'cost': 9.1, 'points': 101},
    'Bottas': {'cost': 5.3, 'points': 92},
    'Sargeant': {'cost': 4.4, 'points': 87}
}

# Team data
teams = {
    'Red Bull': {'cost': 29.1, 'points': 167},
    'Ferrari': {'cost': 26.4, 'points': 158},
    'McLaren': {'cost': 25.6, 'points': 145},
    'Mercedes': {'cost': 20.9, 'points': 136},
    'Aston Martin': {'cost': 16.2, 'points': 110},
    'Alpine': {'cost': 13.8, 'points': 88},
    'Haas': {'cost': 12.9, 'points': 95},
    'RB': {'cost': 14.3, 'points': 98},
    'Williams': {'cost': 7.0, 'points': 75},
    'Sauber': {'cost': 7.5, 'points': 78}
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

numDrivers = 1
budget = 17.2
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