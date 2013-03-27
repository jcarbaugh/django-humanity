django-humanity: PROVE YOU ARE HUMAN!
=====================================

The robots are trying to take over the world. Ensure that your forms
are used only by humans.

django-humanity adds a simple mathematical equation to your form that users
must solve in order to submit. Computers are notoriously terrible at math,
so this is a task that only humans (or maybe dolphins) can accomplish.

Usage
-----

Create your form as a subclass of HumanityForm::

    from humanity.forms import HumanityForm

    class MyForm(HumanityForm):
        pass

That's it! Just include the form in your template and everything will be
handled for you.
