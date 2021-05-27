Overlaps
========

Cool text about overlaps

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.____
    print(response)


Get Overlap Details for a Domain
********************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.overlaps.get_domain_overlaps(domain="example.com")


Overlap Across all Industries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, only the overlaps for a domain within the same industry will be returned.  To show the overlaps across all industries, use the parameter `ignoreIndustry`, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.overlaps.get_domain_overlaps(
        domain="example.com",
        ignoreIndustry=True
    )


Exclude Domains from the Same Company
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.overlaps.get_domain_overlaps(
        domain="example.com",
        excludeSameCompany=True
    )


Get Overlap Details Between Specific Domains
********************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.overlaps.get_narrowed_overlap(
        domain="example.com",
        overlapDomain=["overlap1.com", "overlap2.com"]
    )

Get Overlap of Top Competitors for a Domain
*******************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.overlaps.get_top_competing(domain="example.com")

