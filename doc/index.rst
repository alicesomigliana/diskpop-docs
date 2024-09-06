.. Diskpop documentation master file, created by
   sphinx-quickstart on Thu Feb  3 10:52:58 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. image:: images/Logo_transparent.png
  :width: 1000
  :alt: Alternative text
  
.. rst-class:: center
   
A Python code for population synthesis of protoplanetary discs
================================================================


Diskpop is a Python code used to generate and evolve synthetic populations of protoplanetary discs. It includes the viscous, hybrid and MHD-wind driven accretion prescriptions, internal and external photoevaporation, as well as dust evolution.

The physical processes and solution algorithms employed are described in  :ref:`Solution algorithms<target to solution>`, while the initial conditions are discussed in :ref:`Initial conditions <target to initial_parameters>`.

To analyse the raw output of Diskpop, the Python library :ref:`popcorn<target to popcorn>` is available. Both codes have been published in `Somigliana et al. (2024) <https://ui.adsabs.harvard.edu/abs/2024arXiv240721101S/abstract>`_.


Using Diskpop for your work
-----------------------------

Diskpop and popcorn are freely available for the community to use. If you use Diskpop simulations in your work, please make sure to cite `Somigliana et al. (2024) <https://ui.adsabs.harvard.edu/abs/2024arXiv240721101S/abstract>`_. The code is based on Richard Booth’s repository, and the dust module is entirely forked with no modifications; if you include dust in your simulations, please cite also `Booth et al. (2017) <https://ui.adsabs.harvard.edu/abs/2017MNRAS.469.3994B/abstract>`_.


Installation
-------------

Diskpop can be installed from terminal as

.. code-block :: bash

	pip install diskpop

Alternatively, it is also possible to clone the Bitbucket repository.

Likewise, the output analysis library popcorn can be installed from terminal as

.. code-block :: bash

	pip install popcorn_diskpop

or accessed cloning the Bitbucket repository.

Diskpop Team
-------------

Diskpop and popcorn have been developed by Alice Somigliana, Giovanni Rosotti, Marco Tazzari, Leonardo Testi, Giuseppe Lodato, 
Claudia Toci, Rossella Anania, and Benoît Tabone. Both codes are under active development; for questions or bugs report, 
see :ref:`Bugs and features <target to bugsandfeatures>`. 


.. toctree::
   :maxdepth: 4
   :caption: Documentation contents:

   Basic Functioning <basics>
   User interface <user_interface>
   Solution algorithm <solution_algorithm>
   popcorn <popcorn>
   Bugs and features <bugs_features>


Acknowledgements
-----------------

This project was partly supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - Ref no. 325594231 FOR 2634/2 TE 1024/2-1, by the DFG Cluster of Excellence Origins (www.origins-cluster.de). This projec has received funding from the European Research Council (ERC) via the ERC Synergy Grant ECOGAL (grant 855130).