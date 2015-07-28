ci-tools
========

.. image:: https://badge.fury.io/py/citools.png :alt: PyPi-Package :target: https://badge.fury.io/py/citools.png
.. image:: https://travis-ci.org/wuan/ci-tools.svg :alt: Build Status :target: https://travis-ci.org/wuan/ci-tools

prototype tool collection for continuous integration of Java projects with lots of modules

Examples
========

collect/accumulate test results of another job
----------------------------------------------

Example::

    update_job_state master-unittests master-integrationtests

This will create a local database `master-unittests.db` containing all test results. Newer Suites overwrite older ones. Full tests runs overwrite all results.

merge test results of job database
----------------------------------

Example::

    merge_job_state master-unittests master-integrationtests master

create junit result from database
---------------------------------

    export_job_state master

