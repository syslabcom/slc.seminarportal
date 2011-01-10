from Acquisition import aq_inner, aq_parent
from DateTime import DateTime
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from zope.formlib import form
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from slc.seminarportal import _
from slc.seminarportal import is_osha_installed
from slc.seminarportal.portlets.base import BaseRenderer

if is_osha_installed:
    default_portlet_header = _(u"Our Events")
else:
    default_portlet_header = _(u"Seminars")

class ISeminarsPortlet(IPortletDataProvider):
    """ """
    header = schema.TextLine(
                    title=_(u"Portlet header"),
                    description=_(u"Title of the rendered portlet"),
                    default=default_portlet_header,
                    required=True
                    )
    count = schema.Int(
                    title=_(u'Number of Seminars to display'),
                    required=True,
                    default=5
                    )
    state = schema.Tuple(title=_(u"Workflow state"),
                    description=_(
                            u"You may limit the displayed Seminars to a "
                            u"specific workflow state.."),
                    default=('published', ),
                    required=True,
                    value_type=schema.Choice(
                        vocabulary="plone.app.vocabularies.WorkflowStates")
                    )
    subject = schema.Tuple(
                    title=_(u"Categories"),
                    description=_(
                            u"Pick one or more categories with which you want to filter "
                            u"Seminars."),
                    default=tuple(),
                    required=False,
                    value_type=schema.Choice(
                        vocabulary="slc.seminarportal.vocabularies.categories")
                    )

class Renderer(BaseRenderer):
    """ """
    _template = ViewPageTemplateFile('seminars.pt')

    @property
    def available(self):
        """ The portlet will not appear if there aren't any seminars to display.
        """
        return len(self._data())

    def seminars(self):
        return self._data()

    @memoize
    def _data(self):
        """ Get all SPSeminar objects that conform to the workflow state and
            category specified on the portlet.
        """
        context = aq_inner(self.context)

        # search in the navigation root of the currently selected language 
        paths = [self.navigation_root_path]
        if self.navigation_root:
            # Also search in its canonical
            canonical = self.navigation_root.getCanonical()
            if canonical is not None:
                paths.append('/'.join(canonical.getPhysicalPath()))

        # Search: Language = preferredLanguage or neutral
        preflang = getToolByName(self.context, 'portal_languages').getPreferredLanguage()
        query = dict(
                    Language=['', preflang],
                    end={'query': DateTime(), 'range': 'min'},
                    path=paths,
                    portal_type='SPSeminar',
                    review_state=self.data.state,
                    sort_limit=self.data.count,
                    sort_on='start',
                    )

        if is_osha_installed:
            # Include OSHA SEP keywords if available
            oshaview = getMultiAdapter((self.context, self.request), name=u'oshaview')
            mySEP = oshaview.getCurrentSingleEntryPoint()
            kw = ''
            if mySEP is not None:
                kw = mySEP.getProperty('keyword', '')
            if kw !='':
                query.update(Subject=kw)

        catalog = getToolByName(context, 'portal_catalog')
        return catalog(query)[:self.data.count]

    @memoize
    def calendarLink(self):
        """ Compute a link to the "closest" calendar
        """
        context = aq_inner(self.context)
        query = dict(   
                    portal_type="Folder",
                    path=self.navigation_root_path,
                    object_provides="p4a.calendar.interfaces.ICalendarEnhanced"
                    )

        catalog = getToolByName(context, 'portal_catalog')
        res = catalog(query)
        if len(res):
            calurl = None
            pathelems = 0
            for r in res:
                pe = len(r.getPath().split('/'))
                if pathelems==0 or pe < pathelems:
                    calurl = r.getURL()
                    pathelems = pe
            return calurl
        return ""

    @memoize
    def all_seminars_link(self):
        calurl = self.calendarLink()
        if calurl:
            return '%s/seminars.html' % calurl
        else:
            context = aq_inner(self.context)
            if not context.isPrincipiaFolderish:
                context = aq_parent(context)
            return '%s/seminars.html' % context.absolute_url()

    @memoize
    def prev_seminars_link(self):
        calurl = self.calendarLink()
        if calurl:
            return '%s/past_seminars.html' % calurl
        else:
            context = aq_inner(self.context)
            if not context.isPrincipiaFolderish:
                context = aq_parent(context)        
            return '%s/past_seminars.html' % context.absolute_url()


class Assignment(base.Assignment):
    implements(ISeminarsPortlet)

    def __init__(       
                self, 
                count=5, 
                state=('published', ), 
                subject=tuple(), 
                header=default_portlet_header):

        self.count = count
        self.state = state
        self.subject = subject
        self.header = header

    @property
    def title(self):
        return self.header


class AddForm(base.AddForm):
    form_fields = form.Fields(ISeminarsPortlet)
    label = _(u"Adding the Seminars Portlet")
    description = _(u"This portlet lists upcoming Seminars.")
        
    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(ISeminarsPortlet)
    label = _(u"Editing the Seminars Portlet")
    description = _(u"This portlet lists upcoming Seminars.")
