from django.forms import widgets


class SemanticSelect(widgets.Select):
    def __init__(self, attrs=None, choices=()):
        super(SemanticSelect, self).__init__(attrs=attrs, choices=choices)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'ui dropdown semantic-dropdown'


class SemanticSearchSelect(widgets.Select):
    def __init__(self, attrs=None, choices=()):
        super(SemanticSearchSelect, self).__init__(attrs=attrs, choices=choices)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'ui search dropdown semantic-dropdown'


class SemanticSelectMultiple(widgets.SelectMultiple):
    def __init__(self, attrs=None, choices=()):
        super(SemanticSelectMultiple, self).__init__(attrs, choices)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'ui dropdown semantic-dropdown'


class SemanticSearchSelectMultiple(widgets.SelectMultiple):
    def __init__(self, attrs=None, choices=()):
        super(SemanticSearchSelectMultiple, self).__init__(attrs, choices)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'ui search dropdown semantic-dropdown'
