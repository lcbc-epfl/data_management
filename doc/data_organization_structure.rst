.. _data-organization-structure:
Data organization structure
------------------------------------------

Notes
******************

Think about how you can make your project most accesible to yourself and others. It should be possible to figure out what you did and which system you use in every directory of your document. This does not mean you need to create page long README files in every directory but rather keep a consistent structure of your files which makes things easier not only for yourself but also for others. 

Things that can help you achieve this are: 
********************************************************

* Give each project a common identifier. This makes it more evident, what the current system is just by looking at any folder in your project. 
    * Abbreviation for your system name like GB1 (Guanine nucleotide-binding protein subunit beta1), RNH (RNase H)
    * Use a modifier for every major modification you make to your system. RNH.dsDNA is the RNH protein with dsDNA instead of RNA/DNA hybrid. The modifier is used as a prefix for every coordinate file you generate. 

* Use common suffixes and keep them consistent. E.g _dry, _solv categories when generating modifications to your input coordinates from a crystal structure. 

READMEs, where?
**********************
There should be one general, long README file in the root folder of your projects and shorter README files in the respective subdirectories. The long README file describes overall goals of your project and gives guidance on how to process in understanding the data in the subdirectories. The shorter README files in the respective folders should give information pertinent to rerunning and understanding this specific calculation or analysis. 

More information on how to write the README files find in the README section

Folder structure
**********************************
We don't want to limit you in your creativity or your workflow so we won't enforce a specific one-size-fits-all folder structure.

However, we request you to think about your folder structure before starting with the project and avoid arbitray named folders or folders like test, junk etc at any cost. 

For making the project accessible to any third party try organizing the files of every project in a folder where you organize all inputs for the calculation (unedited crystal structures etc.), folders where you store calculation raw data with no modification and folders where you store data that was generated based on your raw data (energy plots, density plots, RMSD distributions etc.) 

.. code-block:: bash

    $ tree project_folder
    ├── README
    ├── input_prep
    |   ├── crystal_structures
    |   ├── parameters
    |   ├── docking
    ├── computations
    |   ├── QM
    |   |   ├── SYSTEM.geo_opt.1
    |   |   ├── SYSTEM.qmmm_md.1
    |   ├── metadyn
    |   |   ├──SYSTEM.noH.metadyn.1
    |   ├── [..]
    ├── analysis

