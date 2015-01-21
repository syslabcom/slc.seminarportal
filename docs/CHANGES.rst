Changelog
*********

1.4.9 (unreleased)
------------------

- Nothing changed yet.


1.4.8 (2015-01-21)
------------------

- Enable quickupload for seminars #10902 [reinhardt]

1.4.7 (2013-11-04)
------------------

- Bugfix: add missing scale "icon" for image on speaker, which was referenced in
  the speech view [pysailor]
- Bugfix: in the speakersfolder view, we must reference images and create links
  using the absolute_url [pysailor]


1.4.6 (2013-05-14)
------------------

- make speakers overlay narrower [jcerjak]
- move javascript resources to jsregistry [jcerjak]


1.4.5 (2012-09-17)
------------------

WARNING: Plone4 fixes which attemps to keep Plone3 compatibility, 
  but without testing done on plone3, please test before trying to
  use this version in a plone3 environment, or stick to the previous
  versions since all of the changes in this version are only to fix
  the package for Plone4.

- Updated Plone4 branch with the changes to 1.4.4 plus the following changes
  marked with [ichimdav]
- Use subject field in session_view instead of Event Type since in 
  plone 4 the archetype field for event Type is named subject [ichimdav]
- Condition the use of document_actions since in Plone4 it is a viewlet
  [ichimdav]
- Defined lots of plone helpers that are no longer available in main_template
  [ichimdav]
- Used self.request instead of self.context.request to make it compatible 
  with Plone4 and Plone3 [ichimdav]
- Removed tab index since it is no longer present in Plone4 [ichimdav]
- Fixed search portlets [ichimdav]

1.4.4 (2011-12-05)
------------------

- No changes yet

1.4.3 (2011-12-05)
------------------

- Adding jQuery/fancybox overlay for the speaker details [deroiste]
  #2552

1.4.2 (2011-11-09)
------------------

- Bugfix for the speakers portlet: eliminate duplicates #3896 [thomasw]
- Fixed the problem of testing views registered to a layer. We just let
  the request provide that layer's interface. [jcbrand]


1.4.1 (2011-03-31)
------------------

- Bugfix in the speakers portlet, re-added path as parameter for _render_cachekey,
  otherwise it's impossible to show speakers from the current seminar only,
  when there's more than one seminar; fixes #2889 [thomasw]
- The SPSpeaker content type has a new label and description for its description
  field to indicate that it's only for SEO purposes. [jcbrand]

1.4.0 (2011-02-21)
------------------

- Speakers portlet: if the "only speakers from current seminar" option is selected
  and less speakers than the maximum number are found, display them in
  alphabetical order rather than randomly [thomasw]

1.4b3 (2011-01-13)
------------------

- Removed a superfluous template [jcbrand]
- Changed some more string domains to plone where applicable [jcbrand]


1.4b2 (2011-01-12)
------------------

- Made the speaker portlet's strings i18n aware and updated the .po files [jcbrand]
- Fixed bug in the speaker portlet's view code [jcbrand]


1.4b1 (2011-01-12)
------------------

- Created a new portlet which shows upcoming seminars [jcbrand]
- Consolidated the browserviews into views.py [jcbrand]
- Consolidated the different templates [jcbrand]
- Backported changes from osha to templates/seminarfolder_view.pt and changed
  its registered name to @@seminars-view [jcbrand]
- Added a custom viewlet manager to allow header customizations for @@seminars-view [jcbrand]
- Customized @@seminars-view to also be able to show past seminars. [jcbrand]
- Updated the .pot file and merged with all the .po files. [jcbrand]
- Wrote new tests [jcbrand]


1.3.5 (2010-12-15)
------------------

- Added translations for days of week and 2 headings, provided by EU-OSHA
  refs #1557, #2048 [thomasw]

1.3.4 (2010-11-26)
------------------

- Bugfix in the speech_view for the print view [thomasw]


1.3.3 (2010-11-24)
------------------

- Give an id to the div that displays "Add to calendar" on the speech so that
  we can hide it via CSS [thomasw]


1.3.2 (2010-11-04)
------------------

- Added several missing i18n / translation statements [thomasw]
- Added new msgids [thomasw]
- Show dates in localised format [thomasw]

1.3.1 (2010-10-21)
------------------

- Added translations in 21 European languages, provided by EU-OSHA
  [thomasw]

1.3.0 (2010-10-05)
------------------

- Added lots of i18n stuff, added a locales dir and pot file [thomasw]

1.3.0b1 (2010-09-12)
--------------------

WARNING: This release will probably break existing installations!

