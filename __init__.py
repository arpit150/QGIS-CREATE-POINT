# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CreatePoint
                                 A QGIS plugin
 this plugin is create point.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-05-22
        copyright            : (C) 2020 by arpit srivastava
        email                : arpitvk99@gmail.com
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
    """Load CreatePoint class from file CreatePoint.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Create_Point import CreatePoint
    return CreatePoint(iface)