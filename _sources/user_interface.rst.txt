.. _target to user_interface:

.. rst-class:: center
User Interface
##################

The user interface of Diskpop is the **parameters.json** file, which stores all of the user-defined parameters to initialise
the disc population and customise the type of evolution. The output is printed on an .hdf5 file that can be read with the library
popcorn (described in the :ref:`dedicated section <target to popcorn>`).


.. _target to initial_parameters:

Initial parameters
===================

The default **parameters.json** is shown below:

.. literalinclude:: parameters.json
  :language: JSON

The file is structured in nested sub-groups of parameters depending on which type of property of the simulation 
they control:

#. *parameters_options* set the general properties of the simulation (e.g., whether to perform a Monte-Carlo extraction of the population parameters);
#. *parameters_population* are set to simulate a whole population of discs;
#. *parameters_singledisc* are set to manually determine the disc parameters.

Below is a description of the meaning (and possible choices, where applicable) of all the simulation parameters.
The default values of all the simulation parameters are stored in the ``defaults.py`` file.


parameters_options
--------------------

The options can be set to either *true* (a) or *false* (b):


.. note:: 

    Note the syntax: in .json files, the boolean values must be written in *lowercase*.

**options.MONTECARLO** sets whether the disc properties are (a) determined from a distribution (to be specified further in the
parameters file) or (b) manually set by the user;

**options.CORRELATIONS** sets whether the disc properties are determined based on the observed correlations with the stellar mass, :math:`M_{\mathrm{d}} \propto {M_{\star}}^{\lambda_{\mathrm{m}}}` and :math:`\dot M \propto {M_{\star}}^{\lambda_{\mathrm{acc}}}`;

.. note::

    It is only meaningful to set **options.CORRELATION** to **True** if **options.MONTECARLO** is also **True**. 
    This is because **options.MONTECARLO** puts the strongest requirement on initial conditions: given that it requires 
    each parameter to be set manually, it does not allow to perform a drawing of the parameters themselves (which could actually 
    make use of the provided correlations).


**options.REPRODUCIBILITY**: sets the reproducibility (a) or lack thereof (b) of the simulation. If true, setting a seed for the random extractions is required;

**options.MHD**: sets whether the discs are subjected to MHD winds (a) or not (b);

**options.INTERNAL_PHOTOEV**: sets whether the discs are subjected to internal photoevaporation (a) or not (b);

**options.DO_PLOTS**: **NEED TO REMOVE THIS**

**multiprocessing_options**: contains the parameters to set to evolve the simulation in parallel;
    - **parallel_evol**: sets whether to evolve in parallel (a) or not (b);
    - **all_available_proc**: sets whether the simulation should take up all of the available processors on the machine (a) or not (b)
    - **nproc**: allows to manually set the number of processors to use (has to be an integer number).



parameters_population
-----------------------

Within *parameters_population* there are 6 additional levels: *parameters_general*, *parameters_mhd*, *parameters_imf*, 
*parameters_correlations*, *parameters_nocorrelation* and *parameters_spreads*:

- **parameters_general**

    These parameters set the general properties of the simulation and must be set regardless of the type of population and disc evolution.


    - **output_name**: sets the .hdf5 output file name. Can be any string, default value is `default`.
    If `default`, the file name will be assembled combining 
    the key parameters. With options.MONTECARLO = True, it will be set as '(no)dust_Montecarl_corr=(true)false_XYZ' depending
    on the presence of dust and correlation between the parameters, where XYZ is the date and time of the simulation; with 
    options.MONTECARLO = False, it will be set as '(no)dust_alphavalue_mdiscmean_rdiscmean_single_disc_XYZ' combining the values
    of the `Shakura & Sunyaev (1973) <https://ui.adsabs.harvard.edu/abs/1976MNRAS.175..613S/abstract>`_ :math:`\alpha` parameter,
    the mean disc mass and the mean disc radius of the simulation.

    - **nysos**: sets the initial number of discs in the population. Default value is :math:`100`.

    - **analytic**: can be true or false and sets whether to use the analytic solution. If an analytic solution is not available for the chosen combination of parameters, an error message is printed.

    - **times_snapshot**: ages at which the output will be printed, in Myr. Has to be in the form [age1, age2, ...].

    - **alpha**: `Shakura & Sunyaev (1973) <https://ui.adsabs.harvard.edu/abs/1976MNRAS.175..613S/abstract>`_ :math:`\alpha` parameter
   
    - **dust**: can be true or false, sets whether to include dust in the simulation.
   
    - **limit_discmass**: sets the disc mass (in :math:`M_{\odot}`) below which the disc is considered dispersed (see :ref:`disc dispersal <target to discdispersal>`). Default value is :math:`10^{-6}`.
   
    - **d2g**: the dust-to-gas ratio of the simulation (standard value :math:`0.01`).
   
    - **seed**: can be an integer number or `null`. If options.REPRODUCIBILITY is set to True, it sets the seed to use in the 
    random number generators for the simulation to be easily reproduced. If `null`, the seed is not set.


