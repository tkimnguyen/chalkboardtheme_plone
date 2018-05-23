# -*- coding: utf-8 -*-

from plone.app.theming.interfaces import IThemeSettings
from plone import api
from plonetheme.chalkboard import PORTAL_SKINS, PROJECTNAME, THEME_BASE_NAME
from plonetheme.chalkboard.logger import logger

DEFAULT_THEME_NAME = "Sunburst Theme"
ITHEMESETTINGS_CURRENT_THEME = 'plone.app.theming.interfaces.IThemeSettings.currentTheme'
ITHEMESETTINGS_THEME_STATUS = 'plone.app.theming.interfaces.IThemeSettings.enabled'

def remove_theme_skin(portal):
    """Remove Theme base skin and Diazo theme"""
    skins_tool = api.portal.get_tool(PORTAL_SKINS)
    current_diazo_theme = api.portal.get_registry_record(ITHEMESETTINGS_CURRENT_THEME)
    theme_enabled = api.portal.get_registry_record(ITHEMESETTINGS_THEME_STATUS)
    
    if THEME_BASE_NAME in skins_tool.default_skin:
        # Set a reasonable default skin
        skins_tool.default_skin = DEFAULT_THEME_NAME
        logger.info('{0} skin disabled; default skin set to {1}'.format(THEME_BASE_NAME, DEFAULT_THEME_NAME,))

    # Custom settings for plone.app.theming
    if PROJECTNAME in current_diazo_theme:
        api.portal.set_registry_record('plone.app.theming.interfaces.IThemeSettings.absolutePrefix', u'')
        api.portal.set_registry_record(ITHEMESETTINGS_CURRENT_THEME, u'')
        api.portal.set_registry_record('plone.app.theming.interfaces.IThemeSettings.rules', u'')
        if theme_enabled:
            api.portal.set_registry_record(ITHEMESETTINGS_THEME_STATUS, False)
        logger.info('{0} diazo theme disabled'.format(PROJECTNAME,))

    logger.info('{0} skin and {1} diazo theme are disabled'.format(THEME_BASE_NAME, PROJECTNAME,))


def uninstall(portal, reinstall=False):
    """Uninstall by cleaning up portal_skins"""

    if not reinstall:
        remove_theme_skin(portal)
        profile = 'profile-{0}:uninstall'.format(PROJECTNAME)
        setup_tool = api.portal.get_tool('portal_setup')
        setup_tool.runAllImportStepsFromProfile(profile)
        return 'Ran all uninstall steps.'
