"""

01219114 Computer Programming
Week 8, Long Program Assignment: Mother Tux's Gold Shop (V1)
(C) 2024 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

DISCLAIMER: This task does NOT suggest any form of investment or financial
advice. NOR it does imply that the author understands any form of gold or
commodity trade. Treat this problem as a completely fantasy scenario.

"""


class Gold:
    """
    Represents a gold piece, any kind.

    Attributes:
    name -- the name of the piece of gold
    gold_mass -- the mass of gold in grams, initialize as 0
    total_mass -- the total mass of the piece in grams, initialize as 0
    markup_add -- how much to ADD to the value when attempting to sell in THB
                  default value for markup_add is 0.

    >>> g = Gold()
    >>> g.markup_add = 100
    >>> g.markup_add
    100
    """

    def __init__(self,
                 name: str = "Gold",
                 markup: int = 0):
        """
        Create a new piece of gold. Its name can be specified.
        If name is not given, then it is simply called "Gold".
        Do not change the case.

        >>> Gold('a').name
        'a'
        >>> Gold().name
        'Gold'
        >>> Gold().gold_mass
        0
        >>> Gold().total_mass
        0
        >>> Gold().markup_add
        0
        """

        self.name = name
        self.gold_mass = 0
        self.total_mass = 0
        self.markup_add = markup

    def add(self, is_gold: bool, amount: int) -> None:
        """
        Add some mass to the piece. This will increase the
        total mass of the piece.
        If it's gold, increase the gold mass too.

        >>> g = Gold()

        Adding non-gold mass
        >>> g.add(False, 10)
        >>> g.total_mass, g.gold_mass
        (10, 0)

        Add gold mass
        >>> g.add(True, 5)
        >>> g.total_mass, g.gold_mass
        (15, 5)
        """
        self.total_mass += amount

        if is_gold:
            self.gold_mass += amount

    def remove(self, is_gold: bool, amount: int) -> int:
        """
        Remove some mass from the piece, and return the
        actual mass removed as int.

        (Doctest Setup)
        >>> g = Gold()
        >>> g.add(False, 30)
        >>> g.total_mass, g.gold_mass
        (30, 0)
        >>> g.add(True, 30)
        >>> g.total_mass, g.gold_mass
        (60, 30)

        If all mass requested can be removed, return that amount
        >>> g.remove(False, 10)
        10
        >>> g.total_mass, g.gold_mass
        (50, 30)

        In this case, there is not enough non-gold mass, so only
        a partial amount is returned. In this case, only 20 grams
        can be removed, so return the number 20.
        >>> g.remove(False, 40)
        20
        >>> g.total_mass, g.gold_mass
        (30, 30)
        """
        if is_gold:
            removable_mass = min(self.gold_mass, amount)
            self.gold_mass -= removable_mass
        else:
            removable_mass = min(self.total_mass - self.gold_mass, amount)

        self.total_mass -= removable_mass

        return removable_mass

    def price(self,
              per_gram: int = 2000,
              include_markup: bool = True,
              force_purity: float = None) -> int:
        """
        Returns the appraised price of the gold artifact.
        Price is calculated per gram OF GOLD. If the price per gram is not
        given, force it to 2000 baht per gram.

        (Doctest Setup)
        >>> g = Gold()
        >>> g.add(False, 10)
        >>> g.add(True, 10)
        >>> g.markup_add = 1000

        Normally it should be:
        (self.gold_mass * per_gram) + self.markup_add

        Of course, don't add self.markup_add if include_markup is False.

        >>> g.price()
        21000
        >>> g.price(3000)
        31000
        >>> g.price(include_markup = False)
        20000
        >>> g.price(3000, include_markup = False)
        30000

        However, if purity is forced (not None), the formula now uses:
        (force_purity * self.total_mass * per_gram) + self.markup_add

        >>> g.price(2000, include_markup = True, force_purity = 1.00)
        41000
        >>> g.price(2000, include_markup = True, force_purity = 0.75)
        31000

        Round price down to integer!

        Forcing purity value is a way for us to sell gold at a profit, so
        don't forget to force purity value when told to.
        """
        if force_purity is not None:
            price = force_purity * self.total_mass * per_gram
        else:
            price = self.gold_mass * per_gram

        if include_markup:
            price += self.markup_add

        return int(price)

    def purity(self) -> float:
        """
        Return the purity of the gold piece.

        (Doctest Setup)
        >>> g = Gold()

        Pure gold should return a value of 1. For example, this one-gram piece
        of gold is completely pure.
        >>> g.add(True, 1)
        >>> g.purity()
        1.0

        Of course, if we add one gram of non-gold material, its purity is
        reduced.
        >>> g.add(False, 1)
        >>> g.purity()
        0.5

        Use the round builtin function to limit the number of digits to 4.
        In this case, now the gold piece has 1 g gold in 222 g total mass,
        making the purity only 0.0045.
        >>> g.add(False, 220)
        >>> g.purity()
        0.0045

        (THIS IS NOT THE SAME AS THE F-STRING)

        For the purpose of this exercise, assume that gold will always have
        some positive mass before this method is ever called.

        """
        purity = self.gold_mass / self.total_mass

        return round(purity, 4)

    def __repr__(self):
        """
        The STRING REPRESENTATION of the gold piece must look like this:

        Gold: <self.name>, <self.gold_mass> g / <self.total_mass> g

        Do not display the brackets.

        >>> g = Gold("Test")
        >>> g.add(False, 10)
        >>> g.add(True, 20)
        >>> g
        Gold: Test, 20 g / 30 g
        """
        return f"Gold: {self.name}, {self.gold_mass} g / {self.total_mass} g"

    def __eq__(self, other):
        """
        Two gold objects are considered equal only when:
        - The gold masses are equal
        - The total masses are equal
        - The markup amounts are equal

        Since all gold, if initialized like this, have zero gold and non-gold
        masses, it could be said that 'All Gold is Born Equal.'
        >>> a = Gold()
        >>> b = Gold()

        >>> a == b
        True

        Changes would make them unequal or equal based on the nature of those
        changes.

        >>> a.add(False, 50)
        >>> a == b
        False
        >>> b.add(False, 50)
        >>> a == b
        True
        >>> a.add(True, 100)
        >>> a == b
        False
        >>> b.add(True, 200)
        >>> a == b
        False

        Shave off 100 grams from b ...
        >>> b.remove(True, 100)
        100

        ... and it's now equal.
        >>> a == b
        True

        >>> a.remove(False, 10)
        10
        >>> a == b
        False

        """
        if isinstance(other, Gold):
            return (self.gold_mass == other.gold_mass and
                    self.total_mass == other.total_mass and
                    self.markup_add == other.markup_add)
        return False


# Do not remove this block.
# Doctest will not run otherwise and you won't get score.
if __name__ == "__main__":
    import doctest

    doctest.testmod()