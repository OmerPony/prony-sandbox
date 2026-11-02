import stripe


def charge(amount: int) -> None:
    stripe.Charge.create(amount=amount)
