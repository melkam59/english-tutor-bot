from dishka import Provider, Scope, provide_all

from app.application.interactors.admin.broadcast import BroadcastInteractor
from app.application.interactors.admin.stats import AdminStatsInteractor
from app.application.interactors.admin.users import AdminUsersInteractor
from app.application.interactors.assessment.level_assessment import LevelAssessmentInteractor
from app.application.interactors.lessons.personalized import LessonsInteractor
from app.application.interactors.limits.usage import UsageLimitsInteractor
from app.application.interactors.onboarding.profile import ProfileInteractor
from app.application.interactors.pm.user_status import PMInteractor
from app.application.interactors.progress.summary import ProgressInteractor
from app.application.interactors.subscription.manage import SubscriptionInteractor
from app.application.interactors.tutor.conversation import TutorConversationInteractor
from app.application.interactors.vocabulary.trainer import VocabularyInteractor
from app.application.interactors.voice.transcription import VoiceInteractor


class InteractorsProvider(Provider):
    scope = Scope.REQUEST

    interactors = provide_all(
        AdminStatsInteractor,
        AdminUsersInteractor,
        BroadcastInteractor,
        LessonsInteractor,
        LevelAssessmentInteractor,
        PMInteractor,
        ProfileInteractor,
        ProgressInteractor,
        SubscriptionInteractor,
        TutorConversationInteractor,
        UsageLimitsInteractor,
        VocabularyInteractor,
        VoiceInteractor,
    )
