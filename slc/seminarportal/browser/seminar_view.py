from zope.interface import implements

from DateTime import DateTime

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

from interfaces import ISeminarView

class SeminarView(BrowserView):
    """ Helper functionality for displaying a roster of speeches at a
        Seminar.
    """
    implements(ISeminarView)

    def get_datetime(self, date):
        """ Returns DateTime object
        """
        return DateTime(date)
        
    def get_venues(self):
        """ Return brains for SpeechVenue objects in context 
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='SPSpeechVenue', 
                         path='/'.join(self.context.getPhysicalPath()),
                         sort_on='getObjPositionInParent',)
        return list(brains)
 
    def get_roster(self, venues=[]):
        """ Return a dict of {date:{venue_id:{time:[speeches]}}}
        """
        d = {}
        catalog = getToolByName(self.context, 'portal_catalog')
        venues = venues or self.get_venues()
        for venue in venues:
            venue_id = venue.id
            speeches = catalog(portal_type='SPSpeech', 
                               path='%s/speech-venues/%s' % ('/'.join(self.context.getPhysicalPath()), venue_id))
            for speech in speeches:
                date = speech.start.Date()
                time = speech.start
                if d.has_key(date):
                    if d[date].has_key(venue_id):
                        if d[date][venue_id].has_key(time):
                            d[date][venue_id][time].append(speech)
                        else:
                            d[date][venue_id][time] = [speech]
                    else:
                        d[date][venue_id] = {time:[speech]}
                else:
                    d[date] = {venue_id:{time:[speech]}}
        return d

    def get_event_summary(self, venues=[]):
        """ Return a dict of {date:[(time, speech)]}
        """
        d = {}
        catalog = getToolByName(self.context, 'portal_catalog')
        venues = venues or self.get_venues()
        for venue in venues:
            speeches = catalog(portal_type='SPSpeech', 
                               path='%s/speech-venues/%s' % ('/'.join(self.context.getPhysicalPath()), venue.id))
            for speech in speeches:
                date = speech.start.Date()
                time = speech.start
                if d.has_key(date):
                    d[date].append((time, speech.getPath(), speech))
                else:
                    d[date] = [(time, speech.getPath(), speech)]
        return d
        

    def get_day_times(self, roster={}):
        """ Return a dictionary of {seminar_day_date:[speech_time]}
        """
        roster = roster or self.get_roster()
        day_times = {}
        for day in roster.keys():
            times = []
            d = {} # Dict used to enforece uniqueness
            for venue_id in roster[day].keys():
                for t in roster[day][venue_id].keys():
                    d[t] = 'dummy'

            day_times[day] = sorted(d.keys())

        return day_times 

    def get_files_and_images(self):
        """ Return a list of files and images in current context
        """
        return self.context.objectValues(['ATFile', 'ATImage'])

    def get_speechvenues(self):
        """ Return speech venues in current context
        """
        return self.context.objectValues(['SPSpeechVenue'])

    def get_speeches(self):
        """ Return speeches in current context
        """
        return self.context.objectValues(['SPSpeech'])
        

