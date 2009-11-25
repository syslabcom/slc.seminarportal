import re 

from zope.app.component.hooks import getSite
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName

from slc.clicksearch.interfaces import IClickSearchConfiguration

class SpeakerVocabulary(object):
    """Vocabulary factory returning all available speakers.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        site = getSite()
        catalog = getToolByName(site, 'portal_catalog')
        items = {}
        for speaker in catalog(portal_type='SPSpeaker'):
            items[speaker.getPath()] = SimpleTerm(speaker.getPath(), speaker.getPath(), speaker.Title)

        return SimpleVocabulary(items.values())

SpeakerVocabularyFactory = SpeakerVocabulary()

