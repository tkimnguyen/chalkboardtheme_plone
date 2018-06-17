=====================
plonetheme.chalkboard
=====================

`Chalkboard Theme`_ from (a Wordpress theme), applied to Plone 4.3.x using Diazo.


Introduction
============

*Chalkboard Theme* is an installable Plone theme package that using the **packaging** 
features available in Plone 4.3.x, developed by `Leonardo J. Caballero G.`_, which in 
turn packages the `chalkboardtheme_plone`_ Diazo theme developed by `T. Kim Nguyen`_ 
using the **theming** features available in `plone.app.theming`_.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/tkimnguyen/chalkboardtheme_plone/blob/master/screenshot.png


Features
========

- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- It's have support for clean uninstallation.
- Also it's a simple Diazo package (Zip file).


Installation
============


Zip file
--------

If you are an end user, you might enjoy installation via zip file import.

1. Download a `zip file <https://github.com/tkimnguyen/plonetheme.chalkboard/raw/master/plonetheme.chalkboard.zip>`_.
2. Import the theme from the Diazo theme control panel.


Enabling the theme
^^^^^^^^^^^^^^^^^^

Select and enable the theme from the Diazo control panel. That's it here!

To make this theme work correctly, got to the ``Theming`` control panel's ``Advanced settings`` 
change the ``Theme base`` from the default "Sunburst Theme" to "(Unstyled)".


Disabling the theme
^^^^^^^^^^^^^^^^^^

Select and disable the theme from the Diazo control panel. That's it here!

For uninstall this theme work correctly, got to the ``Theming`` control panel's ``Advanced settings`` 
change the ``Theme base`` from the default "(Unstyled)" to "Sunburst Theme".


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``plonetheme.chalkboard`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.chalkboard


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.chalkboard',
    ],


Usage
=====

This currently shows the Plone content object's title, body, and byline, as well as the 
right portlet column.

Everything else is hardcoded – sorry :) – please contribute your improvements!


Contribute
==========

- Issue Tracker: https://github.com/plone-ve/plonetheme.chalkboard/issues
- Source Code: https://github.com/plone-ve/plonetheme.chalkboard


License
=======

The project is licensed under the GPLv2.

Credits
-------

- T\. Kim Nguyen (tkimnguyen).

.. _`Chalkboard Theme`: https://wordpress.org/themes/classic-chalkboard/
.. _`chalkboardtheme_plone`: https://github.com/tkimnguyen/chalkboardtheme_plone
.. _`Leonardo J. Caballero G.`: http://macagua.github.io/
.. _`T. Kim Nguyen`: https://twitter.com/tkimnguyen
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
