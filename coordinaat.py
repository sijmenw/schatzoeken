# created by Sijmen van der Willik
# 04/02/2018 14:02

import json


class Coordinaat(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Schatkaart:
    def __init__(self, path):
        # vanaf hier wordt de file geladen en geparset
        with open(path) as f:
            content = f.readlines()

        content = [x.strip() for x in content]

        start_punt, *instructies = content

        start_punt = json.loads(start_punt)

        self.start_punt = Coordinaat(start_punt[0], start_punt[1])
        self.instructies = instructies
        # hier is alles ingevoerd uit de .txt file

voorbeeld = Schatkaart("treasure_maps/map0.txt")

print("Startpunt X:", voorbeeld.start_punt.x)
print("Startpunt Y:", voorbeeld.start_punt.y)
print("Startpunt instructies:", voorbeeld.instructies)
