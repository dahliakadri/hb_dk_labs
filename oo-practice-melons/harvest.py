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
        self.is_seedless = bool(is_seedless)
        self.is_bestseller = bool(is_bestseller)
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

    def __repr__(self):
        return self.name


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []
    muskmelon = MelonType('musk', 1998, 'green', True, True, 'muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)
    casaba = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)
    yellowwatermelon = MelonType('yw', 2013, 'yellow', True, True, 'yellow watermelon')
    yellowwatermelon.add_pairing('ice cream')
    all_melon_types.append(yellowwatermelon)

    return all_melon_types


def print_pairing_info(all_melon_types):
    """Prints information about each melon type's pairings."""
    
    for melon in all_melon_types:
        print(f'{melon.name} pairs with:')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print('')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_list = melon_types
    melon_dict = {}
    for melon in melon_list:
        melon_dict[melon.code] = melon

    return melon_dict
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, melon_number, shape_rating, color_rating,
        harvest_field, harvester):
        
        #melon_type is a list of MelonType objects
        self.melon_type = melon_type
        self.melon_number = melon_number
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvester = harvester

    def is_sellable(self, shape_rating, color_rating, harvest_field):
        return shape_rating > 5 and color_rating > 5 and harvest_field != 3

def make_melons(all_melon_types_list):
    """Returns a list of Melon objects."""

    for melon in all_melon_types_list:
        melon_1 = Melon(melon.code, 8, 7, 2, 'Sheila')
        all_melon_list.append(melon_1)
        melon_2 = Melon(melon.code, 3, 4, 2, 'Sheila')
        all_melon_list.append(melon_2)
        melon_3 = Melon(melon.code, 9, 8, 3, 'Sheila')
        all_melon_list.append(melon_3)


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



