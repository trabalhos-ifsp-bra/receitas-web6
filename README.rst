receitas
========

Projeto Web s6 IFSP

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

receitas
========

Learning Django Framework and Python syntax.

Checklist
---------

-  [X] Adicionar receitas – os usuários poderão publicar suas receitas
   no site
-  [X] Comentar – os usuários poderão adicionar comentários nas receitas
   publicadas por terceiros.
-  [X] Avaliações – os usuários poderão avaliar as receitas de terceiros
   por meio de estrelas.
-  [X] Adicionar imagem – os usuários poderão publicar imagem das suas
   receitas e nos comentários.
-  [X] Editar receitas – os usuários poderão editar receitas (somente as
   próprias).
-  [X] Excluir receitas – os usuários poderão excluir receitas
   publicadas (somente as próprias).
-  [X] Categorização – separação de receitas por categorias. Ex:
   salgados, doces, assados, fritos, vegetariano.
-  [ ] Favoritos – os usuários poderão ‘favoritar’ as receitas para
   serem guardadas.
-  [X] Responsividade – poderá ser aberto em qualquer dispositivo, sem
   problemas de resolução.
-  [ ] Impressão – os usuários poderão imprimir as receitas.



Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy receitas

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.




