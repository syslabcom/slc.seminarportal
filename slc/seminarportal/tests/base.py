from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from slc.seminarportal.config import PRODUCT_DEPENDENCIES

from Products.Five import fiveconfigure, zcml
from Products.PloneTestCase import layer

SiteLayer = layer.PloneSite

class SeminarPortalLayer(SiteLayer):
    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        import slc.seminarportal
        zcml.load_config('configure.zcml', slc.seminarportal)
        fiveconfigure.debug_mode = False
        for dependency in PRODUCT_DEPENDENCIES:
            ztc.installProduct(dependency)
        ztc.installPackage('slc.seminarportal')
        ptc.setupPloneSite(products=['slc.seminarportal'])
        SiteLayer.setUp()


class SeminarPortalTestCase(ptc.PloneTestCase):
    """Base class used for test cases
    """
    layer = SeminarPortalLayer

class SeminarPortalFunctionalTestCase(ptc.FunctionalTestCase):
    """Test case class used for functional (doc-)tests
    """
    layer = SeminarPortalLayer


