django-humanity: PROVE YOU ARE HUMAN!
=====================================

The robots are trying to take over the world. Ensure that your forms
are used only by humans.

Usage
-----

Create your form as a subclass of HumanityForm::

    from humanity.forms import HumanityForm

    class MyForm(HumanityForm):
        pass

That's it! Just include the form in your template and everything will be
handled for you.
