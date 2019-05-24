from text_normalizer.text_normalizer import TextNormalizer, strip_emoji, remove_redundant_spaces, \
    remove_spaces_before_puncts, lowercase, yo_to_e, filter_symbols_only, filter_end_punctuation, filter_fit_limits, \
    add_spaces_after_puncts


class TestTextNormalizer:
    def setup(self):
        self.normalizer = TextNormalizer()

    def test_empty(self):
        text = ''
        norm = self.normalizer.normalize(text)
        assert norm == ''

    def test_emojis(self):
        text = '👍🔥👆🚀🛎👉🎁📣'
        norm = strip_emoji(text)
        assert norm == ''

    def test_add_spaces_after_puncts(self):
        text = 'This,is.a,text...This is, another text,it has no space after the comma. ott.com'
        norm = add_spaces_after_puncts(text)
        assert norm == 'This, is. a, text... This is, another text, it has no space after the comma. ott. com'

    def test_redundant_spaces(self):
        text = 'Hello     world! \t \t \n \n nice to meet you'
        norm = remove_redundant_spaces(text)
        assert norm == 'Hello world! nice to meet you'

    def test_spaces_before_puncts(self):
        text = 'Someone - placed , symbols , very . very ; very ? very ! bad '
        norm = remove_spaces_before_puncts(text)
        assert norm == 'Someone - placed, symbols, very. very; very? very! bad '

    def test_lowercase(self):
        text = 'SoMe TeXt'
        norm = lowercase(text)
        assert norm == 'some text'

    def test_yo_to_e(self):
        text = 'ёжик тщетно пытается съёжиться'
        norm = yo_to_e(text)
        assert norm == 'ежик тщетно пытается съежиться'

    def test_filter_symbols_only(self):
        text = ',.!@312'
        norm = filter_symbols_only(text)
        assert norm == ''

    def test_filter_end_punctuation(self):
        text = 'hello . , ; : /'
        norm = filter_end_punctuation(text)
        assert norm == 'hello'

    def test_filter_fit_limits(self):
        text = 'short_text'
        norm = filter_fit_limits(text)
        assert norm == ''

    def test_filter_fit_limits_2(self):
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
        ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum."""
        norm = filter_fit_limits(text)
        assert norm == text
