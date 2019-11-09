"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_total(self):
        base_price = 5
        if self.species == 'christmas':
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total += 3
        return total 


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0

    def __init__(self, species, qty, country_code=None):
        super().__init__(species, qty, country_code)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        if passed is True:
            passed_inspection = True
        return passed_inspection
