| **Creation date:** 28.01.2019
| **Metadata type:** Workflow
| **Subject:** Photo-chemistry
| **Project title:** Absorption spectrum of (solvated) iodine
| **Author:** Pablo Baudin
| **Email:** pablo.baudin@epfl.ch

GENERAL DESCRIPTION
===================

This directory regroups the calculations performed with the CPMD package
at the QM/MM level. The QM part consist of iodine while the MM part is a 
box of ethanol molecules.


SOFTWARE INFORMATION
====================

The main software used in this folder are the *CPMD* package and the
*comp_chem_py* library.

CPMD
----

The version of CPMD used was based on version 4.1.
It is a local version hosted on a private git repository:

https://gitlab.com/pablobaudin/cpmd_porting.git

Using the ``ml_playground`` branch and corresponding 
to git hash: ``83a3a1e63c44d6c3f6a5817ac45c57614c04e00c``

comp_chem_py
------------

The code is available at:
repo: https://gitlab.com/pablobaudin/comp_chem_py.git
branch: ``master``
git hash : ``c6c389f12bd5949682a8da680afe0d4ba77c62c8``

The functionalities of comp_chem_py used were:
* pyrun script for submission
* comp_chem_utils.cpmd_utils for seting upt the directories
* comp_chem_utils.spectrum for plotting the absorption spectra


HARDWARE INFORMATION
====================

All the calculations were ran on the local LCBC station: lcbcpc78


DATA & FILE OVERVIEW
====================

* Name: 10001, 10391, ..., 48611
* Short Description:

      Directories containing the individual calculations on snapshots.
      Each directory is named after the MD index corresponding to the
      geometry used.

* Name: README.rst
* Short Description:

		Present file which serves as metadata for the folder.

* Name: build_cpmd_input.py
* Short Description:

		Python script which can be used to create a cpmd input files based on
		two parameters, the functional, and the solvent.
		This is just to make the submission process more convenient.

* Name: camb3lyp_copy.py
* Short Description:

      Python script used to generate the CPMD input for the CAM-B3LYP calculations.

* Name: check_convergence.sh
* Short Description:

      Bash script used to check for convergence problem in the CPMD outputs.

* Name: global_blyp_spec.py, global_camb3lyp_spec.py
* Short Description:

      Python scripts used to plot the absorption spectra from all the calculations.

* Name: gromos.crd, gromos.inp, gromos.top
* Short Description:

      Gromos input files for the iodine in ethanol structure. Used as input for 
      the CPMD calculations and taken from: 
      iodine_spectrum/qmmm_equilibrations/ethanol/CPMD/restart/

* Name: setup.py
* Short Description:
      
      Python script used to generate all the calculations directory with the correct
      input and restart files (for the BLYP calculations).

* Name: super_submit.sh
* Short Description:

      Bash script used to submit all the calculations one by one.

WORKFLOW
========

run on the terminal::

   # Create 100 work directories ready for submission (TDDFT/BLYP calculations)
   ./setup.py
   #
   # Submit all blyp calculations one by one
   nohup ./super_submit.sh &
   #
   # Check for convergence problem
   ./check_convergence.sh
   #
   # Prepare input files for CAM-B3LYP calculations
   ./camb3lyp_copy.py
   #
   # Submit all camb3lyp calculations one by one
   # note: the func variable was modified inside the script
   nohup ./super_submit.sh &