- **parameters_mhd**

    These parameters set the MHD wind parameters as defined by `Tabone et al. (2022) <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.2290T/abstract>`_. The third parameter, :math:`\alpha_{\rm{DW}}`, is determined from the correlation with the plasma :math:`beta` parameter (see REFREFREF).


    - **leverarm**: `Tabone et al. (2022) <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.2290T/abstract>`_ :math:`\lambda` parameter. Default value is 3.
   
    - **omega**: `Tabone et al. (2022) <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.2290T/abstract>`_ :math:`\omega` parameter. Default value is 0.25.

    .. note::

        Setting the MHD parameters is only meaningful is options.MHD is set to true.    


- **parameters_imf**

    These parameters determine how the stellar masses of the population of YSOs are extracted, and need to be set for every type of simulation.

    - **imf**: sets the IMF to use to generate the population of YSOs. Possible options are `kroupa` (which follows the `Kroupa (2002) <https://ui.adsabs.harvard.edu/abs/2002Sci...295...82K/abstract>`_ prescription), `single` (all stars will have :math:`M_{\star} = 1 M_{\odot}`) or `custom`. If `custom`, the user must provide a file called `mstar.txt` with the desired stellar masses, in the same folder as the parameters file, that will be used as input to build the population.

    .. note::

        If **nysos** and the lenght of the `mstar.txt` files differ, the former will be overwritten to match the number
        of stellar masses provided.

    - **mmin**: minimum stellar mass [:math:`M_{\odot}`]. Default is :math:`5 \times 10^{-2}`. If imf is `kroupa`, the minimum stellar mass must be smaller than :math:`8 \times 10^{-2}`.

    - **mmax**: maximum stellar mass [:math:`M_{\odot}`]. Default is :math:`50`. If imf is `kroupa`, the maximum stellar mass must be bigger than :math:`1`.


- **parameters_correlation**

    These parameters determine the disc properties when **options.CORRELATION** is set to True.


    - **beta**: slope of the correlation between the disc aspect ratio and the stellar mass, :math:`H/R \propto {M_{\star}}^{\beta}`. Default is :math:`-0.5`.

    - **mdisc_norm**: disc mass for a solar-type star (normalisation of the correlation between the disc mass and the stellar mass) [:math:`M_{\odot}`]. Default is :math:`5 \times 10^{-3}`.

    - **mdisc_slope**: slope of the correlation between the disc mass and the stellar mass, :math:`M_{\mathrm{d}} \propto {M_{\star}}^{\text{mdisc_slope}}`. Default is 2.1. In the release paper Somigliana et al. 2024, this parameter is :math:`\lambda_{\mathrm{m}, 0}`.
   
    - **mdot_slope**: slope of the correlation between the accretion rate and the stellar mass, :math:`\dot M \propto {M_{\star}}^{\text{mdot_slope}}`. Default is 1.5. In the release paper Somigliana et al. 2024, this parameter is :math:`\lambda_{\mathrm{acc}, 0}`.

    - **beta_mag_norm**: plasma :math:`\beta` parameter for a solar-type star. Default is :math:`6 \times 10^{-4}.`

    - **beta_mag_slope**: slope of the correlation between the plasma :math:`\beta` parameter and the stellar mass, :math:`\beta \propto {M_{\star}}^{\text{beta_mag_slope}}`.

    - **L_x_norm**: stellar X luminosity for a solar-type star [erg/s] (normalisation of the correlation between the stellar X luminosity and the stellar mass). Default is :math:`10^{30}`.

    - **L_x_slope**: slope of the correlation between the stellar X luminosity and the stellar mass, :math:`L_x \propto {M_{\star}}^{\text{L_x_slope}}`

    - **mdot_photoev_norm**: mass-loss rate due to internal photoevaporation for a solar-type star [:math:`M_{\odot}/\rm{yr}^{-1}`] (normalisation of the correlation between the mass-loss rate and the stellar mass). Default is :math:`6.25 \times 10^{-9}`.

    - **mdot_photoev_slope**: slope of the correlation between the mass-loss rate due to internal photoevaporation and the stellar mass, :math:`\dot M_{\rm{photoev}} \propto {M_{\star}}^{\text{mdot_photoev_slope}}`.


   
    .. note::

        Setting this set of parameters is only meaningful if both options.MONTECARLO and options.CORRELATION are set to true.  

