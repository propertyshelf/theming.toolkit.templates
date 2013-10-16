# -*- coding: utf-8 -*-

"""Test Layer theming.toolkit.templates"""

# zope imports
from plone.app.testing import (
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from zope.configuration import xmlconfig


class ToolkitTemplates(PloneSandboxLayer):
    """Custom Test Layer for theming.toolkit.templates"""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import theming.toolkit.templates
        xmlconfig.file('configure.zcml',
                       theming.toolkit.templates,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'theming.toolkit.templates:default')


TOOLKIT_TEMPLATES_FIXTURE = ToolkitTemplates()
TOOLKIT_TEMPLATES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TOOLKIT_TEMPLATES_FIXTURE, ),
    name="ToolkitTemplates:Integration")
