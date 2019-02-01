#!/usr/bin/env python
"""Generate a README file for metadata based on some input information."""

import os
import datetime

# ADD POSSIBLE README FILE TYPES HERE
allowed_types = ['main', 'calculation']

# ADD POSSIBLE SUBJECTS HERE
allowed_subjects = ['perovskites', 'biochemistry', 'photochemistry', 'methods']

class metadata(object):
    """This class is used to control the main information regarding a metadata README file."""

    def __init__(self, filename=None):

        print("\n  CREATING NEW README FILE METADATA TEMPLATE")
        print("  ==========================================\n")

        if filename:
            self.__read_file(filename)

        else:
            # ask user for input through setters
            print("Please fill in the following mandatory information:")
            self.mtype = None
            self.filename = None
            self.subject = None
            self.title = None
            self.author = None
            self.email = None


    # --- CREATION DATE ---
    @property
    def date(self):
        # export formated date
        return datetime.datetime.now().strftime("%Y-%m-%d")


    # --- METADATA TYPE ---
    @property
    def mtype(self):
        return self.__mtype.capitalize()

    @mtype.setter
    def mtype(self, mtype):
        if not mtype:
            mtype = input("Metadada type ({}): ".format( ', '.join( allowed_types ) ) )

        # make sure mtype is part of allowed types
        assert mtype.lower() in allowed_types, "Metadata type not allowed!"
        self.__mtype = mtype


    # --- README FILENAME ---
    @property
    def filename(self):
            return self.__filename

    @filename.setter
    def filename(self, filename):
        if not filename:
            filename = input("Name for the README file? [README.rst]: ")
            # make sure filename is a non-empty string
            if filename=='':
                filename = "README.rst"
        self.__filename = filename


    # --- SUBJECT ---
    @property
    def subject(self):
            return self.__subject.title()

    @subject.setter
    def subject(self, subject):
        if not subject:
            subject = input("Subject ({}, ...): ".format( ', '.join( allowed_subjects ) ) )

        self.__subject = subject


    # --- TITLE ---
    @property
    def title(self):
            return self.__title.title()

    @title.setter
    def title(self, title):
        if not title:
            title = input("Project title: ")

        self.__title = title


    # --- AUTHOR ---
    @property
    def author(self):
            return self.__author.title()

    @author.setter
    def author(self, author):
        if not author:
            author = input("Author: ")

        self.__author = author


    # --- EMAIL ---
    @property
    def email(self):
            return self.__email.lower()

    @property
    def __guess_email(self):
        firstname = self.author.lower().split()[0]
        surname = self.author.lower().split()[-1]
        return "{}.{}@epfl.ch".format( firstname, surname )

    @email.setter
    def email(self, email):
        if not email:
            guess = self.__guess_email
            email = input("Email [{}]: ".format( guess ) )
            if email=='':
                email = guess
        self.__email = email


    def __str__(self):
        """Generate a formatted header of the mandatory information."""
        head =  "| **Creation date:**  {} \n".format( self.date )
        head += "| **Metadata type:**  {} \n".format( self.mtype )
        head += "| **Subject:**        {} \n".format( self.subject )
        head += "| **Project title:**  {} \n".format( self.title )
        head += "| **Author:**         {} \n".format( self.author )
        head += "| **Email:**          {} \n".format( self.email )
        head += "\n\n"
        return head


    def __read_file(self, filename):
        """Parse input file to get headers elements."""

        read_type = False
        read_filename = False
        read_subject = False
        read_title = False
        read_author = False
        read_email = False

        with open(filename,"r") as inp:
            for line in inp:
                l = [x.strip() for x in line.lower().split('=')]
                if "type" in l:
                    self.mtype = l[-1]
                    read_type = True
                if "filename" in l:
                    self.filename = l[-1]
                    read_filename = True
                if "subject" in l:
                    self.subject = l[-1]
                    read_subject = True
                if "title" in l:
                    self.title = l[-1]
                    read_title = True
                if "author" in l:
                    self.author = l[-1]
                    read_author = True
                if "email" in l:
                    self.email = l[-1]
                    read_email = True

        if not read_type:
            self.mtype = None
        if not read_filename:
            self.filename = None
        if not read_subject:
            self.subject = None
        if not read_title:
            self.title = None
        if not read_author:
            self.author = None
        if not read_email:
            self.email = None


    def print_readme(self):
        """Generate a README file based on the collected information."""

        # read and format template
        if self.mtype == "Main":
            main_tmp = os.path.dirname(os.path.abspath(__file__)) + '/main_template.rst'
            with open(main_tmp, 'r') as tmp:
                template = tmp.read().format(
                                              self.title,
                                              self.author,
                                              self.email,
                                              self.date,
                                              )
        elif self.mtype == "Calculation":
            calc_tmp = os.path.dirname(os.path.abspath(__file__)) + '/calculation_template.rst'
            with open(calc_tmp, 'r') as tmp:
                template = tmp.read()

        # Write header plus formated template to README file
        with open(self.filename,"w") as readme:
            readme.write( self.__str__() )
            readme.write( template )

        print("\nThe {} file has been created sucessfully!".format(self.filename) )
        print("Open it and fill in the missing information.")
        print("Continue to update it until the end of your project.")


if __name__=="__main__":

    import argparse

    # check if the script was called with an input file
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i","--inp", type=str, help="Configuration file.", default=None)
    args = parser.parse_args()

    # set up of the necessary information for the readme file
    readme = metadata( args.inp )

    # generate readme file
    readme.print_readme()
