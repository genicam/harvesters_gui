.. image:: https://img.shields.io/pypi/v/harvesters.svg
    :target: https://pypi.org/project/harvesters

.. image:: https://readthedocs.org/projects/harvesters/badge/?version=latest
    :target: https://harvesters.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/pypi/pyversions/harvesters.svg

----

*Even though we just wanted to research image processing algorithms, why did we have to change our image acquisition library every time we change the camera that we use for the research?
- Anonymous*

----

.. contents:: Table of Contents
    :depth: 2

###############
About Harvester
###############

Harvester was created to be a friendly image acquisition library for all people who those want to learn computer/machine vision. Harvester consists of two Python libraries, Harvester Core and Harvester GUI, and technically speaking, each library is responsible for the following tasks:

Harvester Core:

- Image acquisition
- Device manipulation

Harvester GUI:

- Image data visualization

Harvester consumes image acquisition libraries, so-called GenTL Producers. Just grabbing a GenTL Producer and GenICam compliant machine vision cameras, then Harvester will supply you the acquired image data as `numpy <http://www.numpy.org>`_ array to make your image processing task productive.

You can freely use, modify, distribute Harvester under `Apache License-2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_ without worrying about the use of your software: personal, internal or commercial.

Currently, Harvester is being developed by the motivated contributors from all over the world.

***********************
Where is the name from?
***********************

Harvester's name was coming from the great Flemish painter, Pieter Bruegel the Elder's painting so-called "The Harvesters". Harvesters harvest a crop every season that has been fully grown and the harvested crop is passed to the consumers. On the other hand, image acquisition libraries acquire images as their crop and the images are passed to the following processes. We found the similarity between them and decided to name our library Harvester.

Apart from anything else, we love its peaceful and friendly name. We hope you also like it ;-)

.. figure:: https://user-images.githubusercontent.com/8652625/40595190-1e16e90e-626e-11e8-9dc7-207d691c6d6d.jpg
    :align: center
    :alt: The Harvesters

    Pieter Bruegel the Elder, The Harvesters, 1565, (c) 2000–2018 The Metropolitan Museum of Art

****************
Asking questions
****************

We have prepared a chat room in Gitter. Please don't hesitate to drop your message when you get a question regarding Harvester!

https://gitter.im/genicam-harvester/chatroom

**************
External links
**************

* `GitHub <https://github.com/genicam/harvesters>`_: This is the main repository of Harvester
* `Harvester Core <https://github.com/genicam/harvesters>`_: Image acquisition front-end library with Python
* `PyPI <https://pypi.org/project/harvesters/>`_: This is the package distribution page of Harvester which is located in PyPI
* `Read the Docs <https://harvesters.readthedocs.io/en/latest/>`_: You can find the API reference of Harvester Core and Harvester GUI

###########
Terminology
###########

Before start talking about the detail, let's take a look at some important terminologies that frequently appear in this document. These terminologies are listed as follows:

* **The GenApi-Python Binding**: A Python module that communicates with the GenICam reference implementation.

* **A GenTL Producer**: A library that has C interface and offers consumers a way to communicate with cameras over physical transport layer dependent technology hiding the detail from the consumer.

* **The GenTL-Python Binding**: A Python module that communicates with GenTL Producers.

* **Harvester**: A Python module that consists of Harvester Core and Harvester GUI.

* **Harvester Core**: A part of Harvester that works as an image acquisition engine.

* **Harvester GUI**: A part of Harvester that works as a graphical user interface of Harvester Core.

* **A GenICam compliant device**: It's typically a camera. Just involving the GenICam reference implementation, it offers consumers a way to dynamically configure/control the target devices.

The following diagram shows the hierarchy and relationship of the relevant modules:

.. figure:: https://user-images.githubusercontent.com/8652625/44316633-926cf100-a467-11e8-92c6-ac69ad3c8129.png
    :align: center
    :alt: Module hierarchy

############
Installation
############

