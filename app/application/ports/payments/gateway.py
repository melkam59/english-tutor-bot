from typing import Protocol


class PaymentsGateway(Protocol):
    """
    Placeholder for a real payment provider (Telegram Stars, Stripe, ...).
    The MVP only flips the subscription status, see ``SubscriptionInteractor``.
    """

    async def create_invoice_link(self, user_id: int, months: int) -> str: ...
