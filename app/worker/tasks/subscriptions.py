from dishka import AsyncContainer


async def expire_subscriptions(container: AsyncContainer) -> None:
    # TODO(M4): downgrade users whose subscription_expires_at is in the past and notify them
    raise NotImplementedError
