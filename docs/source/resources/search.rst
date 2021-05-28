Search
======

Competitive Tracker's Search is an incredibly powerful tool for users to retrieve campaign details about the mailings
sent by other organizations.  Competitive Search capabilities empowers teams with tremendous data to help with
everything from conducting market research, to industry benchmarking, and sales enablement.  There are numerous filters
and parameters that can be applied to the search query that will quickly surface campaigns of interest.  All campaigns
sent by a domain over the past 3 days can be retrieved using the `Competitive Tracker API`_, as shown below:


.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        sendingDomain="example.com"
    )
    print(response)


Additional tips and tricks to `maximize the Advanced Search`_ in Competitive Tracker are also available in the
documentation.


.. _Competitive Tracker API: http://api.edatasource.com/docs/#/competitive
.. _maximize the Advanced Search: https://support.emailanalyst.com/en/articles/2414635-how-to-maximize-advanced-search-in-competitive-tracker


Search for Campaigns
********************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        sendingDomain="example.com"
    )


Search for Keywords in Subject and Body
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When using keywords to search, more complex queries can be structured with the following:

* Multiple terms or clauses can be grouped together with parentheses for sub-queries

    Example: (Free or %) AND Fall

* Boolean operators

    * "+" Indicates it must be present; "-" indicates it must not be present

    * The "+" and "–" only affects the terms to the right of the operator. Example: Fall +Sale

    * Familiar operators AND, OR and NOT are also supported. NOT takes precedence over AND. AND takes precedence over OR

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        subject="Sample Text",
        body="Sample Text"
    )


Filter on Specific Industries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Filtering on specific industries requires the numerical industryId.  The industryId can be retrieved using the Core
class, by either retrieving the complete list of all industries with corresponding industryId using
`competitivetracker.core.industries`, or by searching for industries with a search text string using
`competitivetracker.core.discover`.

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        industryId=[1, 2, 3]
    )


Filter on Specific Companies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Filtering on specific companies requires the numerical companyId.  The companyId can be retrieved using the Core
class, by either retrieving the complete list of all companies with corresponding companyId using
`competitivetracker.core.companies`, or by searching for companies with a search text string using
`competitivetracker.core.discover`.

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        companyId=[1, 2, 3],
        excludedCompanyId=[5, 6, 7]
    )


Filter on Specific Brands
^^^^^^^^^^^^^^^^^^^^^^^^^

Filtering on specific brands requires the numerical brandId.  The brandId can be retrieved using the Core
class, by either retrieving the complete list of all brands with corresponding brandId using
`competitivetracker.core.brands`, or by searching for brands with a search text string using
`competitivetracker.core.discover`.

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        brandId=[1, 2, 3],
        excludedBrandId=[5, 6, 7]
    )


Filter on Specific Domains
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        sendingDomain=["example1.com", "example2.com"],
        excludeSendingDomain=["example3.com", "example4.com"]
    )


Exclude Campaigns without Creatives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        hasCreative=True
    )


Filter on ESP
^^^^^^^^^^^^^

Filtering on specific ESPs requires the numerical espId.  The espId can be retrieved using the Core
class, by either retrieving the complete list of all ESPs with corresponding espId using
`competitivetracker.core.esps`, or by searching for ESPs with a search text string using
`competitivetracker.core.discover`.

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        espId=1
    )


Filter on Engagement
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        readPercentage=">,20"
    )


Filter on Inbox Placement
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        inboxPercentage="<,90"
    )

