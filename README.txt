.. contents::

    slc.seminarportal can be used to model and present seminars and
    conferences.

    When you view a seminar, you will be presented with a roster showing all
    the rooms (venues) and the speeches held in those rooms. The roster is a
    table with the rooms as the columns and the times of the speeches as the
    rows.

    The following content types are available: 
    - Seminar
        -The Seminar is globally addable and contains all the seminar-related
        subobjets.

    - Speakers Folder
        ¯ The Speakers folder is automatically created whenever a seminar has
        been created. This folder's allowed content types are restricted to
        speakers only.

    - Speaker
        - Every conference and seminar has people holding talks, making
        presentations and giving speeches. These people are modeled with the
        speaker content type. You can add references to speeches (i.e the
        speeches held by this speaker). These references are two-way, so the
        speeches now also have references to this speaker.

    - Speech Venues Folder
        - The Speech Venues folder is also automatically created when a seminar
        is created. This folder's allowed content types are restricted to
        speech venues only.

    - Speech Venue
        - A speech venue refers to the room or conference hall in which
        speeches are held. This folder's allowed content types are restricted
        to speeches only.

    - Speech
        - A speech is a talk or presentation held at the conference and in one
        of the rooms/venues. You can add references to speakers (i.e the
        speakers who held the speech). These references are two-way, so the
        speakers now also have references to the speeches.

    Other features:
    You can add a 'layout' property on the folder containing your seminars.
    Give the value of '@@seminarfolder-view' and you will have now a special
    view for your seminars with simple and advanced search options.


.. Note!
   -----
   
   - bug tracker
   - questions/comments feedback mail

- Questions and comments to info (at) syslab (dot) com
- Report bugs at http://products.syslab.com/products/slc.seminarportal/issues



