from dishka import Provider, Scope, provide_all

from app.presentation.telegram.flows.admin.panel import AdminFlow
from app.presentation.telegram.flows.common.lesson import LessonFlow
from app.presentation.telegram.flows.common.menu import CommonMenuFlow
from app.presentation.telegram.flows.common.onboarding import OnboardingFlow
from app.presentation.telegram.flows.common.practice import PracticeFlow
from app.presentation.telegram.flows.common.profile import ProfileFlow
from app.presentation.telegram.flows.common.progress import ProgressFlow
from app.presentation.telegram.flows.common.subscription import SubscriptionFlow
from app.presentation.telegram.flows.common.vocabulary import VocabularyFlow
from app.presentation.telegram.flows.extra.errors import ExtraErrorsFlow
from app.presentation.telegram.flows.extra.pm import PMFlow


class FlowsProvider(Provider):
    scope = Scope.REQUEST

    flows = provide_all(
        AdminFlow,
        CommonMenuFlow,
        ExtraErrorsFlow,
        LessonFlow,
        OnboardingFlow,
        PMFlow,
        PracticeFlow,
        ProfileFlow,
        ProgressFlow,
        SubscriptionFlow,
        VocabularyFlow,
    )
