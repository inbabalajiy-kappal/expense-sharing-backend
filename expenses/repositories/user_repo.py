from expenses.models import User


class UserRepository:

    def get_by_id(self, user_id):

        return User.objects.get(id=user_id)

    def get_many_by_ids(self, user_ids):

        return list(User.objects.filter(id__in=user_ids))
