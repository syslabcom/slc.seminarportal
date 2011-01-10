from Acquisition import aq_inner
from zope.interface import implements
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from slc.seminarportal.portlets.base import BaseRenderer
from interfaces import ISearchPortlet

class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()

class Assignment(base.Assignment):
    implements(ISearchPortlet)

    @property
    def title(self):
        return u"Search for Seminars, Speakers of Speeches"


class Renderer(BaseRenderer):
    _template = ViewPageTemplateFile('search.pt')

    @memoize
    def here_url(self):
        context = aq_inner(self.context)
        return '/'.join(context.getPhysicalPath())

    @memoize
    def template_id(self):
       return '@@seminar-search'
        
    def results(self):
        return self._data()

