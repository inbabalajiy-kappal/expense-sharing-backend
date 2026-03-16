class EqualSplitStrategy:

    def split(self, amount, participants):
        count = len(participants)
        share = amount / count

        result = {}

        for user in participants:
            result[user] = share

        return result