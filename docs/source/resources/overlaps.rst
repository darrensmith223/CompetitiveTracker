Overlaps
========

Overlap details enable a user to understand what domains are sending email to the same recipient lists, and to what
degree the mailing lists overlap.  The overlapping sending domains for a specific domain and the related details can
be retrieved using the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.overlaps.get_domain_overlaps(domain="example.com")
    print(response)


.. _Competitive Tracker API: http://api.edatasource.com/docs/#/competitive


Get Overlap Details for a Domain
********************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.overlaps.get_domain_overlaps(domain="example.com")


Overlap Across all Industries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, only the overlaps for a domain within the same industry will be returned.  To show the overlaps across
all industries, use the parameter ``ignoreIndustry``, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.overlaps.get_domain_overlaps(
        domain="example.com",
        ignoreIndustry=True
    )


Exclude Domains from the Same Company
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.overlaps.get_domain_overlaps(
        domain="example.com",
        excludeSameCompany=True
    )


Get Overlap Details Between Specific Domains
********************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.overlaps.get_narrowed_overlap(
        domain="example.com",
        overlapDomain=["overlap1.com", "overlap2.com"]
    )

Get Overlap of Top Competitors for a Domain
*******************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.overlaps.get_top_competing(domain="example.com")

