Data organization structure
------------------------------------------

Biomolecular projects
***************

Notes
******************

Each project should get a common identifier, which can be modified with a subidentifier for modified structures, to make it evident, what the current system is, just by looking at any folder in your project. 

Ideally, use something like:

* Abbreviation for your system name like GB1 (Guanine nucleotide-binding protein subunit beta1), RNH (RNase H)

* Use a modifier for every major modification you make to your system. RNH.dsDNA is the RNH protein with dsDNA instead of RNA/DNA hybrid. The modifier is used a prefix for every coordinate file you generate. 

* Common modifiers should use the same suffix. E.g always use _dry, _solv categories when generating input files as you go

READMEs, where?
**************
There should be one general, long README file in the root of your project describing the system and major subsystems you made + a current date, which software, which clusters were used and how you can be reached. 
E.g RNase H with hybrid DNA/RNA, dsDNA and dsRNA. 

Use the recommended folder structure below and place shorter README files in the respective subdirectories

Folder structure
**********************************
* README

* prep
    * README
       * describes the system a bit
    * orginal_files
      * contains all files downloaded from RCSB etc.
    * params_QM
      * deposit any basis set files etc here
    * params_MD
      * contains used parameter set, especially self generated parameters e.g MD parameters from MCPB or modifed basis set files
    * docking
      * if you had to dock your ligand etc. 
    * add all other steps you undertook before doing actual "simulation" of your system
* calc
  * MD
    * README
      * add a line for each simulation you do, add one line results here or point to summary file of analysis
    * SYSTEMNAME.freeform.1
      * name each simulation starting with the system name and then use freeform to indicate what it is e.g first_equilibration, try using the keywords min, eq, nvt, npt, eq, prod, analysis for directories in this one, describe with README files to be able to reproduce all terminal commands you use. 
    * add all further MD simulations here 

  * metadyn
    * README
      * add a line for each simulation you do and why you did it, add one line results here or point to summary file of analysis
    * SYSTEMNAME.freeform.1
      * name each simulation starting with the system name and then use freeform to indicate what it is e.g first_equilibration, try using the keywords min, eq, nvt, npt, eq, prod 
    * add all further metadyn simulations here 
  * .....
    * Add all other types of calculations you do with a representative keyword here. E.g qmmm, mmpbsa, genetic_algorithm 

  * scripts 
  deposit all the scripts you use for analysis in the script folder, ideally add scripts to you path so you can reference them more easily



Ideas to make it easier to adopt
**********************************

Create new script that can quickly generate a boilerplate for the recommended directories that can then be filled by the user. 

.. code-block:: bash

   $ generate_new_project
   > generating new project in ~/projects
   > Enter project name: 
   > Enter system name: 
   > all folders created, press [y] to proceed to edit project root README, [n] to exit



