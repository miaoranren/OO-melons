"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, country_code = None):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code                


    def get_total(self):
        """Calculate price, including tax."""
        fee = 0
        base_price = 5
        if self.species == "Christmas melons":
            base_price = 1.5 * base_price

            if self.order_type == "international":
                if self.qty < 10:
                    fee = 3


        total = ((1 + self.tax) * self.qty * base_price) + fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
            
    order_type = "international"
    tax = 0.17


class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = "government"
    tax = 0.0
    def __init__(self,species,qty):
        super().__init__(species,qty)
        self.passed_inspection = False


    def mark_inspection(self, passed):
        # if self.passed == T:
        #     passed_inspection = True
        self.passed_inspection = passed
         
