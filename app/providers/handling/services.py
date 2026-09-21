from dishka import Provider, Scope, provide_all

from app.application.services.access import AccessPolicy
from app.application.services.assessment_bank import AssessmentBank
from app.application.services.context import ConversationContextService
from app.application.services.cost import CostEstimator
from app.application.services.prompts import PromptBuilder


class ServicesProvider(Provider):
    scope = Scope.REQUEST

    services = provide_all(
        AccessPolicy,
        AssessmentBank,
        ConversationContextService,
        CostEstimator,
        PromptBuilder,
    )
