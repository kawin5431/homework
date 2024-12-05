"""

01219114 Computer Programming
Week 10, Long Program Assignment: Mother Tux's Gold Shop (V2)
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

    Attributes (ALL MUST BE PRIVATE):
    name       -- the name of the piece of gold
                  <<GET, SET>> Must always be string
    gold_mass  -- the mass of gold in grams, initialize as 0
                  <<GET, SET>> Must always be int
    other_mass -- the mass of NON-GOLD in grams, initialize as 0
                  <<GET, SET>> Must always be int
    total_mass -- the total mass of the piece in grams, initialize as 0
                  <<GET>> Must always be int
    price      -- the price of the gold, assuming that we just call the
                  manual_price method directly. (Please note that the
                  manual_price method has been renamed from the original
                  assignment. This time, the name 'price' is used only for the
                  getter.) <<GET>> Must always provide int
    markup     -- how much to ADD to the value when attempting to sell in THB
                  default value for markup_add is 0.
                  <<GET, SET>> Must always be int
    purity     -- <<GET>>, use the method header already provided
                  This is often derived from existing values and can be float.

    Don't forget to implement type checks, raising TypeError when needed.
    The doctest is correct but incomplete.

    In this exercise (Week 10), you MUST implement @property getters and
    setters. This doctest will not fully test it, but the full pytest will.

    Also importantly, we will NOT add and remove gold using a special method
    anymore. Instead, we will change the amount of gold_mass and total_mass
    directly.

    >>> g = Gold()
    >>> g.markup_add = 100
    >>> g.markup_add
    100
    """

    def __init__(self,
                 name: str = "Gold",
                 markup: int = 0,
                 gold: int = 0,
                 other: int = 0):
        """
        Create a new piece of gold. Its name can be specified.
        If name is not given, then it is simply called "Gold".
        Do not change the case.

        TODO New init parameters introduced in V2:
        The amount of 'gold' is added immediately to the newly created
        Gold object. The amount of 'other' is also immediately added to
        the non-gold mass of the object.

        >>> Gold('a').name
        'a'
        >>> Gold().name
        'Gold'
        >>> Gold().gold_mass
        0
        >>> Gold().total_mass
        0
        >>> Gold().markup
        0
        >>> g = Gold(gold = 10, other = 20)
        >>> g.gold_mass, g.total_mass
        (10, 30)

        Don't implement any type or error checking here. Perform checks in the
        appropriate setters.
        """
        self.name = name
        self.markup = markup
        self._gold_mass = gold
        self._other_mass = other
        self._total_mass = self._gold_mass + self._other_mass

    @property
    def name(self) -> str:
        """return the name of the Gold"""
        return self._name

    @name.setter
    def name(self, value: str):
        # Check if the value is not a string
        if not isinstance(value, str):
            # Raise TypeError without a message to meet test requirements
            raise TypeError
        # Set the name if the value is valid
        self._name = value

    @property
    def gold_mass(self) -> int:  # getter (TODO implement setter)
        """
        Set the amount of gold in this piece. Cannot be lower than 0.
        Also, for sanity's sake, it must be integer.
        >>> g = Gold(gold=10, other=12)
        >>> g.gold_mass
        10
        >>> g.gold_mass = 11.1 # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError
        >>> g.gold_mass = -1 # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError
        """
        return self._gold_mass

    @gold_mass.setter
    def gold_mass(self, value: int):
        """Return the mass of gold."""
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self._gold_mass = value

    @property
    def other_mass(self) -> int:  # getter (TODO implement setter)
        """
        Set the amount of NON-GOLD content in this piece. Cannot be lower than
        0. Also, again, it must be integer.
        >>> g = Gold(gold=10, other=15)
        >>> g.other_mass
        15
        >>> g.other_mass = 20
        >>> g.other_mass
        20
        >>> g.other_mass = 11.1 # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError
        >>> g.other_mass = -1 # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError
        """
        return self._other_mass

    @other_mass.setter
    def other_mass(self, value: int):
        """Return the mass of other material."""
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self._other_mass = value

    @property
    def total_mass(self) -> int:
        """
        Returns the total mass of this gold piece based on:
        total_mass = gold_mass + other_mass
        """
        return self._gold_mass + self._other_mass

    @property
    def markup(self) -> int:
        """return the markup of the Gold"""
        return self._markup

    @markup.setter
    def markup(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Markup must be an integer.")
        if not 0 <= value:
            raise ValueError("Markup must be a non-negative integer.")
        self._markup = value

    @property
    def price(self):
        """
        This is a wrapper, meaning it simply calls a more complex method.

        This getter returns the price of the gold piece itself, assuming that
        it calls manual_price on itself. In actual world, this is not a good
        OOP practice. However, doing it the good way would require way more
        classes, so I'll let it slide this time.

        >>> g = Gold(gold=20, other=5)

        Works as if it's just manual_price, i.e. the property name is now a
        shorthand for calling the method without anything.
        >>> g.price == g.manual_price()
        True

        Does not work if per-gram price is changed.
        >>> g.price == g.manual_price(per_gram = 2001)
        False
        """
        return self.manual_price()

    def manual_price(self,
                     per_gram: int = 2000,
                     include_markup: bool = True,
                     force_purity: float = None) -> int:
        """
        Returns the appraised price of the gold artifact.
        Price is calculated per gram OF GOLD. If the price per gram is not
        given, force it to 2000 baht per gram.

        (Doctest Setup)
        >>> g = Gold(gold=10, other=10)
        >>> g.markup = 1000

        Normally it should be:
        (self.gold_mass * per_gram) + self.markup

        Of course, don't add self.markup_add if include_markup is False.

        >>> g.manual_price()
        21000
        >>> g.manual_price(3000)
        31000
        >>> g.manual_price(include_markup = False)
        20000
        >>> g.manual_price(3000, include_markup = False)
        30000

        However, if purity is forced (not None), the formula now uses:
        (force_purity * self.total_mass * per_gram) + self.markup

        >>> g.manual_price(2000, include_markup = True, force_purity = 1.00)
        41000
        >>> g.manual_price(2000, include_markup = True, force_purity = 0.75)
        31000

        Round price down to integer!

        Don't forget to raise ValueError when force_purity is outside the
        [0.00 to 1.00] range. You must also provide other type and value
        checking, raising TypeError or ValueError as appropriate.

        Do not include messages into the exceptions when you raise them.

        Forcing purity value is a way for us to sell gold at a profit, so
        don't forget to force purity value when told to.
        """
        if not isinstance(per_gram, int):
            raise TypeError

        # Check for type and value of force_purity
        if force_purity is not None:
            if not isinstance(force_purity, float):
                raise TypeError
            if not 0 <= force_purity <= 1:
                raise ValueError
            price = force_purity * self.total_mass * per_gram
        else:
            price = self.gold_mass * per_gram

        # Add markup if include_markup is True
        if include_markup:
            price += self.markup

        # Return the final price as an integer
        return int(price)

    @property
    def purity(self) -> float:
        """
        Return the purity of the gold piece.

        Pure gold should return a value of 1. For example, this one-gram piece
        of gold is completely pure.
        >>> g = Gold(gold=1, other=0)
        >>> g.purity
        1.0

        Of course, if we add one gram of non-gold material, its purity is
        reduced.
        >>> g = Gold(gold=1, other=1)
        >>> g.purity
        0.5

        Use the round builtin function to limit the number of digits to 4.
        In this case, now the gold piece has 1 g gold in 222 g total mass,
        making the purity only 0.0045.
        >>> g = Gold(gold=1, other=221)
        >>> g.purity
        0.0045

        If there is no total mass yet, then an error should be raised like
        this:
        >>> g = Gold()
        >>> g.purity # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ZeroDivisionError

        Do not include any message in the exception. Just raise it as is.
        (This is to help reduce the chaos when every single student somehow
        has their own flavor of exception message.)

        """
        if self.total_mass == 0:
            raise ZeroDivisionError
        return round(self._gold_mass / self.total_mass, 4)

    def __repr__(self):
        """
        The STRING REPRESENTATION of the gold piece must look like this:

        Gold: <self.name>, <self.gold_mass> g / <self.total_mass> g

        Do not display the brackets.

        >>> g = Gold("Test", gold=20, other=10)
        >>> g
        Gold: Test, 20 g / 30 g
        """
        return f"Gold: {self.name}, {self.gold_mass} g / {self.total_mass} g"

    def __eq__(self, other):
        """
        Two gold objects are considered equal only when:
        - The gold mass are equal
        - The other (non-gold) mass are equal
        - The markup amount (extra money to charge) are equal

        >>> g1 = Gold("Test 1", gold=10, other=20)
        >>> g2 = Gold("Test 2", gold=10, other=20)
        >>> g1 == g2
        True

        Equal purity does not mean equal.
        >>> g3 = Gold("Test 3", gold=20, other=40)
        >>> g2 == g3
        False

        Same name does not mean equal.
        >>> g4 = Gold("A", gold=0, other=1)
        >>> g5 = Gold("A", gold=1, other=1)
        >>> g4 == g5
        False
        """
        if not isinstance(other, Gold):
            return NotImplemented
        return (self._gold_mass == other._gold_mass and
                self._other_mass == other._other_mass and
                self._markup == other._markup)

    def __add__(self, other):
        """
        Two gold pieces can be added by combining their weights, both the
        gold and non-gold portions.

        Keep the name of the left-side of the operand.

        >>> g1 = Gold("A", gold=20, other=22)
        >>> g2 = Gold("B", gold=30, other=44)
        >>> (g1 + g2) == Gold("A", gold=50, other=66)
        True
        >>> (g2 + g1) == Gold("B", gold=50, other=66)
        True
        """
        if not isinstance(other, Gold):
            return NotImplemented
        return Gold(self.name, gold=self._gold_mass + other._gold_mass, other=self
                    ._other_mass + other._other_mass, markup=self._markup)


# Do not remove this block.
# Doctest will not run otherwise and you won't get score.
if __name__ == "__main__":
    import doctest

    doctest.testmod()