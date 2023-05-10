
from . import repos


class OrderServices:
    repos = repos.OrderRepos()

    def get_orders(self):
        return self.repos.get_orders()
