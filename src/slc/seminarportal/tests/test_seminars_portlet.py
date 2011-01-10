import logging
import random

from zope import event
from zope import component

from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletType
from plone.portlets.interfaces import IPortletRenderer

from plone.app.portlets.storage import PortletAssignmentMapping

from Products.Archetypes.event import ObjectInitializedEvent

from slc.seminarportal.tests.base import SeminarPortalTestCase
from slc.seminarportal.portlets import seminar as seminar_portlet

log = logging.getLogger('test_seminar_portlet.py')

class TestPortlet(SeminarPortalTestCase):

    def afterSetUp(self):
        self.loginAsPortalOwner()

    def test_portlet_registered(self):
        portlet = component.getUtility(IPortletType, name="slc.SeminarPortlet")
        self.assertEquals(portlet.addview, "slc.SeminarPortlet")

    def test_portlet_interfaces(self):
        portlet = seminar_portlet.Assignment()
        self.failUnless(IPortletAssignment.providedBy(portlet))
        self.failUnless(IPortletDataProvider.providedBy(portlet.data))

    def test_invoke_addview(self):
        portlet = component.getUtility(IPortletType, name='slc.SeminarPortlet')
        mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')
        for m in mapping.keys():
            del mapping[m]
        addview = mapping.restrictedTraverse('+/' + portlet.addview)

        addview.createAndAdd(data={})

        self.assertEquals(len(mapping), 1)
        self.failUnless(isinstance(mapping.values()[0], seminar_portlet.Assignment))

    def test_invoke_edit_view(self):
        mapping = PortletAssignmentMapping()
        request = self.folder.REQUEST

        mapping['foo'] = seminar_portlet.Assignment()
        editview = component.getMultiAdapter((mapping['foo'], request), name='edit')
        self.failUnless(isinstance(editview, seminar_portlet.EditForm))

    def test_renderer(self):
        context = self.folder
        request = self.folder.REQUEST
        view = self.folder.restrictedTraverse('@@plone')

        manager = component.getUtility(
                                IPortletManager, 
                                name='plone.rightcolumn', 
                                context=self.portal
                                )

        assignment = seminar_portlet.Assignment()

        renderer = component.getMultiAdapter(
                                (context, request, view, manager, assignment), 
                                IPortletRenderer
                                )

        self.failUnless(isinstance(renderer, seminar_portlet.Renderer))


class TestRenderer(SeminarPortalTestCase):
    
    def afterSetUp(self):
        """ Create a Seminar object, and call the relevant event to enable the
            auto-creation of the sub-objects ('speakers', 'speech venues').
        """
        self.loginAsPortalOwner()
        portal = self.portal
        qi = portal.portal_quickinstaller
        portal.invokeFactory('SPSeminar', 'plone-conference', title="Seminar")
        seminar = getattr(portal, 'plone-conference')
        seminar._renameAfterCreation(check_auto_id=True)
        event.notify(ObjectInitializedEvent(seminar))
        self.create_speakers(seminar)
        self.seminar = seminar


    def renderer(self, context=None, request=None, view=None, manager=None, assignment=None):
        context = context or self.folder
        request = request or self.folder.REQUEST
        view = view or self.folder.restrictedTraverse('@@plone')
        manager = manager or component.getUtility(IPortletManager, 
                                        name='plone.rightcolumn', 
                                        context=self.portal)
        assignment = assignment or seminar_portlet.Assignment()
        return component.getMultiAdapter((context, request, view, manager, assignment), 
                               IPortletRenderer)


    def test_get_speakers(self):
        """ """
        speakers = self.seminar.speakers.objectValues()
        speakers_urls = ['/'.join(s.getPhysicalPath()) for s in speakers]

        # Test random:
        for count in random.sample(range(0, 10), 5):
            assignment = seminar_portlet.Assignment(
                                                speakers=[],
                                                count=count,
                                                random=1,
                                                )

            r = self.renderer(
                        context=self.portal, 
                        assignment=assignment,
                        )

            speakers = r.get_speakers()

            self.assertEquals(len(speakers), count)
            for speaker in speakers:
                self.assertEquals(speaker.portal_type, 'SPSeminar')

            speakers_paths = ['/'.join(s.getPhysicalPath()) for s in speakers]
            for s in speakers_paths:
                self.assertEquals(s in speakers_urls, True)

        # Test with specified:
        count = 5
        assignment = seminar_portlet.Assignment(
                                            speakers=speakers_urls[:5],
                                            count=count,
                                            random=0,
                                            )

        r = self.renderer(
                    context=self.portal, 
                    assignment=assignment,
                    )

        speakers = r.get_speakers()
        # The speakers 
        speakers_paths = ['/'.join(s.getPhysicalPath()) for s in speakers]

        self.assertEquals(len(speakers), count)

        for s in speakers_paths:
            self.assertEquals(s in speakers_urls, True)



def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestPortlet))
    suite.addTest(makeSuite(TestRenderer))
    return suite

