from pprint import pprint
############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def __repr__(self):
        return '{}'.format(self.name)

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairing.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, "Muskmelon")
    musk.pairings.append('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, "Casaba")
    casaba.pairings.extend(['strawberries', 'mint'])
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    crenshaw.pairings.append('prosciutto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', True, True, "Yellow Watermelon")
    yellow_watermelon.pairings.append('ice cream')
    all_melon_types.append(yellow_watermelon)
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print("{0} pairs with:".format(melon.name))
        for food in melon.pairings:
            print("\t-{}".format(food))

# melon_types = make_melon_types()
# print_pairing_info(melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        code = melon.code
        melon_dict[code] = melon 

    return melon_dict

##testing
# melon_types = make_melon_types()
# melon_dict = make_melon_type_lookup(melon_types)
# pprint(melon_dict)
# casaba = melon_dict["cas"]
# print(casaba.color)
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def __repr__(self):
        return '{}'.format(self.melon_type)

    def is_sellable(self, shape_rating, color_rating, field):
        #reject melons from field 3 that was accidentally poisoned by neighboring farm
        if field == 3:
            return False
        #melons are sellable if they meet color and shape standard greater than 5
        elif int(shape_rating) > 5 and int(color_rating) > 5:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []
    melon_dict = make_melon_type_lookup(melon_types)

    melon1 = Melon(melon_dict['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melon_dict['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melon_dict['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melon_dict['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melon_dict['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melon_dict['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melon_dict['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melon_dict['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melon_dict['yw'], 7, 10, 3, 'Sheila')

    melons.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable(melon.shape_rating, melon.color_rating, melon.field):
            print("Harvested by {0} from Field {1} CAN BE SOLD".format(melon.harvester, melon.field))
        else:
            print("Harvested by {0} from Field {1} NOT SELLABLE".format(melon.harvester, melon.field))



def imported_melons(melon_log):
    '''
    Read melon log and return list of Melon objects 
    '''
    melons = []

    with open(melon_log) as log:

        for line in log:
            line.strip()
            words = line.split(" ")
            shape_rating = words[1]
            color_rating = words[3]
            code = words[5]
            harvester = words[8]
            field = words[11]

            melon = Melon(melon_dict[code], shape_rating, color_rating, field, harvester)
            melons.append(melon)

    return melons

#test
melon_types = make_melon_types()
melon_dict = make_melon_type_lookup(melon_types)
melons = imported_melons('harvest_log.txt')
for melon in melons:
    print(melon.is_sellable(melon.shape_rating, melon.color_rating, melon.field))

