from .base import EnvSettings


class LimitsConfig(EnvSettings, env_prefix="LIMITS_"):
    # Daily quotas, 0 means unlimited
    free_daily_messages: int = 20
    free_daily_voice_messages: int = 3
    premium_daily_messages: int = 0
    premium_daily_voice_messages: int = 0
    max_voice_duration: int = 60
    max_input_length: int = 1000
    # Per-user throttling, seconds between requests
    throttle_rate: float = 1.0
    # Duplicate update protection window, seconds
    update_dedup_ttl: int = 300
