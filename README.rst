.. figure:: https://user-images.githubusercontent.com/8652625/40595190-1e16e90e-626e-11e8-9dc7-207d691c6d6d.jpg
    :align: center
    :alt: The Harvesters

    Pieter Bruegel the Elder, The Harvesters, 1565, (c) The Metropolitan Museum of Art

.. image:: https://img.shields.io/pypi/v/harvesters_gui.svg
    :target: https://pypi.org/project/harvesters_gui

.. image:: https://img.shields.io/pypi/pyversions/harvesters_gui.svg

----

######################
What Is Harvester GUI?
######################

Harvester GUI is a reference implementation of a `Harvester <https://github.com/genicam/harvesters>`_-based GUI. We need to admit that it must not be the one that satisfies your realuse cases but it should give you an idea how you can design a GUI that is based on Harvester as its image acquisition front-end.

You can freely use, modify, distribute Harvester under `Apache License-2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_ without worrying about the use of your software: personal, internal or commercial.


----

.. contents:: Table of Contents
    :depth: 1

**Disclaimer**: All external pictures should have associated credits. If there are missing credits, please tell us, we will correct it. Similarly, all excerpts should be sourced. If not, this is an error and we will correct it as soon as you tell us.

----

#############
Announcements
#############

- **Version 1.0.2**: Resolves issue `#22 <https://github.com/genicam/harvesters_gui/issues/22>`_.
- **Version 1.0.1**: Resolves issue `#17 <https://github.com/genicam/harvesters_gui/issues/17>`_.
- **Version 1.0.0**: Resolves issue `#16 <https://github.com/genicam/harvesters_gui/issues/16>`_.
- **Version 0.4.0**: Resolves issue `#15 <https://github.com/genicam/harvesters_gui/issues/15>`_.
- **Version 0.3.0**: Resolves issues `#11 <https://github.com/genicam/harvesters_gui/issues/11>`_ and `#14 <https://github.com/genicam/harvesters_gui/issues/14>`_.
- **Version 0.2.6**: Resolves issue `#13 <https://github.com/genicam/harvesters_gui/issues/13>`_.
- **Version 0.2.5**: Use Harvester version ``0.2.4``.
- **Version 0.2.4**: Use Harvester version ``0.2.3``.
- **Version 0.2.3**: Use Harvester version ``0.2.2``.
- **Version 0.2.2**: Resolves issue `#5 <https://github.com/genicam/harvesters_gui/issues/7>`_.
- **Version 0.2.1**: Works with Harvester versions >= ``0.2.1``.
- **Version 0.2.0**: Works with Harvester versions >= ``0.2.0``.
- **Version 0.1.0**: Note that this version will be deprecated and the following versions will be incompatible with any of ``0.1.n`` versions.

**************
External links
**************

* `Harvester <https://github.com/genicam/harvesters>`_: Image acquisition front-end library
* `PyPI <https://pypi.org/project/harvesters/>`_: This is the package distribution page of Harvester which is located in PyPI
* `Read the Docs <https://harvesters.readthedocs.io/en/latest/>`_: You can find the API reference of Harvester and Harvester GUI

############
Installation
############

In this section, we will learn how to instruct procedures to get Harvester work.

*******************
System Requirements
*******************

The following software modules are required to get Harvester working:

* Python>=3.5,<3.9

In addition, you will need the following items to let Harvester make something meaningful:

* GenTL Producers
* GenICam compliant machine vision cameras

************************
Installing Harvester GUI
************************

If you want to use Harvester GUI, then please invoke the following command:

.. code-block:: shell

    $ pip install harvesters_gui

Note that ``PyQt5`` is distributed under LGPL and it may not be ideal for your purpose. In the future, we might support other GUI frameworks which are more or less open and free.

***********************
Launching Harvester GUI
***********************

To launch Harvester GUI, let's create a Python script file, naming ``harvester.py``, that contains the following code:

.. code-block:: python

    import sys
    from PyQt5.QtWidgets import QApplication
    from harvesters_gui.frontend.pyqt5 import Harvester

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        h = Harvester()
        h.show()
        sys.exit(app.exec_())

Then launch ``harvester.py``:

.. code-block:: shell

    $ python path/to/harvester.py

You will see Harvester GUI pops up.

###########################
How does Harvester GUI us?
###########################

Harvester GUI works on the top of Harvester and offers you high-performance image data visualization on the fly. It involves VisPy for controlling OpenGL functionality and PyQt for providing GUI.

The main features of Harvester GUI are listed as follows:

