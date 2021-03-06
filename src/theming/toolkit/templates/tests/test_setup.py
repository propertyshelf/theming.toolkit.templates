# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (c) 2013 Propertyshelf, Inc. and its Contributors.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AS IS AND ANY EXPRESSED OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
###############################################################################
"""Test Setup of theming.toolkit.templates"""

# python imports
import unittest2 as unittest

# zope imports
from Products.CMFCore.utils import getToolByName
from plone.browserlayer import utils as layerutils

# local imports
from theming.toolkit.templates.browser.interfaces import IToolkitTemplates
from theming.toolkit.templates.testing import (TOOLKIT_TEMPLATES_INTEGRATION_TESTING,
)


class TestSetup(unittest.TestCase):
    """Setup Test Case for toolkit.color."""
    layer = TOOLKIT_TEMPLATES_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """Test that the product is installed."""
        self.assertTrue(self.qi_tool.isProductInstalled(
            'theming.toolkit.templates'))

    def test_browserlayer(self):
        """Test that the browserlayer is registered."""
        self.assertIn(IToolkitTemplates, layerutils.registered_layers())

    def test_dependency_diazotheme_bootstrap(self):
        """Test if diazotheme.bootstrap is installed as dependency"""
        self.assertTrue(self.qi_tool.isProductInstalled(
            'diazotheme.bootstrap'))
