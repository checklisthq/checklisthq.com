from django import forms

INITIAL_TEXT = """= Heading =

This is some text. Use it to explain things and give guidance.

Text can be on multiple lines (like this). When it's turned into a web-form each will be a separate paragraph.

[] This is a single item in a checklist.
[] This is another item in the checklist.
[] {doctor, nurse} This is a special item since it also contains an indication of what roles are associated with it.

// This is a comment for other checklist authors. Use it to explain things; for example, adding a line break is easy with three or more dashes, just like this:

---

Regular items in the checklist that start with square brackets are great, but sometimes you need to limit the options available. Use items that start with parenthesis to achieve this:

() This is an item in a selection group.
() You may only choose one item in this group.
() The group continues until you stop using the "()" at the beginning of items.

Because of this text, the next selection-group is separate from the one above:

() Item 1
() Item 2
() {doctor} Item 3

That's it! Experiment and play!

// Click on the submit button below to see this checklist rendered as a web-form.
// Click the "Back" button on the rendered form to return here.

All feedback most welcome... ;-)"""

class DSLForm(forms.Form):
    """
    A form for entering the specification of a checklist.
    """
    specification = forms.CharField(
        label='',
        initial=INITIAL_TEXT,
        widget=forms.Textarea(attrs={
        'class': 'input-xlarge',
        'style': 'width: 100%',
        'rows': 28})
    )
