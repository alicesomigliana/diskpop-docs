.. _target to popcorn:

.. image:: images/popcorn_logo.png
  :width: 300
  :alt: Alternative text
  :align: center

popcorn
##################

popcorn is a Python library to analyse the output of Diskpop (described :ref:`here<target to output>`).
popcorn is automatically installed with Diskpop, say sth here
popcorn performs bets in a Jupyter notebook environment. In the Diskpop repository, under the `examples`` folder, we provide two
example notebooks reading a viscous and a MHD wind-driven population respectively.

Installation
-------------

popcorn is included in the Diskpop folder. To be able to import it in Jupyter notebooks, run the following commands from terminal:

.. code::

  cd path_to_diskpop/popcorn
  python setup.py bdist_wheel
  pip install dist/popcorn-0.0.1-py3-none-any.whl

.. note::

  If you want to overwrite a previously installed version of popcorn, replace the third line with

  .. code::

    pip install dist/popcorn-0.0.1-py3-none-any.whl --force-reinstall


.. note::

  The `setup.py` file of popcorn **forces the installation of the 1.21 version of numpy** because of compatibility issues
  with the following versions. We recommend setting up a virtual environment to avoid possible conflicts with other
  codes.



In the following, we describe the available functions.

popcorn functions
------------------

.. _target to used_in_tut:

Used in the tutorial notebook
+++++++++++++++++++++++++++++

- **popcorn.print_info(evolved_population)**

Prints all the simulations parameters, as input in :ref:`parameters.json<target to initial_parameters>`.

.. code:: 

    >>> evolvedpop = EvolvedPopulation('filename.hdf5')
    >>> popcorn.print_info(evolvedpop)

    Simulation Parameters
    Simulating a population of 100 objects
    Not using dust
    ...

- **load_data_pop_alltimes(evolved_population)**

Returns a dictionary of N elements, where N is the number of timesteps. Generating the dictionary through this function is 
a necessary step to load the arrays.

**Parameters:**
  **evolved_population**: object of type EvolvedPopulation

**Returns:**
  A dictionary containing pandas DataFrames of N elements, where N is the number of input timesteps.


.. code:: 

    >>> data = popcorn.load_data_pop_alltimes(evolvedpop)


- **popcorn.evolved_timesteps(evolved_population, data)**

Returns a numpy array filled with the input timesteps in Myr (`times_snapshots` in the parameters.json file).

**Parameters:**
  **evolved_population**: object of type EvolvedPopulation

  **data**: dictionary (pandas DataFrame) containing the simulation output, created by the `load_data_pop_alltimes` function

**Returns:**
  Numpy array filled with the input timesteps, in Myr.
  

.. code:: 

    >>> timesteps = popcorn.evolved_timesteps(evolvedpop, data)
    array([1e-3, 1e-2, 1e-1, 1, 5, 10])

- **popcorn.load_arrays(evolved_population, data, timesteps, mhd = False)**

Returns a set of arrays filled with the disc and stellar properties for all YSOs in the population at required ages.

**Parameters:**
  **evolved_population**: object of type EvolvedPopulation

  **data**: list of pandas DataFrames, created by the `load_data_pop_alltimes` function

  **timesteps**: array of ages at which the disc and stellar properties are extracted. It needs to contain
    ages at which Diskpop output was produced (i.e., values that were input in `times_snapshots` 
    in the parameters.json file) as it *recovers* the parameter from the simulation and does not interpolate them.

  **mhd**: `True` if the population evolved under the influence of MHD winds, `False` otherwise (default is `False`).
    Depending on the value of this parameter, the number of output arrays changes; if `True`, it includes also 
    :math:`f_{\mathrm{M}, 0}`, :math:`\alpha_{\mathrm{DW}}` and the plasma :math:`\beta`.

**Returns:**
  Set of numpy N-D arrays filled with the disc and stellar properties.

  - **mstar**: stellar masses [:math:`M_{\odot}`], 2D (mstar[i][j] is the stellar mass at the i-th timestep of the j-th object).
  - **mdisc**: disc gas masses [:math:`M_{\odot}`], 2D (same as mstar).
  - **mdot**: accretion rate on the star [:math:`M_{\odot}`/yr], 2D (same as mstar)
  - **sigma_g**: gas surface density at all disc radii [g/cm^2], 3D (sigma_g[i][j][k] is the surface density of the j-th object at the i-th timestep in the k-th radial location).
  - **tacc0_Myr**: initial accretion timescale (viscous timescale in the viscous case) [Myr], 1D (tacc0_Myr[i] is the initial accretion timescale of the i-th object).
  - **Rd**: disc gas radius [au], 2D (same as mstar).
  - **mask**: boolean mask on the object type, containing `True` if Class II and `False` if Class III, 2D (same as mstar).

  Only if mhd=True:

  - **fM0**: :math:`f_{\mathrm{M}, 0}` parameter from `Tabone et al. (2022) <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.2290T/abstract>`_, 1D (same as tacc0_Myr).
  - **alpha_DW**: :math:`\alpha_{\mathrm{DW}}` parameter from `Tabone et al. (2022) <https://ui.adsabs.harvard.edu/abs/2022MNRAS.512.2290T/abstract>`_, 1D (same as tacc0_Myr).
  - **beta**: plasma :math:`\beta` parameter, 1D (same as tacc0_Myr).

  .. code:: 

    >>> mstar, mdisc, mdot, sigma_g, R, tacc0_Myr, Rd, mask = popcorn.load_arrays(evolvedpop, data, timesteps, mhd = False)
    >>> mdisc
    [array([1.16110830e-06, 1.27484691e-05, ...]), array([1.13979059e-06, 1.26284132e-05, ...]), ...]


