from pgzero.builtins import Actor

class Dragon():
    def __init__(self, dragon_image: str, dragon_x: int, dragon_y: int,
                sleep_length: int, 
                sleep_counter: int, 
                wake_counter: int) -> None:
        """All attributes the dragon

        Parameters
        ----------
        dragon_image : str
            Dragons starting image
        dragon_x : int
            Dragons x position
        dragon_y : int
            Dragons y position
        sleep_length : int
            Amount of time the dragon will sleep in this lair
        sleep_counter : int
            How long the dragon has been asleep
        wake_counter : int
            How long the dragon has been awake
        """
        self.dragon_image = dragon_image
        self.dragon_x = dragon_x
        self.dragon_y = dragon_y
        self.dragon = Actor(self.dragon_image, pos=(self.dragon_x, self.dragon_y))
        self.sleep_length = sleep_length
        self.sleep_counter = sleep_counter
        self.wake_counter = wake_counter

    def dragon(self):
        return self.dragon

    def sleep_length(self):
        return self.sleep_length
        
    def sleep_counter(self):
        return self.sleep_counter
        
    def wake_counter(self):
        return self.wake_counter


class Eggs():
    def __init__(self, eggs_image: str, eggs_x: int,
                 eggs_y: int, egg_count: int, egg_hidden: bool,
                 egg_hide_counter: int) -> None:
        """All attributes the dragon

        Parameters
        ----------
        eggs_image : str
            Eggs starting image
        eggs_x : int
            Eggs x position
        eggs_y : int
            Eggs y position
        egg_count : int
            Number of eggs in dungeon
        egg_hidden : bool
            Are the eggs hidden?
        egg_hide_counter : int
            How many seconds the eggs have been hidden
        """
        self.eggs_image = eggs_image
        self.eggs_x = eggs_x
        self.eggs_y = eggs_y
        self.eggs = Actor(self.eggs_image, pos=(self.eggs_x, self.eggs_y))
        self.egg_count = egg_count
        self.egg_hidden = egg_hidden
        self.egg_hide_counter = egg_hide_counter

    def dragon(self):
        return self.dragon

    def eggs(self):
        return self.eggs

    def egg_count(self):
        return self.egg_count
        
    def egg_hidden(self):
        return self.egg_hidden
        
    def egg_hide_counter(self):
        return self.egg_hide_counter


class Lair(Dragon, Eggs):
    def __init__(self,  dragon_image: str, dragon_x: int, dragon_y: int,
                eggs_image: str, eggs_x: int, eggs_y: int, 
                egg_count: int, egg_hidden: bool, 
                egg_hide_counter: int, sleep_length: int, 
                sleep_counter: int, 
                wake_counter: int) -> None:
        Dragon.__init__(self, dragon_image, dragon_x, dragon_y, 
                        sleep_length, sleep_counter, wake_counter)
        Eggs.__init__(self, eggs_image, eggs_x, eggs_y, 
                        egg_count, egg_hidden, egg_hide_counter)

        """All attributes of everything in the liar
        """

class Easy_Lair(Lair):
    def __init__(self) -> None:
        Lair.__init__(self, "dragon-asleep",	"""dragons image"""
                        600, 				    """dragon x position"""
                        100,  				    """dragon y position"""
                        "one-egg", 			    """eggs image"""
                        400,  				    """eggs x position"""
                        100, 				    """eggs y position"""
                        1,					    """egg_count"""
                        False,				    """egg_hidden"""
                        0,					    """egg_hide_counter"""
                        10,					    """sleep_length"""
                        0,					    """sleep_counter"""
                        0)  					"""wake_counter"""
        """All attributes of the easy liar
        """

class Medium_Lair(Lair):
    def __init__(self) -> None:
        Lair.__init__(self, "dragon-asleep",	"""dragons image"""
                        600, 				    """dragon x position"""
                        300,  				    """dragon y position"""
                        "two-eggs", 			"""eggs image"""
                        400,  				    """eggs x position"""
                        300, 				    """eggs y position"""
                        2,					    """egg_count"""
                        False,				    """egg_hidden"""
                        0,					    """egg_hide_counter"""
                        7,					    """sleep_length"""
                        0,					    """sleep_counter"""
                        0)  					"""wake_counter"""
        """All attributes of the medium liar
        """

class Hard_Lair(Lair):
    def __init__(self) -> None:
        Lair.__init__(self, "dragon-asleep",	"""dragons image"""
                        600, 				    """dragon x position"""
                        500,  				    """dragon y position"""
                        "three-eggs", 			"""eggs image"""
                        400,  				    """eggs x position"""
                        500, 				    """eggs y position"""
                        3,					    """egg_count"""
                        False,				    """egg_hidden"""
                        0,					    """egg_hide_counter"""
                        4,					    """sleep_length"""
                        0,					    """sleep_counter"""
                        0)  					"""wake_counter"""
        """All attributes of the hard liar
        """