from django import forms

INITIAL_TEXT = """= WHO SURGICAL CHECKLIST: 1ST EDITION =

---
// Checklist DSL version - an example checklist with annotations.
// Created by Wai Keong Wong, updated by Nicholas H.Tollervey
// Date: 25/04/2012
// Version 1.1

// This is a comment because it starts with two slash characters. It won't be rendered on the web-form.

// Placing text between equals characters makes it a heading. Use more equals characters to make the heading smaller.

== SIGN IN ==

// Text on its own becomes a paragraph:

PATIENT HAS CONFIRMED

// Items in the checklist start with empty square brackets making them look like a checkbox.

[] IDENTITY
[] SITE
[] PROCEDURE
[] CONSENT

// Different sections of the checklist are delineated with three or more minus signs rendered as a horizontal line:

---

[] SITE MARKED/NOT APPLICABLE

---

[] ANAESTHESIA SAFETY CHECK COMPLETED

---

[] PULSE OXIMETER ON PATIENT AND FUNCTIONING

---

=== DOES PATIENT HAVE ===

// Items that start with empty parenthesis belong to a checklist group.
// Only one item in the checklist group can be selected.

A KNOWN ALLERGY?
() NO
() YES

---

DIFFICULT AIRWAY/ASPIRATION RISK?
() NO
() YES, AND EQUIPMENT/ASSISTANCE AVAILABLE

---

RISK OF >500ML BLOOD LOSS (7ML/KG IN CHILDREN)?
() NO
() YES, AND ADEQUATE INTRAVENOUS ACCESS AND FLUIDS PLANNED

---

== TIME OUT ==

[] CONFIRM ALL TEAM MEMBERS HAVE INTRODUCED THEMSELVES BY NAME AND ROLE

---

SURGEON, ANAESTHESIA PROFESSIONAL AND NURSE VERBALLY CONFIRM

// Roles associated with specific items are listed at the start of the item within curly brackets like this:

[] {SURGEON, ANAESTHESIST, NURSE} PATIENT
[] {SURGEON, ANAESTHESIST, NURSE} SITE
[] {SURGEON, ANAESTHESIST, NURSE} PROCEDURE

---

ANTICIPATED CRITICAL EVENTS

// Use [...] to make an item into a text box for users to add comments and other textual information.

[...] {SURGEON} WHAT ARE THE CRITICAL OR UNEXPECTED STEPS, OPERATIVE DURATION, ANTICIPATED BLOOD LOSS?
[...] {ANAESTHESIST} ARE THERE ANY PATIENT-SPECIFIC CONCERNS?
[...] {NURSE} HAS STERILITY (INCLUDING INDICATOR RESULTS) BEEN CONFIRMED?
[...] {NURSE} ARE THERE EQUIPMENT ISSUES OR ANY CONCERNS?

---

HAS ANTIBIOTIC PROPHYLAXIS BEEN GIVEN WITHIN THE LAST 60 MINUTES?
() YES
() NOT APPLICABLE

---

IS ESSENTIAL IMAGING DISPLAYED?
() YES
() NOT APPLICABLE

---

== SIGN OUT ==

NURSE VERBALLY CONFIRMS WITH THE TEAM
[] {NURSE} THE NAME OF THE PROCEDURE RECORDED
[] {NURSE} THAT INSTRUMENT, SPONGE AND NEEDLE COUNTS ARE CORRECT (OR NOT APPLICABLE)
[] {NURSE} HOW THE SPECIMEN IS LABELLED (INCLUDING PATIENT NAME)
[] {NURSE} WHETHER THERE ARE ANY EQUIPMENT PROBLEMS TO BE ADDRESSED

---

[...] {SURGEON, ANAESTHESIST, NURSE} REVIEW THE KEY CONCERNS FOR RECOVERY AND MANAGEMENT OF THIS PATIENT

// Click the "Submit" button below to see this checklist rendered as a web form.
// Experiment and play! All feedback most welcome."""

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
        'rows': 32})
    )
