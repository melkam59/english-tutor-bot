from app.application.models.state.base import StateModel


class AssessmentState(StateModel):
    question_index: int = 0
    # question id -> selected option index or written answer
    answers: dict[int, int | str] = {}
