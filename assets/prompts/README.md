# Prompt templates

Loaded by `app/application/services/prompts.py` (`PromptBuilder`).
Keeping prompts as files makes them reviewable and editable without code changes.

| File | Used for | Milestone |
|------|----------|-----------|
| `tutor_system.md` | Conversation mode system prompt (level, native language, goal, mode, recent mistakes, summary) | M2 |
| `summary.md` | Rolling conversation summarization | M2 |
| `lesson.md` | Personalized lesson generation | M3 |
| `lesson_feedback.md` | Feedback on the lesson exercise | M3 |
| `vocabulary_card.md` | Translation + example for a saved phrase | M3 |
| `assessment_writing.md` | CEFR grading of the short written answer | M3 |
