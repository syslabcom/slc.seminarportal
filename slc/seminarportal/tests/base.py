from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup 
from slc.seminarportal.config import PRODUCT_DEPENDENCIES

@onsetup
def setup_slc_seminarportal():
    """Set up the additional products required for slc.seminarportal
    
    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """
    fiveconfigure.debug_mode = True
    import slc.seminarportal
    zcml.load_config('configure.zcml', slc.seminarportal)
    fiveconfigure.debug_mode = False
    
    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML.
    for dependency in PRODUCT_DEPENDENCIES:
        ztc.installProduct(dependency)

    ztc.installPackage('slc.seminarportal')


setup_slc_seminarportal()
ptc.setupPloneSite(products=['slc.seminarportal'])

class SeminarPortalTestCase(ptc.PloneTestCase):
    """Base class used for test cases
    """
       
class SeminarPortalFunctionalTestCase(ptc.FunctionalTestCase):
    """Test case class used for functional (doc-)tests
    """


