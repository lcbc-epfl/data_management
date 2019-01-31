#!/usr/bin/env python

import datetime

# ADD POSSIBLE README FILE TYPES HERE
allowed_types = ['main', 'calculation']

# ADD POSSIBLE SUBJECTS HERE
allowed_subjects = ['perovskites', 'biochemistry', 'photochemistry', 'methods']

class header(object):
    """This class is used to control the main information regarding the README file."""

    def __init__(self):
        self.date = datetime.datetime.now()
        self.filename = "README.rst"
        self.type = None
        self.subject = None
        self.title = None
        self.author = None
        self.email = None

    def __repr__(self):
        """Output formating of the class."""
        head  = "| **Creation date:**  {} \n".format( self.date.strftime("%Y-%m-%d") )
        head += "| **Metadata type:**  {} \n".format( self.type )
        head += "| **Subject:**        {} \n".format( self.subject )
        head += "| **Project title:**  {} \n".format( self.title )
        head += "| **Author:**         {} \n".format( self.author )
        head += "| **Email:**          {} \n".format( self.email )
        return head

    def output(self):
        return self.__repr__()

    def read(self):
        """Read the input information from the user."""

        print("\n  CREATING NEW README FILE METADATA TEMPLATE")
        print("  ==========================================\n")
        print("Please fill in the following mandatory information:")

        inp = input("Metadada type ({}): ".format( ', '.join( allowed_types ) ) )
        if inp not in allowed_types:
            sys.exit("ERROR: Metadata type not allowed!")
        else:
            self.type = inp.capitalize()

        inp = input("Subject ({}, ...): ".format( ', '.join( allowed_subjects ) ) )
        self.subject = inp.title()

        self.title = input("Project title: ").title()
        self.author = input("Author: ").title()
        self.email = input("Email: ").lower()
        inp = input("Name for the README file? [README.rst]: ")
        if inp is not '':
            self.filename = inp


main_template = """
GENERAL INFORMATION
===================

* **Title:** {}

* **Author information:**

  * {}
  * Institution:
  * Email: {}

* **Collaborators:**

  * Name 1
        * Institution:
        * Email:

  * Name 2
        * Institution:
        * Email:

* **Project status and dates:**

  * Started: {}
  * Finished:
  * Published:

* **Project description:**

    Bla bla...


SHARING/ACCESS INFORMATION
==========================

* Recommended citation for the data:

* Links to publications that cite or use the data:

* Licenses/restrictions placed on the data:

* Other important links:


DATA & FILE OVERVIEW
====================

*List all relevant files and subfolders.*

* Name:
* Short Description:

      Bla bla...

* Name:
* Short Description:

      Other bla bla...


METHODOLOGY AND WORKFLOW
========================

*Describe the overall methods and workflow of the project*

"""

calculation_template="""
GENERAL DESCRIPTION
===================

Bla bla...

SOFTWARE INFORMATION
====================

*List all software used. Where can it be accessed? Which version? How was it compiled?*

HARDWARE INFORMATION
====================

*On which computer, cluster... did you run the calculation, which characteristics does it have?*

DATA & FILE OVERVIEW
====================

*List all relevant files and subfolders.*

* Name:
* Short Description:

      Bla bla...

* Name:
* Short Description:

      Other bla bla...

WORKFLOW
========

METHODOLOGY AND WORKFLOW
========================

*Describe methods and workflow you follow in details*

"""

# Read mandatory information for the header of the README file
myhead = header()
myhead.read()

# Create README file based on input info
with open(myhead.filename,"w") as readme:
    readme.write( myhead.output() )
    if myhead.type == "Main":
        readme.write( main_template.format( myhead.title,
                                          myhead.author,
                                          myhead.email,
                                          myhead.date.strftime("%Y-%m-%d"),
                                          ))
    else:
        readme.write( calculation_template )

print("\nThe {} file has been created sucessfully!".format(myhead.filename) )
print("Open it and fill in the missing information.")
print("Continue to update it until the end of your project.")
