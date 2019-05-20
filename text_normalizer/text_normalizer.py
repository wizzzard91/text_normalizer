import logging
import re


class Rule:
    def __init__(self):
        self.logger = logging.getLogger('seo_terminal.' + __name__ + '.rule')


# http://stackoverflow.com/a/13752628/6762004
RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

RE_SPACES_BEFORE_PUNCTS = re.compile(r'\s([?,.;:!"](?:\s|$))')
RE_END_PUNCTUATION = re.compile(r'\s([ .,;:/]*$)')


def strip_emoji(s: str) -> str:
    return RE_EMOJI.sub(str(), s)


def remove_redundant_spaces(s: str) -> str:
    return ' '.join(s.split())  # works with both tabs and spaces


def remove_spaces_before_puncts(s: str) -> str:
    return RE_SPACES_BEFORE_PUNCTS.sub(r'\1', s)


def lowercase(s: str) -> str:
    return s.lower()


def yo_to_e(s: str) -> str:
    return s.replace('ё', 'е')


def filter_symbols_only(s: str) -> str:
    return s if any(char.isalpha() for char in s) else ''


def filter_short(s: str) -> str:
    return s if len(s) >= 2 else ''


def filter_end_punctuation(s: str) -> str:
    return RE_END_PUNCTUATION.sub('', s)


class TextNormalizer:
    """
    Normalizes text based on provided rules.
    """

    def __init__(self, logger=None):
        """
        :param logger: logger for logging
        """
        self.logger = logger or logging.getLogger('seo_terminal.' + __name__)

        self._rules = [strip_emoji, remove_redundant_spaces, remove_spaces_before_puncts, lowercase, yo_to_e,
                       filter_symbols_only, filter_short]

    def normalize(self, text: str) -> str:
        """
        Normalizes text.
        :param text: unnormalized text
        :return: normalized text (string)
        """
        try:
            new_text = str(text)
            for rule in self._rules:
                new_text = rule(new_text)
            return new_text
        except Exception as e:
            self.logger.error("Exception {0} args {1}".format(type(e).__name__, str(e.args)))
            return ''
