Search
======

Cool text about search

Include links:
https://support.emailanalyst.com/en/articles/2414635-how-to-maximize-advanced-search-in-competitive-tracker


.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        sendingDomain="example.com"
    )
    print(response)


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

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.search.search(
        qd="daysBack:3",
        industryId=[1, 2, 3]
    )


Filter on Specific Companies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

