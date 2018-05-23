# -*- coding: utf-8 -*-

from plonetheme.chalkboard import PORTAL_SKINS, PROJECTNAME, THEME_BASE_NAME
from plonetheme.chalkboard.logger import logger
from plone import api


def enable_unstyled_theme_base(site):
    """ Enabling Unstyled Theme Base """

    try:
        skins_tool = api.portal.get_tool(PORTAL_SKINS)

        if skins_tool:
            # Set Unstyled Skin
            skins_tool.default_skin = THEME_BASE_NAME
            logger.info('Enabling Theme Base: {0}'.format(skins_tool.default_skin,))
    except AttributeError:
        pass


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('plonetheme.chalkboard_various.txt') is None:
        return

    # Add additional setup code here
    portal = api.portal.get()
    enable_unstyled_theme_base(portal)