- Implemented Language fallback for attachments #1506
- Attachment fields from schema-extender are no longer considered.
- speaker view is now also a BrowserView
- Seminar view: replaced fieldset with div to sqash printing bug (jquery
  and fieldset apperently don't get along)
- exclude speakers and speech-venues folder from nav #1506 upon creation
- removed LinguaPlone awareness from speaker and speakers-folder
- Seminar: bugfix for the custom setLanguage() method. Passing the corect value
  instead of 'self' now.
- Speech: added custom setLanguage() to prevent AlreadyTrnaslated error from LP 2.2
- Featured Speakers portlet: added an option to display only Speakers from the
  current Seminar.
  WARNING: This will break all existing portlet instances, you'll have to re-create them [thomasw]


1.2.15 (2010-08-25)
-------------------

- In "Featured speakers" portlet, I replaced field name "speakers" with
  "featured_speakers". Reason: in a seminar, we also have a folder called
  "speakers". The code in zope.app.form.browser.itemswidget.OrderedMultiSelectWidget
  in selected() tries to get all values for the field by checking if self.context
  .context has an attr named like the field -> the SPSpeakers folder is found,
  and mayhem follows (= cannot add the portlet inside a seminar) [thomasw]
- add path to _render_cachekey of speakers portlet; make it possible to have more
  than one in the site [thomasw]
- Hide "Add new XXX" buttons for anonymous on speeches, speakers and speech-
  venues folders [thomasw]
- corrected a typo in the GS for Speech FTI, wrong view name [thomasw]


1.2.14 (2010-07-22)
-------------------

- bugfix in views for speakers-, speeches- and speech-venues folders: don't
  show border to anonymous users [thomasw]

1.2.13 (2010-06-09)
-------------------

- Fixed a bug in the speakers portlet, for the case when less speakers were
  found in the catalog than the maximun set number [thomasw]
- Fixed a bug in the seminar view: Mustn't show the border to anonymous
  users [thomasw]

1.2.12 (2010-03-19)
-------------------

- Fixed the bug which prevented you from creating 'speakers' porlets inside
  seminars. [jcbrand]


1.2.11 (2009-12-07)
-------------------

- Show files and images uploaded inside speeches as attachments [jcbrand]
- Moved the speech_view skins template to a browser view [jcbrand]
- Added license information [goibhniu]


1.2.9 (2009-12-01)
------------------

- Added unit tests for the speeches portlet [jcbrand]
- In chrome et al., don't show an ugly icon on the speaker portlet if no image
  has been uploaded [jcbrand]

1.2.8 (2009-11-28)
------------------

- Changed the speaker portlet to be able to show multiple speakers [jcbrand]
- Add unit tests for the speakers portlet. [jcbrand]
- Made showing the 'Hour' column on the seminar roster configurable [jcbrand]

1.2.7 (2009-11-26)
------------------

- Bugfix, also show ATBlobs in the 'Resources' table. [jcbrand]
- Show speakers in the speeches summary and fix a bug that prevented the
  description from showing. [jcbrand]
- Restrict the addable types in speech and speaker. [jcbrand]
- Show thumbnails for speakers more often. [jcbrand]

1.2.6 (2009-11-25)
------------------

- Ditto :-/ [jcbrand]


1.2.5 (2009-11-25)
------------------

- Previous release was a dud, due to svn 1.6.5 and setuptools 0.6c9 [jcbrand]

1.2.4 (2009-11-09)
------------------

- Replaced getURL with get_path [jcbrand]
- Add new view for @@speechvenuesfolder-view [jcbrand]
- Don't show empty fields on the views [jcbrand]
- Show the relatedItems widget on seminars and speakers [jcbrand]
- Updated the test-framework and added tests [jcbrand]
- Removed the custom roles [jcbrand]
- Let SPSpeechVenue subclass BaseFolder instead, to give us a description
  field. [jcbrand]
- Fixed seminar_textarea.pt template for chromium [jcbrand]

1.2.3 (2009-11-09)
------------------

- Event-handler fix: We must not publish the speakers and speech-venues folder on event
  creation, as the user might not have that permission. Rather, register a separate
  event handler that mirrors workflow changes [thomasw]
- Autoinclude seminarportal [jcbrand]
- Removed references to OSHA [jcbrand]
- Code cleanup regarding imports [jcbrand]

1.2.2 (2009-11-03)
------------------

- small fix in speech-add-helper-page [thomasw]

1.2.1 (2009-10-25)
------------------

- fixed minor css bug preventing validation [pilz]

1.2 (2009-06-17)
----------------

- Added testlayer [gerken]

1.1 (2009-05-12)
----------------

- Packaged egg [pilz]

1.0 (2008-03-31)
----------------

- Created [jcbrand]

