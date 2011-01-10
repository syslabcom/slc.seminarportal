from zope.component import getMultiAdapter
from plone.memoize import ram
from plone.memoize.compress import xhtml_compress
from plone.app.portlets.portlets import base
from Products.CMFCore.utils import getToolByName

class BaseRenderer(base.Renderer):

    def __init__(self, *args):
        super(BaseRenderer, self).__init__(*args)

        portal_languages = getToolByName(self.context, 'portal_languages')
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')

        self.portal = portal_state.portal()
        self.navigation_root_path = portal_state.navigation_root_path()
        self.navigation_root = self.portal.restrictedTraverse(self.navigation_root_path)
        self.navigation_root_url = portal_state.navigation_root_url()

    def _render_cachekey(method, self):
        """ Renders a cachekey to be used by the portlets.
        """
        preflang = getToolByName(self.context, 'portal_languages').getPreferredLanguage()
        return (preflang, self.navigation_root_path)
        
    @ram.cache(_render_cachekey)
    def render(self):
        return xhtml_compress(self._template())

