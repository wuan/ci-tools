`ci-tools <https://github.com/wuan/ci-tools>`_
==============================================

.. image:: https://badge.fury.io/py/citools.png
    :alt: PyPi-Package
    :target: https://badge.fury.io/py/citools
.. image:: https://travis-ci.org/wuan/ci-tools.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/wuan/ci-tools
.. image:: https://coveralls.io/repos/wuan/ci-tools/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/wuan/ci-tools?branch=master 

prototype tool collection for continuous integration of Java projects with lots of modules

Examples
========

collect/accumulate test results of another job
----------------------------------------------

Example::

    update_job_state master-unittests master-integrationtests

This will create local databases ``master-unittests.db`` and ``master-integrationtests.db``  containing all test results of the given job names ``master-unittests`` and ``master-integrationtests``. Newer Suites overwrite older ones. Full tests runs overwrite all results.

merge test results of job database
----------------------------------

Example::

    merge_job_state master-unittests master-integrationtests master

Creates a local database ``master.db`` containing the merged test results of the local databases ``master-unittests.db`` and ``master-integrationtests.db``.

create junit result from database
---------------------------------

Example::

    export_job_state master

Creates a JUnit XML file containing the current test state from the ``master.db`` persistence file.