- **parameters_nocorrelation**

    These parameters determine the mean values of the disc properties when **options.CORRELATION** is set to False.

    - **mdisc_mean**: mean disc mass [:math:`M_{\odot}`]. Default is :math:`5 \times 10^{-2}`.

    - **rdisc_mean**: mean disc radius [au]. Default is 10.

    - **beta_mag_mean**: mean plasma :math:`\beta` parameter. Default is :math:`10^6`.

    - **alpha_DW_mean**: mean `Tabone et al. (2022) <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.2290T/abstract>`_ :math:`\alpha_{\rm{DW}}` parameter. Default is :math:`10^{-3}`.

    - **L_x_mean**: mean stellar X luminosity [erg/s]. Default is :math:`10^{30}`.

    - **mdot_photoev_mean**: mean mass-loss rate due to internal photoevaporation [:math:`M_{\odot}/\rm{yr}`]. Default is :math:`10^{-9}`.

    .. note::

        Setting this set of parameters is only meaningful if options.MONTECARLO is set to true and options.CORRELATION is set to false.


- **parameters_spreads**

    These parameters determine the spread of the disc parameters, regardless of whether they correlate with the stellar mass or not.
    
    - **mdisc_spread**: spread of the correlation between the disc mass and the stellar mass [dex]. Default is 0.5.

    - **rdisc_spread**: spread of the correlation between the disc radius and the stellar mass [dex]. Default is 0.5.

    - **beta_mag_spread**: spread of the correlation between the plasma :math:`\beta` parameter and the stellar mass [dex]. Default is 0.

    - **alpha_spread**: spread of the correlation between the `Shakura & Sunyaev (1973) <https://ui.adsabs.harvard.edu/abs/1976MNRAS.175..613S/abstract>`_ :math:`\alpha` parameter and the stellar mass [dex]. Default is 0.

    - **L_x_spread**: spread of the correlation between the stellar X luminosity and the stellar mass [dex]. Default is 0.1.

    - **mdot_photoev_spread**: spread of the correlation between the mass-loss due to internal photoevaporation and the stellar mass [dex]. Default is 0.5.

    .. note::

        Setting this set of parameters is only meaningful if options.MONTECARLO is set to true - otherwise, the parameters are determined from the single disc mode.


parameters_singledisc
-----------------------

- **mstar**: array of stellar masses [:math:`M_{\odot}`] in the form [Mstar1, Mstar2, ...]. 

- **mdisc**: array of disc masses [:math:`M_{\odot}`] in the form [Mdisc1, Mdisc2, ...]. 

- **rdisc**: array of disc radii [au] in the form [Rdisc1, Rdisc2, ...]. 


    .. note::

        Setting this set of parameters is only meaningful if options.MONTECARLO is set to false.



Running Diskpop
================

Once the parameter are set in the *parameters.json* file, this is how to run a Diskpop simulation from terminal:

.. code::

    cd path_to_diskpop_folder
    python run_set.py parameters.json

The simulation will print the output file name, determined with the **output_name** parameter, together with the number of time steps selected. 
While the simulation proceeds, the current time step is also printed. If a disc ends up being dispersed during the simulation, that information is also printed on screen. 


.. _target to output:

Output
=======

The output of a Diskpop run in a .hdf5 file named according to the choice of the **output_name** parameter.
In the following, we briefly explain the structure of .hdf5 files for ease of understanding - however, the *popcorn* library (described :ref:`here <target to popcorn>`) allows to readily read and analyse the output and takes care of the .hdf5 file. 


.hdf5 files
************

In this section, we aim at giving some basic ideas on .hdf5 files; for a deeper discussion, we suggest `the HDF5 library webpage <https://www.hdfgroup.org/solutions/hdf5/>`__
and `the h5py documentation <https://www.h5py.org>`__.

The Hierarchical Data Format (HDF) version 5 is a file format that supports heterogeneous and complex data.
HDF files are structured 'directory-like', allowing to organize the information stored in one single file in a way that is very
similar to a computer's folders system. What is a 'directory' or a 'folder' in a computer, is a 'group' in HDF; what is a 'file'
in a computer, is a 'dataset' in HDF. Groups are folder-like elements in a file that can contain other groups or datasets, while 
datasets contain the actual data stored in the file as well as metadata describing them.

.. figure:: images/hdf5_structure.pdf
    :width: 600

    Structure of a .hdf5 file. 

A key feature of .hdf5 files is that they are designed to store big data, and are therefore compressed and easy to *slice*. 
Moreover, HDF is a *heterogeneous* format - meaning that the same file can contain datas of different types, just as much
as directories in computers do.

Despite the numerous similarities with directories, HDF files cannot be accessed exactly as a folder on the computer;
however, using a programming language, it is possible to access the information stored in the metadata - which 
are already linked to the group of datasets of interest. For users of Diskpop, this is done within :ref:`popcorn <target to popcorn>`.

In Diskpop, each simulation returns a .hdf5 file as an output. The first level of groups are represented by the 
*timesteps* at which the population was evolved (given in input with the **times_snapshot** parameter); each of these groups/directories
in turn contains other groups, which represent the single YSOs in the population; these groups are then splitted in two further groups,
which contain the datasets for the star and disc respectively. *popcorn* bypasses the need to slice the output file and gives N-dimensional
arrays containing the disc and stellar properties for each YSO in the population at all timesteps.


