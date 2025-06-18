import logging
import re
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class PatternFilter(logging.Filter):
    def __init__(self, patterns):
        super().__init__()
        self.regexes = [self._wildcard_to_regex(p) for p in patterns]

    def _wildcard_to_regex(self, pattern: str):
        # Convert "{*}" to a regex wildcard
        escaped = re.escape(pattern)
        regex = escaped.replace(r'\{\*\}', '.*')
        return re.compile(f"^{regex}$")

    def filter(self, record):
        msg = str(record.getMessage())
        return not any(r.match(msg) for r in self.regexes)

class SuppressLogsPlugin(BasePlugin):
    config_scheme = (
        ('patterns', config_options.Type(list, default=[])),
        ('loggers', config_options.Type(list, default=["mkdocs.structure.pages"])),
    )

    def on_config(self, config):
        patterns = self.config.get('patterns', [])
        loggers = self.config.get('loggers', [])

        if not patterns:
            return config

        filter_instance = PatternFilter(patterns)
        for logger_name in loggers:
            logging.getLogger(logger_name).addFilter(filter_instance)

        return config