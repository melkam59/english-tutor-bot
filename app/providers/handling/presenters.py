from dishka import Provider, Scope, provide_all

from app.presentation.telegram.presenters.admin.panel import AdminPresenter
from app.presentation.telegram.presenters.common.lesson import LessonPresenter
from app.presentation.telegram.presenters.common.menu import CommonMenuPresenter
from app.presentation.telegram.presenters.common.onboarding import OnboardingPresenter
from app.presentation.telegram.presenters.common.practice import PracticePresenter
from app.presentation.telegram.presenters.common.profile import ProfilePresenter
from app.presentation.telegram.presenters.common.progress import ProgressPresenter
from app.presentation.telegram.presenters.common.subscription import SubscriptionPresenter
from app.presentation.telegram.presenters.common.vocabulary import VocabularyPresenter
from app.presentation.telegram.presenters.extra.errors import ExtraErrorsPresenter


class PresentersProvider(Provider):
    scope = Scope.REQUEST

    presenters = provide_all(
        AdminPresenter,
        CommonMenuPresenter,
        ExtraErrorsPresenter,
        LessonPresenter,
        OnboardingPresenter,
        PracticePresenter,
        ProfilePresenter,
        ProgressPresenter,
        SubscriptionPresenter,
        VocabularyPresenter,
    )
