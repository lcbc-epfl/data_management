| **Creation date:** 28.01.2019
| **Metadata type:** Project description
| **Subject:** Photo-chemistry
| **Project title:** Absorption spectrum of (solvated) iodine
| **Author:** Pablo Baudin
| **Email:** pablo.baudin@epfl.ch


GENERAL INFORMATION
===================

* **Title:** Absorption spectrum of (solvated) iodine

* **Author information:** 
  
  * Pablo Baudin
  * Institution: Laboratory of Computational Chemistry and Biochemistry, EPFL
  * Email: pablo.baudin@epfl.ch

* **Collaborators:**

  * Luca Longetti
        * Institution: Laboratory of Ultrafast Spectroscopy, EPFL 
        * Email: luca.longetti@epfl.ch

  * Majed Chergui
        * Institution: Laboratory of Ultrafast Spectroscopy, EPFL
        * Email: majed.chergui@epfl.ch

  * Ursula Röthlisberger
        * Institution: Laboratory of Computational Chemistry and Biochemistry, EPFL
        * Email: ursula.roethlisberge@epfl.ch

* **Project status and dates:** 

  * Started: 09.04.2019
  * Finished:
  * Published:

* **Project description:**

    As a first step, the goal of this project is to reproduce and rationalize 
    the absorption spectrum of iodine in different solvent. In particular, the 
    experimentalist would like to understand the strong blue shift of the lower
    covalent transition which happen when iodine is put in ethanol.


SHARING/ACCESS INFORMATION
==========================

* Recommended citation for the data:

* Links to publications that cite or use the data:

* Licenses/restrictions placed on the data:

* Other important links:


DATA & FILE OVERVIEW
====================

Most sub-directories are named based on the quantum chemistry package
used to perform the calculations it contains.
Further information can be found in the README file present in each
sub-directory.

* Name: adf
* Short Description: 

      Includes many TDDFT calculations, some include
      relativistic effect and spin-orbit coupling. Solvent effect
      have also been included implicitly with the COSMO model.
      Attempts to describe the solvent excplicitly are also included.

* Name: cpmd
* Short Description:

      Contains TDDFT calculations with CPMD. BLYP, B3LYP and CAMB3LYP
      functional have been tested, as well as different plane wave cutoffs
      and different cell dimensions. QMMM calculations have also been 
      performed. Plots of the orbitals are included as well as tentative
      of inclusion of spin-orbit coupling effects.

* Name: dalton
* Short Description: 

      The Dalton package has been used to performe some coupled cluster
      calculations on gas phase iodine from CCS to CC3.

* Name: experimental
* Short Description:

      Contains the experimental data given by Majed's group as absorption
      spectra which have then been digitalized.

* Name: gaussian
* Short Description:

      Gaussian geometry optimization and TDDFT/BLYP calculation of I2 in
      gas phase.

* Name: newton-x
* Short Description:

      Calculation of gas phase I2 absorption spectrum using Gaussian via
      newton-x.

* Name: orca
* Short Description:

      Calculation on gas phase I2 at CIS(D), CASSCF, NEVPT2 and TDDFT levels.
      Also contains some COSMO (implicit solvent) calculations.

* Name: qmmm_equilibrations
* Short Description:

      Contains all the calculations with AMBER and CPMD to get MD snapshots
      for I2 in ethanol, n-hexane, and water.

* Name: turbomole
* Short Description:

      Calculation on gas phase I2 at ADC(2), CC2 and TDDFT levels.
      Also contains some COSMO (implicit solvent) calculations.

* Name: README.rst
* Short Description: 

      Present file which serves as metadata for the iodine project.

* Name: relat_corr.dat
* Short Description: 

      Collection of iodine excitation energies from published works.
      The description of data is included in the file itself.


METHODOLOGY AND WORKFLOW
========================

The first steps of the project consisted in reproducing the gas phase spectrum
of I2. The reference data were taken from *relat_corr.dat*. 
The corresponding results are available in the following folders:

* adf
* cpmd
* dalton
* gaussian
* newton-x
* orca
* turbomole

Afterwards, the inclusion of implicit solvent was performed in:

* adf
* orca
* turbomole

The preparation of snapshot from QM/MM MD simulations was performed 
in *qmmm_equilibrations*. 

TDDFT calculations on the snapshots were done in *cpmd*.

