from dishka import AsyncContainer


async def send_vocabulary_reminders(container: AsyncContainer) -> None:
    # TODO(M3): VocabularyGateway.get_user_ids_with_due_items -> Broadcaster.send("time to revise")
    #  Repositories are REQUEST scoped: ``async with container() as request_container``.
    #  The ``User`` dependency is resolved from a Telegram update, so worker tasks must only
    #  use gateways / services, never user-bound interactors.
    raise NotImplementedError
