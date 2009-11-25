from Products.Archetypes.interfaces import IObjectInitializedEvent
from Products.Archetypes.utils import shasattr
from Products.CMFCore.utils import getToolByName

from slc.seminarportal.content.speakersfolder import SPSpeakersFolder
from slc.seminarportal.content.speechvenuefolder import SPSpeechVenueFolder
from slc.seminarportal.interfaces import ISeminar

class SeminarEvents:
    """ Event Subscriber for the SPSeminar object type """

    def __call__(self, obj, event, **kw):
        """ Called by the event system """
        if ISeminar.providedBy(obj):
            if IObjectInitializedEvent.providedBy(event):
                self.objectInitialized(obj, **kw)
    
    def objectInitialized(self, seminar, **kw):
        """ Create Speakers and Speeches folder inside the seminar after
            creation.
        """
        for fid, title, type, subtype in (('speakers', 'Speakers', SPSpeakersFolder, 'SPSpeaker',), 
                                 ('speech-venues', 'Speech Venues', SPSpeechVenueFolder, 'SPSpeechVenue',)):
            
            if shasattr(seminar, fid):
                continue

            seminar._setObject(fid, type(fid))
            folder = getattr(seminar, fid)
            folder.setTitle(title)
            folder.setConstrainTypesMode(1)
            folder.setImmediatelyAddableTypes([subtype])
            folder.setLocallyAllowedTypes([subtype])
            wftool = getToolByName(seminar, 'portal_workflow')
            wftool.doActionFor(folder, 'publish')


event_subscriber = SeminarEvents()

