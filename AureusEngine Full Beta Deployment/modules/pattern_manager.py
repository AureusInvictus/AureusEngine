# pattern_manager.py

from collections import defaultdict, deque
from .constants import MIN_PATTERN_LENGTH, MAX_PATTERN_LENGTH, PATTERN_DECAY_RATE, PATTERN_MAX_AGE

class PatternManager:
    def __init__(self):
        self.pattern_store = defaultdict(lambda: {"count": 0, "last_seen": 0, "age": 0})

    def update_patterns(self, session_data):
        for length in range(MIN_PATTERN_LENGTH, min(MAX_PATTERN_LENGTH + 1, len(session_data))):
            for i in range(len(session_data) - length + 1):
                pattern = tuple(session_data[i:i+length])
                self.pattern_store[pattern]["count"] += 1
                self.pattern_store[pattern]["last_seen"] = len(session_data)
                self.pattern_store[pattern]["age"] = 0

        self.decay_patterns()

    def decay_patterns(self):
        for pattern in list(self.pattern_store):
            self.pattern_store[pattern]["age"] += 1
            self.pattern_store[pattern]["count"] *= PATTERN_DECAY_RATE
            if self.pattern_store[pattern]["age"] > PATTERN_MAX_AGE:
                del self.pattern_store[pattern]

    def get_common_patterns(self):
        sorted_patterns = sorted(self.pattern_store.items(), key=lambda x: -x[1]["count"])
        return [pat for pat, data in sorted_patterns if data["count"] > 1]