* Image data visualization of the acquired images
* Image magnification using a mouse wheel or a trackpad
* Image dragging using a mouse or a trackpad
* An arbitrary selection of image displaying point in the data path (Not implemented yet)

Unlike Harvester, Harvester GUI limits the number of GenTL Producers to load just one. This is just a limitation to not make the GUI complicated. In general, the user should know which GenTL Producer should be loaded to control his target remote device. It's not necessary to load multiple GenTL Producers for this use case. However, this is just an idea in an early stage. We might support multiple loading on even Harvester GUI in the future.

###########
Screenshots
###########

In this section, we see some useful windows which Harvester GUI offers you.

****************************
Image data visualizer window
****************************

The image data visualizer window (below) offers you a visualization of the acquired images. In this screenshot, Harvester is acquiring a 4000 x 3000 pixel of RGB8 image at 30 fps; it means it's acquiring images at 8.6 Gbps. It's quite fast, isn't it?

.. image:: https://user-images.githubusercontent.com/8652625/43035346-c84fe404-8d28-11e8-815f-2df66cbbc6d0.png
    :align: center
    :alt: Image data visualizer

***************************
Attribute controller window
***************************

The attribute controller window (below) offers you to manipulate GenICam feature nodes of the target remote device. Changing exposure time, triggering the target remote device for image acquisition, storing a set of camera configuration so-called User Set, etc, you can manually control the target remote device anytime when you want to. It supports the visibility filter feature and regular expression feature. These features are useful in a case where you need to display only the features you are interested in.

.. image:: https://user-images.githubusercontent.com/8652625/43035351-d35a2936-8d28-11e8-83d5-7b6efa6e2ad8.png
    :align: center
    :alt: Attribute Controller

###################
Using Harvester GUI
###################

****************************
Image data visualizer window
****************************

Image data visualizer window :: Toolbar
=======================================

Most of Harvester GUI's features can be used through its toolbox. In this section, we describe each button's functionality and how to use it. Regarding shortcut keys, replace ``Ctrl`` with ``Command`` on macOS.

.. image:: https://user-images.githubusercontent.com/8652625/43035384-7d1109e0-8d29-11e8-9005-38b965a9680e.png
    :align: center
    :alt: Toolbar

Selecting a CTI file
--------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596073-7e1b6a82-6273-11e8-9045-68bbbd034281.png
    :align: left
    :alt: Open file

This button is used to select a GenTL Producer file to load. The shortcut key is ``Ctrl+o``.

Updating the remote device information list
-------------------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596091-9354283a-6273-11e8-8c6f-559db511339a.png
    :align: left
    :alt: Update

This button is used to update the remote device information list; the list will be filled up with the remote devices that are handled by the GenTL Producer that you have loaded on Harvester GUI; sometime it might be empy if there's no remote device is available. The shortcut key is ``Ctrl+u``. It might be useful when you newly connect a remote device to your system.

Selecting a GenICam compliant remote device
-------------------------------------------

This combo box shows a list of available GenICam compliant remote devices. You can select a remote device that you want to control. The shortcut key is ``Ctrl+D``, i.e., ``Ctrl+Shift+d``.

Connecting a selected remote device to Harvester
------------------------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596045-49c61d54-6273-11e8-8424-d16e923b5b3f.png
    :align: left
    :alt: Connect

This button is used to connect a remote device which is being selected by the former combo box. The shortcut key is ``Ctrl+c``. Once you connect the remote device, the remote device is exclusively controlled.

Disconnecting the connecting remote device from Harvester
---------------------------------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596046-49f0fd9e-6273-11e8-83e3-7ba8aad3c4f7.png
    :align: left
    :alt: Disconnect

This button is used to disconnect the connecting remote device from Harvester. The shortcut key is ``Ctrl+d``.

Starting image acquisition
--------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596022-34d3d486-6273-11e8-92c3-2349be5fd98f.png
    :align: left
    :alt: Start image acquisition

This button is used to start image acquisition. The shortcut key is ``Ctrl+j``. The acquired images will be drawing in the following canvas pane.

Pausing/Resuming image drawing
------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596063-6cae1aba-6273-11e8-9049-2430a042c671.png
    :align: left
    :alt: Pause

This button is used to pausing/resuming drawing images on the canvas pane while it's keep acquiring images in the background. The shortcut key is ``Ctrl+k``. If you want to resume drawing images, just click the button again. You can do the same thing with the start image acquisition button (``Ctrl+j``).

Stopping image acquisition
--------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596024-35d84c86-6273-11e8-89b8-9368db740f22.png
    :align: left
    :alt: Stop image acquisition

