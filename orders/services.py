from typing import OrderedDict

from . import repos


class OrderServices:
    repos = repos.OrderRepos()

    def get_user_orders(self, user):
        if user.is_staff:
            return self.repos.get_orders()

        return self.repos.get_user_orders(user)

    def get_order(self, pk):
        return self.repos.get_order(pk=pk)
