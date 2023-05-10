from . import models


class OrderRepos:
    model = models.Order

    def get_orders(self):
        return self.model.objects.all()
