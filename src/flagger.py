
SCAM_PHRASES = [     # List of lowercase scammy phrases to match against
    "click here",
    "verify your account",
    "urgent action required",
    "free gift",
    "limited time offer",
    "your account has been suspended",
    "act now",
    "confirm your identity",
    "win big",
    "exclusive deal"
]


def flag_keywords(text: str) -> list[str]: # Takes email text
    """
    Scans the input text for known scam phrases.
    Returns a list of matched phrases.
    """
    text_lower = text.lower()     # Converts input text to lowercase for case-sensitive
    return [phrase for phrase in SCAM_PHRASES if phrase in text_lower]