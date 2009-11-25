from zope.interface import implements

from Products.Archetypes import atapi
from Products.LinguaPlone.I18NOrderedBaseFolder import I18NOrderedBaseFolder

from slc.seminarportal.config import PROJECTNAME
from slc.seminarportal.interfaces import ISpeechVenue

class SPSpeechVenue(I18NOrderedBaseFolder):
    """ Represents a venue, hall or room where speeches are held during
        a seminar.
    """
    implements(ISpeechVenue)
    meta_type = portal_type = "SPSpeechVenue"

    _at_rename_after_creation = True


atapi.registerType(SPSpeechVenue, PROJECTNAME)

