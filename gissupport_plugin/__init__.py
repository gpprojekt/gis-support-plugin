# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GISSupportPlugin
                                 A QGIS plugin
 Wtyczka GIS Support
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-09-03
        copyright            : (C) 2019 by GIS Support
        email                : kamil.kozik@gis-support.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GISSupportPlugin class from file GISSupportPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gissupport_plugin import GISSupportPlugin
    return GISSupportPlugin(iface)
