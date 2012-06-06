checklisthq.com
===============

A simple website for checklists.

All code is covered by the Gnu Affero GPL v.3 (see the LICENSE file for
a copy).

A list of authors is in the AUTHORS file.

Planned by Wai Keong and Nicholas.

Created in 48 hours at NHSHackday 2012.

Quick start
-----------

How to run checklistHQ locally

1. clone the repository: ``git clone git://github.com/checklisthq/checklisthq.com.git``
2. install the requirements (use of ``virtualenv`` is advised): ``pip install -r requirements.txt``
3. create the local SQLite databases: ``./checklisthq/manage.py syncdb``
4. run the server locally on ``localhost:8000``: ``./checklisthq/manage.py runserver``
5. start making modifications to the code
