from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

from slc.seminarportal.config import names

ztc.installProduct('Relations')
ztc.installProduct('slc.seminarportal')

PRODUCTS = ['Relations', 'slc.seminarportal']
ptc.setupPloneSite(products=PRODUCTS)
class SeminarPortalTestCase(ptc.PloneTestCase):
    """Base class used for test cases
    """
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            import slc.seminarportal
            zcml.load_config('configure.zcml', slc.seminarportal)
            fiveconfigure.debug_mode = False
            ztc.installProduct('Relations')
            ztc.installPackage('slc.seminarportal');


    # Some helper methods

    def create_speakers(self, seminar):
        """ Create test speakers
        """
        speakers_folder = getattr(seminar, 'speakers')
        for surname, firstname in names:
            speaker_id = seminar.generateUniqueId('SPSpeaker')
            speakers_folder.invokeFactory('SPSpeaker', 
                                speaker_id,)
            s = getattr(speakers_folder, speaker_id)
            s._renameAfterCreation(check_auto_id=True)
            s.setLastName(surname)
            s.setFirstName(firstname)



