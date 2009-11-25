from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from slc.seminarportal import seminarportalMessageFactory as _

class IThemeLayer(Interface):
    """Marker Interface used by BrowserLayer
    """

class ISeminar(Interface):
    """A Seminar 
    """

class ISpeechVenue(Interface):
    """A Speech 
    """

class ISpeech(Interface):
    """A Speech 
    """

class ISpeaker(Interface):
    """A Speaker 
    """

class ISpeakersFolder(Interface):
    """A Speaker Folder
    """

class ISpeechVenueFolder(Interface):
    """A Speech Venue Folder
    """

