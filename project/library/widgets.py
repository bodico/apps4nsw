from math import ceil

from django import forms
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


class CheckboxSelectMultipleWithTwoDivs(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)
        output = []
        # Normalize to strings
        str_values = set([force_unicode(v) for v in value])
        #half = int(ceil(float((len(self.choices), len(self.choices))[len(self.choices) % 2 == 0]) / 2))
        half = int(ceil(len(self.choices) / 2.0))
        choice_groups = (
            (u'<div class="checkboxes-left"><ul>', list(self.choices)[:half]), 
            (u'<div class="checkboxes-right"><ul>', list(self.choices)[half:])
        )
        for (begin_markup, choice_group) in choice_groups:
            if (choice_group):
                output.append(begin_markup)
                for option_value, option_label in choice_group:
                    # If an ID attribute was given, add a numeric index as a suffix,
                    # so that the checkboxes don't all have the same ID attribute.
                    if has_id:
                        final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], option_value))
                        label_for = u' for="%s"' % final_attrs['id']
                    else:
                        label_for = ''

                    cb = forms.CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
                    option_value = force_unicode(option_value)
                    rendered_cb = cb.render(name, option_value)
                    option_label = conditional_escape(force_unicode(option_label))
            
                    output.append(u'<li><label%s>%s %s</label></li>' % (label_for, rendered_cb, option_label))
                output.append(u'</ul></div>')
        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        # See the comment for RadioSelect.id_for_label()
        if id_:
            id_ += '_0'
        return id_
    id_for_label = classmethod(id_for_label)