In this section, we will learn how to instruct procedures to get Harvester work.

*******************
System Requirements
*******************

The following software modules are required to get Harvester working:

* Either of Python 3.4, 3.5, 3.6, or 3.7

In addition, you will need the following items to let Harvester make something meaningful:

* GenTL Producers
* GenICam compliant machine vision cameras

***************************
Supported operating systems
***************************

Harvester has been tested with the following operating systems:

* macOS 10.13
* Ubuntu 14.04
* Red Hat Enterprise Linux Workstation 7.4
* Windows 7

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

Harvester GUI works on the top of Harvester Core and offers you high-performance image data visualization on the fly. It involves VisPy for controlling OpenGL functionality and PyQt for providing GUI.

The main features of Harvester GUI are listed as follows:

* Image data visualization of the acquired images
* Image magnification using a mouse wheel or a trackpad
* Image dragging using a mouse or a trackpad
* An arbitrary selection of image displaying point in the data path (Not implemented yet)

Unlike Harvester Core, Harvester GUI limits the number of GenTL Producers to load just one. This is just a limitation to not make the GUI complicated. In general, the user should know which GenTL Producer should be loaded to control his target device. It's not necessary to load multiple GenTL Producers for this use case. However, this is just an idea in an early stage. We might support multiple loading on even Harvester GUI in the future.

*****************************************
Pixel formats that Harvester GUI supports
*****************************************

Currently, Harvester GUI supports the following pixel formats that are defined by the Pixel Format Naming Convention:

    ``Mono8``, ``Mono10``, ``Mono12``, ``Mono16``, ``RGB8``, ``RGBa8``, ``BayerRG8``, ``BayerGR8``, ``BayerBG8``, ``BayerGB8``, ``BayerRG16``, ``BayerGR16``, ``BayerBG16``, ``BayerGB16``

Note that Harvester GUI has not yet supported demosaicing.

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

The attribute controller window (below) offers you to manipulate GenICam feature nodes of the target device. Changing exposure time, triggering the target device for image acquisition, storing a set of camera configuration so-called User Set, etc, you can manually control the target device anytime when you want to. It supports the visibility filter feature and regular expression feature. These features are useful in a case where you need to display only the features you are interested in.

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

Updating the device information list
------------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596091-9354283a-6273-11e8-8c6f-559db511339a.png
    :align: left
    :alt: Update

This button is used to update the device information list; the list will be filled up with the devices that are handled by the GenTL Producer that you have loaded on Harvester GUI; sometime it might be empy if there's no device is available. The shortcut key is ``Ctrl+u``. It might be useful when you newly connect a device to your system.

Selecting a GenICam compliant device
------------------------------------

This combo box shows a list of available GenICam compliant devices. You can select a device that you want to control. The shortcut key is ``Ctrl+D``, i.e., ``Ctrl+Shift+d``.

Connecting a selected device to Harvester
-----------------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596045-49c61d54-6273-11e8-8424-d16e923b5b3f.png
    :align: left
    :alt: Connect

This button is used to connect a device which is being selected by the former combo box. The shortcut key is ``Ctrl+c``. Once you connect the device, the device is exclusively controlled.

Disconnecting the connecting device from Harvester
--------------------------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596046-49f0fd9e-6273-11e8-83e3-7ba8aad3c4f7.png
    :align: left
    :alt: Disconnect

This button is used to disconnect the connecting device from Harvester. The shortcut key is ``Ctrl+d``.

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

Showing the device attribute dialog
-----------------------------------

.. image:: https://user-images.githubusercontent.com/8652625/40596224-7b2cf0e2-6274-11e8-9088-bb48163968d6.png
    :align: left
    :alt: Device attribute

This button is used to show the device attribute dialog. The shortcut key is ``Ctrl+a``. The device attribute dialog offers you to a way to intuitively control device attribute over a GUI.

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

The attribute controller offers you an interface to each GenICam feature node that the the target device provides.

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