This button is used to stop image acquisition. The shortcut key is ``Ctrl+l``.

Showing the remote device attribute dialog
------------------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596224-7b2cf0e2-6274-11e8-9088-bb48163968d6.png
    :align: left
    :alt: Device attribute

This button is used to show the remote device attribute dialog. The shortcut key is ``Ctrl+a``. The remote device attribute dialog offers you to a way to intuitively control remote device attribute over a GUI.

Showing the about dialog
------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596039-449ddc36-6273-11e8-9f91-1eb7830b8e8c.png
    :align: left
    :alt: About

This button is used to show the about dialog.

Image data visualizer window :: Canvas
======================================

The canvas of Harvester GUI offers you not only image data visualization but also some intuitive object manipulations.

.. image:: https://user-images.githubusercontent.com/8652625/43035349-cdd9f9a0-8d28-11e8-8152-0bc488450ef6.png
    :align: center
    :alt: Canvas

Zooming into the displayed image
--------------------------------

If you're using a mouse, spin the wheel to your pointing finger points at. If you are using a trackpad on a macOS, slide two fingers to the display side.

Zooming out from the displayed image
------------------------------------

If you're using a mouse, spin the wheel to your side. If you are using a trackpad on a macOS, slide two fingers to your side.

Changing the part being displayed
---------------------------------

If you're using a mouse, grab any point in the canvas and drag the pointer as if you're physically grabbing the image. The image will follow the pointer. If you are using a trackpad on a macOS, it might be useful if you assign the three finger slide for dragging.

***************************
Attribute controller window
***************************

The attribute controller offers you an interface to each GenICam feature node that the the target remote device provides.

Attribute controller window :: Toolbar
======================================

.. image:: https://user-images.githubusercontent.com/8652625/43035353-d64c96e2-8d28-11e8-8c68-0bc4ee866d28.png
    :align: center
    :alt: Toolbar

Filtering GenICam feature nodes by visibility
---------------------------------------------

This combo box offers you to apply visibility filter to the GenICam feature node tree. The shortcut key is ``Ctrl+v``

GenICam defines the following visibility levels:

* **Beginner**: Features that should be visible for all users via the GUI and API.
* **Expert**: Features that require a more in-depth knowledge of the camera functionality.
* **Guru**: Advanced features that might bring the cameras into a state where it will not work properly anymore if it is set incorrectly for the cameras current mode of operation.
* **Invisible**: Features that should be kept hidden for the GUI users but still be available via the API.

The following table shows each item in the combo box and the visibility status of each visibility level:

.. list-table::
    :header-rows: 1
    :align: center

    - - Combo box item
      - Beginner
      - Expert
      - Guru
      - Invisible
    - - Beginner
      - Visible
      - Invisible
      - Invisible
      - Invisible
    - - Expert
      - Visible
      - Visible
      - Invisible
      - Invisible
    - - Guru
      - Visible
      - Visible
      - Visible
      - Invisible
    - - All
      - Visible
      - Visible
      - Visible
      - Visible

Filtering GenICam feature nodes by regular expression
-----------------------------------------------------

This text edit box offers you to filter GenICam feature nodes by regular expression.

Expanding the feature node tree
-------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/41112454-f7471566-6ab9-11e8-93a4-d2d56c7bbd31.png
    :align: left
    :alt: Expand feature node tree

This button is used to expand the feature node tree. The shortcut key is ``Ctrl+e``.

Collapsing the feature node tree
--------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/41112453-f712498a-6ab9-11e8-9f9f-160c0e0d8866.png
    :align: left
    :alt: Collapse feature node tree

This button is used to collapse the feature node tree. The shortcut key is ``Ctrl+c``.

################
Acknowledgements
################

*********************
Open source resources
*********************

Harvester GUI uses the following open source libraries/resources:

* VisPy

  | License: `BSD 3-Clause <https://opensource.org/licenses/BSD-3-Clause>`_
  | Copyright (c) 2013-2018 VisPy developers

  | http://vispy.org
  | https://github.com/vispy/vispy

* PyQt5

  | License: `GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>`_
  | Copyright (c) 2018 Riverbank Computing Limited

  | https://www.riverbankcomputing.com
  | https://pypi.org/project/PyQt5/

* Icons8

  | License: `Creative Commons Attribution-NoDerivs 3.0 Unported <https://creativecommons.org/licenses/by-nd/3.0/>`_
  | Copyright (c) Icons8 LLC

  | https://icons8.com
