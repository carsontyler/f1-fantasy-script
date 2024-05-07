# Driver data
drivers = {
    'Verstappen': {'cost': 30.3, 'points': 161},
    # 'Perez': {'cost': 29.2, 'points': 161},
    'Leclerc': {'cost': 28.2, 'points': 159},
    'Norris': {'cost': 28.7, 'points': 156},
    'Sainz': {'cost': 26.3, 'points': 155},
    # 'Russell': {'cost': 22.2, 'points': 139},
    'Alonso': {'cost': 21.6, 'points': 139},
    'Hamilton': {'cost': 20.1, 'points': 129},
    # 'Piastri': {'cost': 19.7, 'points': 141},
    'Hulkenberg': {'cost': 15.2, 'points': 121},
    'Tsunoda': {'cost': 14.9, 'points': 117},
    'Albon': {'cost': 11.1, 'points': 105},
    # 'Stroll': {'cost': 11.5, 'points': 111},
    'Ocon': {'cost': 13.2, 'points': 110},
    'Gasly': {'cost': 11.8, 'points': 102},
    # 'Magnussen': {'cost': 7.8, 'points': 105},
    'Ricciardo': {'cost': 8.6, 'points': 103},
    # 'Zhou': {'cost': 9.1, 'points': 102},
    'Bottas': {'cost': 5.7, 'points': 94},
    # 'Sargeant': {'cost': 4.0, 'points': 90}
}

# Team data
teams = {
    'Red Bull': {'cost': 29.1, 'points': 167},
    'Ferrari': {'cost': 26.4, 'points': 158},
    'McLaren': {'cost': 25.6, 'points': 145},
    'Mercedes': {'cost': 20.9, 'points': 136},
    'Aston Martin': {'cost': 18.1, 'points': 128},
    'Alpine': {'cost': 14.0, 'points': 103},
    'Haas': {'cost': 11.9, 'points': 105},
    'RB': {'cost': 12.9, 'points': 106},
    'Williams': {'cost': 7.7, 'points': 89},
    'Sauber': {'cost': 7.5, 'points': 89}
}

def find_best_lineup(drivers, teams, budget):
    best_lineup = None
    max_average_points = 0
    
    for driver1 in drivers:
        for driver2 in drivers:
            if driver2 == driver1:
                continue
            for driver3 in drivers:
                if driver3 == driver1 or driver3 == driver2:
                    continue
                for driver4 in drivers:
                    if driver4 == driver1 or driver4 == driver2 or driver4 == driver3:
                        continue
                    for driver5 in drivers:
                        if driver5 == driver4 or driver5 == driver1 or driver5 == driver2 or driver5 == driver3:
                            continue
                        for team in teams:
                            total_cost = drivers[driver1]['cost'] + drivers[driver2]['cost'] + drivers[driver3]['cost'] + drivers[driver4]['cost'] + drivers[driver5]['cost'] + teams[team]['cost']
                            if total_cost <= budget:
                                average_points = (drivers[driver1]['points'] + drivers[driver2]['points'] + drivers[driver3]['points'] + drivers[driver4]['points'] + drivers[driver5]['points']) / 5
                                if average_points > max_average_points:
                                    max_average_points = average_points
                                    best_lineup = (driver1, driver2, driver3, driver4, driver5, team)
    
    return best_lineup, max_average_points

best_lineup, average_team_points = find_best_lineup(drivers, teams, 101.5)
print("Best lineup under budget:")
print("Driver 1:", best_lineup[0])
print("Driver 2:", best_lineup[1])
print("Driver 3:", best_lineup[2])
print("Driver 4:", best_lineup[3])
print("Driver 5:", best_lineup[4])
print("Team:", best_lineup[5])
print("Average Team Points:", average_team_points)
