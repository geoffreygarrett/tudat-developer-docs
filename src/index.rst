Welcome
=======
.. epigraph::
    This documentation serves as a comprehensive guide for developers who
    aspire to contribute to the Tudat project. Whether you're setting up your
    development environment or diving into the intricacies of the codebase,
    this is your starting point.

Introduction
------------
Welcome, Developers! This platform is designed to equip you with all the
necessary information to contribute effectively to the Tudat project. It
includes guidelines for setting up your development environment, building the
Tudat project, and contributing code.

Getting Started
---------------
If you're new to Tudat or are setting up your development environment for the
first time, start here. This section provides a primer on the essential topics
you need to understand before you dive into the codebase.

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :caption: Getting Started
   :glob:

   getting-started/github.rst
   getting-started/conda.rst
   getting-started/devops.rst
   getting-started/azure.rst
   getting-started/*

How-to guides
-------------
For those looking for more advanced or specific information, the Guides section dives deeper into particular topics.
Whether you're trying to understand specific workflows or looking for best practices, this is the place for you.

.. toctree::
   :maxdepth: 3
   :titlesonly:
   :caption: How-to Guides
   :glob:

   how-to-guides/*

.. todo::
    - New ``tudat`` function, module, class

Explanation
-----------
The Explanation section provides in-depth understanding and context for key concepts and mechanisms. It aims to clarify
the 'why' behind various features and processes, offering a comprehensive background to help you grasp the underlying
principles and rationale.

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :caption: Explanation
   :glob:

   explanation/*

.. todo::
    - CI/CD pipeline and its components

Reference
---------
For an organized and detailed look at Tudat's codebase, the Reference section has you covered. It provides
comprehensive information about the classes, functions, and variables that make up the project.

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :caption: Reference
   :glob:

   reference/*

.. panels::
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    ---

    .. link-button:: Development Operations
          :type: ref
          :text: Development Operations
          :classes: btn-outline-primary btn-block

    ^^^

    :ref:`Code Collaboration`

    :ref:`Release versioning`

    :ref:`Package Management`

    :ref:`Continuous Deployment`

    ---

    .. link-button:: Software Documentation
          :type: ref
          :text: Software Documentation
          :classes: btn-outline-primary btn-block

    ^^^


    :ref:`Sphinx Documentation`

    :ref:`Release an online version`

    :ref:`Multidoc`

    :ref:`How to write docstrings`

    ---

    .. link-button:: Software Development
          :type: ref
          :text: Software Development
          :classes: btn-outline-primary btn-block

    ^^^

    :ref:`Build System`

    :ref:`Developer Environment`

    :ref:`Extending Features`

    :ref:`Exposing C++ to Python`
    
    :ref:`Exposing kernel modules directly through tudatpy`

    :ref:`Autocompletion in Python`

.. toctree::
   :maxdepth: 3
   :caption: Primer
   :hidden:

   primer/devops
   primer/docs
   primer/software
   primer/bib