Additional functions
+++++++++++++++++++++

Users of Diskpop will most likely only need the functions described :ref:`above <target to used_in_tut>`; in the following,
we describe the rest of the popcorn functions (which are used in the main ones described above) for completeness.


- **popcorn.load_data_population(evolved_population, time_index)**

  Same as **popcorn.load_data_pop_alltimes**, but limited to a single timestep.

  **Parameters:**
    **evolved_population**: object of type EvolvedPopulation

    **time_index**: index corresponding to the output age of the population in the _timesteps_ array (timesteps[time_index] 
    is the desired age in Myr).

  **Returns:**
    A dictionary containing a pandas DataFrames of disc properties at age `timesteps[time_index]`.


- **popcorn.load_data_alltimes(evolved_population, yso_index)**

  Same as **popcorn.load_data_pop_alltimes**, but limited to a single disc in the population.

  **Parameters:**
    **evolved_population**: object of type EvolvedPopulation

    **yso_index**: index corresponding to the required YSO in the population.

  **Returns:**
    A dictionary containing a pandas DataFrames of disc properties at all ages for the yso_index-th YSO.

- **popcorn.load_data(evolved_population, yso_index, time_index, verbose = False)**

  Same as **popcorn.load_data_pop_alltimes**, but limited to a single disc in the population at a single age.

  **Parameters:**
    **evolved_population**: object of type EvolvedPopulation

    **yso_index**: index corresponding to the required YSO in the population.

    **time_index**: index corresponding to the output age of the population in the _timesteps_ array (timesteps[time_index] 
    is the desired age in Myr).

  **Returns:**
    A dictionary containing a pandas DataFrames of disc properties of the yso_index-th YSO at age timesteps[time_index].


- **popcorn.convert(data)**

    Converts the radius from cm to au and the disc mass (both in gas and dust, if applicable) from grams to :math:`M_{\odot}`. 

 **Parameters:**
  **data**: dictionary (pandas DataFrame) containing the simulation output, created by the `load_data_pop_alltimes` function

 **Returns:** converted input dictionary (pandas DataFrame).


- **popcorn.fildic2df(fulldata, wanted_keys)**

  Filters a dictionary, returning a new one with only the chosen variables.

  **Parameters:**
    **fulldata**: full dictionary (pandas DataFrame) to be filtered.

    **wanted_keys**: list of variables to be mainteined in the new dictionary 
    
    (ex. wanted_keys =
    ['t_Myear', 'sigma_g']).

  **Returns:** filtered input dictionary (pandas DataFrame).

  .. code:: 

    >>> filtered_data = popcorn.fildic2df(data, wanted_keys = ['t_Myear', 'sigma_g'])

- **popcorn.g2Msun(mass)**:
  Converts a mass from grams to solar masses.

  **Parameters:**
    **mass**: mass in grams.

  **Returns:** mass in solar masses.

- **popcorn.cm2au(length)**:
  Converts a length from cm to au.

  **Parameters:**
    **length**: length in cm.

  **Returns:** length in au.

- **popcorn.second2year(time)**:
  Converts a time from seconds to years.

  **Parameters:**
    **length**: time in seconds.

  **Returns:** time in years.

- **popcorn.year2second(time)**:
  Converts a time from years to seconds.

  **Parameters:**
    **length**: time in years.

  **Returns:** time in seconds.



Tutorial
---------

Tutorial notebooks to use the main features of popcorn are available `here ADD LINK<blabla>`. This link leads to an examples folder, which includes two jupyter notebooks and their corresponding output files, to read a viscous and MHD-wind driven population respectively.


