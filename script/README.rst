.. _readme_templates:

Generate README file templates for metadata
===========================================

One of the simplest way to describe your data is to use README files.
In order to follow the same conventions and file organization 
at LCBC, we have created a script called :py:mod:`create_metadata.py`.

This script can be used to generate templates for metadata README files.
Once a template has been generated, you can just fill in the missing 
information and update it as your data is changing.

General structure
-----------------

The :py:mod:`create_metadata.py` can be used to generate different metadata
README file templates. Each type of template is categorized via an attribute
:py:attr:`mtype`, which stands for "metadata type". So far we have the following types:

* ``main``

* ``calculation``

.. note::

    * If you feel that another type of template should be added to the list.
    * Or that something should be modified in the template.
    * If you consistently modify the resulting template because you miss a
      section or something else.
    * ...

    Make us all benefit from your modification by :ref:`updating the script <modify_script>` (or by
    asking someone else to do it).


The data structure we recommend is to have a folder for each project.
The name of the folder should reflect the project (e.g. ``2D_halide_perovskites``).
Inside each project folder you should have a ``main`` metadata README file.
This file should give a general overview of the data organization and naming
conventions that you will be using for the project. On top of that we recommend
to put other information like a project description, the list of collaborators,
the general workflow...

Inside every project folder there will be subfolders containing data (most
probably coming from computer simulations). Inside each subfolder you should
include a README file to describe the content of the folder. If the folder
contains data from computer simulations (input coordinates, output files,
restart files...) we recommend to use the ``calculation`` metadata type when
generating the README file template.

We have tried not to be too restrictive in the naming conventions and folder
structure such that it requires minimal amount of work to document your data.
The only important thing is that your metadata should explain clearly and in
details how you have chosen to organize your data. We hope that the templates
produced by the :py:mod:`create_metadata.py` can help you doing that.

Using the script
----------------

At the moment, to use the :py:mod:`create_metadata.py` script on the LCBC cluster,
you should add the following line to your ``.bashrc``::

    PATH=$PATH:/home/pbaudin/Work/data_management/script/

Alternatively you can follow the :ref:`installation procedure <install>` below.
Once the script is available, just execute it as::

    $ create_metadata.py
    
      CREATING NEW README FILE METADATA TEMPLATE
      ==========================================
    
    Please fill in the following mandatory information:
    Metadada type (main, calculation): main
    Name for the README file? [README.rst]:
    Subject (perovskites, biochemistry, photochemistry, methods, ...): photochemistry
    Project title: My awesome project to save the world
    Author: Marie Curie
    Email [marie.curie@epfl.ch]:
    
    The README.rst file has been created sucessfully!
    Open it and fill in the missing information.
    Continue to update it until the end of your project.
    
Let us take a look at what happened.

#. After calling the script we are told that a new template will be created and
   that we have to give some mandatory information.

#. **Metadada type:** This is the most important information as it will decide
   which template to create. For now there are only two possible choices, ``main``
   or ``calculation``. 

#. **README filename:** The default filename for the template is ``README.rst`` by
   pressing enter directly we choose the default in brackets. It is however
   recommended to choose a more meaningful and descriptive filename.

#. **Subject:** Here a list of subjects is given for convenience. You can add
   your own or select several subjects.

#. **Project title:** Just insert the title of your project.

#. **Author:** Put your first name and then your family name (in that order since it
   will be used to generate the default email address).

#. **Email:** If the suggested email address is correct just press
   enter. Otherwise enter the correct email.

#. Finally we are told that the template has been created and that we can start
   editing it.


By default the template file has a ``.rst`` extension which stands for
``reStructuredText``. It is a plaintext markup language that can be interpreted
to render documents (html, latex...). We encourage you to use this format but
of course you are free to use just plaintext ``.txt`` or markdown ``.md`` but
please avoid using proprietary formats such as ``.docx``.

If you want to know more about the ``reStructuredText`` format, we recommend
the following documentation:

* http://www.sphinx-doc.org/en/stable/usage/restructuredtext/index.html

* http://docutils.sourceforge.net/docs/ref/rst/introduction.html


Adding a .config_metadata file
------------------------------

Most of the information required by the :py:mod:`create_metadata.py` script
will always be the same, at least for a given project.

To avoid filling in all fields every time you can add a ``.config_metadata`` 
file in your home directory which contain the relevant information::

    # Configuration file for create_metadata.py
    # mtype = main
    filename = README_FOR_MY_PROJECT.rst
    subject = perovskites
    title = My awesome project to save the world
    author = Albert Einstein
    email = albert.einstein@epfl.ch

If one of the field is missing in the config file or if it is commented out with a ``#``.
You will be prompted to enter this field during the execution of the script.

.. danger::

    You can only comment out a whole line by starting with ``#``.
    If you write the following::
        
        author = Max Planck # This is my name and I am a smart guy!

    The script will not see the comment and take the author name to be
    everything after the equal sign...

A config file can also be passed as an argument during the execution of the script.
For example::

	$ create_metadata.py -c /path/to/my/config_metadata

This option has priority over the main config file in ``~/.config_metadata``.
If you are lucky you may get more information by typing::

	$ create_metadata.py -h


.. _install:

How to install the script
-------------------------

If you want to use the :py:mod:`create_metadata.py` script on your own laptop
or somewhere else than the LCBC cluster, you can get it from our github
data_management repository.

#. Install git if it is not already done.

#. Got to the place where you want to store the script and run::

        git clone https://github.com/lcbc-epfl/data_management

#. Assuming you were in your home directory, the script is now in 
   ``~/data_management/script/create_metadata.py``.
   The README templates are also in the script directory.

#. You can then add the script to your path, e.g. in your ``.bashrc`` file::

        PATH=$PATH:~/data_management/script/


.. _modify_script:

How to improve/modify the script
--------------------------------

.. todo::

    This section needs to be written...
    But basicaly: clone the data_management repository from the github account
    and push your changes.
    If you have troubles with git or understanding the script contact me
    (pablo: pablo.baudin@epfl.ch).

.. automodule:: create_metadata

