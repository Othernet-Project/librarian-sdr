==============
librarian-sdr
==============

This component includes a setup wizard step to install sdr100 binary

Installation
------------

The component has the following dependencies:

- librarian_

To enable this component, add it to the list of components in librarian_'s
`config.ini` file, e.g.::

    [app]
    +components =
        librarian_sdr

Configuration
-------------

``sdr.binary_path``
    Path where the sdr100 binary should be stored.
    Example::

        [sdr]
        binary_path = /usr/sbin/sdr100

Development
-----------

In order to recompile static assets, make sure that compass_ and coffeescript_
are installed on your system. To perform a one-time recompilation, execute::

    make recompile

To enable the filesystem watcher and perform automatic recompilation on changes,
use::

    make watch

.. _librarian: https://github.com/Outernet-Project/librarian
.. _compass: http://compass-style.org/
.. _coffeescript: http://coffeescript.org/
