Intelligence
============

Competitive Intelligence enables a user to get information about the email programs of different organizations by
accessing data across a number of facets.  Intelligence includes the following classes:

* `competitivetracker.intelligence.brand`
* `competitivetracker.intelligence.campaign`
* `competitivetracker.intelligence.domain`
* `competitivetracker.intelligence.ipdeliverability`


Brand
-----

Brand Intelligence enables a user to access details about a brand.  Where the numerical
brandId is needed, the brandId can be retrieved by either retrieving the complete list of all brands with corresponding
brandId using `competitivetracker.core.brands`_, or by searching for brands with a search text string using
`competitivetracker.core.discover`_.  For example, the top sending domains for a brand can be retrieved using the
`Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.brand.get_top_domains(brandId=1)
    print(response)


.. _Competitive Tracker API: http://api.edatasource.com/docs/#/competitive
.. _competitivetracker.core.brands: https://competitivetracker.readthedocs.io/en/latest/api/core.html#competitivetracker-core-brands
.. _competitivetracker.core.discover: https://competitivetracker.readthedocs.io/en/latest/api/core.html#competitivetracker-core-discover


Get Top Domains for a Brand
***************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.brand.get_top_domains(brandId=1)


Campaign
--------

Campaign Intelligence enables a user to get details about a specific campaign that was delivered by a sender.  Where
the numerical campaignId is needed, the campaignId can be retrieved from the results of any campaign query function.
For example, the campaignId can be retrieved from `competitivetracker.intelligence.domain.get_campaigns()`_ and
`competitivetracker.search.search()`_.  For example, the campaign details can be retrieved for a specific campaignId by
using the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.campaign.get_campaign(campaignId=1)
    print(response)


.. _competitivetracker.search.search(): https://competitivetracker.readthedocs.io/en/latest/api/search.html#competitivetracker.search.Search.search
.. _competitivetracker.intelligence.domain.get_campaigns(): https://competitivetracker.readthedocs.io/en/latest/api/intelligence.html#competitivetracker.intelligence.Domain.get_campaigns



Get the Details for a Specific Campaign
***************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.campaign.get_campaign(campaignId=1)


Get Target Country for a Campaign
*********************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.campaign.get_target_country(campaignId=1)


Domain
------

Domain Intelligence enables a user to get details about a sending domain.  For example, the details for all campaigns
delivered from a sending domain over the past 3 days can be retrieved using the `Competitive Tracker API`_, as shown
below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.domain.get_campaigns(
        domain="example.com",
        qd="daysBack:3"
    )
    print(response)


Get All Campaigns for a Domain
******************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.domain.get_campaigns(
        domain="example.com",
        qd="daysBack:3"
    )


Get the Number of Campaigns Sent by a Domain Per Week
*****************************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.domain.get_campaigns_per_week(domain="example.com")


Get the Average Campaign Volume for a Domain
********************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.domain.get_average_volume_per_campaign(
        domain="example.com",
        qd="daysBack:3"
    )


Get the Total Volume Sent for a Domain
**************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.domain.get_total_volume(
        domain="example.com",
        qd="daysBack:3"
    )


Get Sending Volume Over Time for a Domain
*****************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.domain.get_volumes(
        domain="example.com",
        qd="daysBack:3"
    )


Get Volume Data for a Domain by Day of the Week
***********************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.domain.get_dow_avg_volume(domain="example.com")


Get ISP Placement for a Domain
******************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.domain.get_isp_placements(
        domain="example.com",
        qd="daysBack:3"
    )


IP Deliverability
-----------------

IP Deliverability Intelligence enables a user to get deliverability details from an IP address or range of IP addresses
that are used to send email.  For example, the deliverability details of a sending IP address from the past 3 days can
be retrieved using the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.ipdeliverability.get_deliverability_stats(
        qd="daysBack:3",
        sendingIpAddress="0.0.0.0"
    )
    print(response)


The IP Deliverability data can be retrieved at either an individual IP address level, or in aggregate for a range of IP
addresses.


Get Deliverability Stats by IP
******************************

Retrieving deliverability stats at an individual IP address level enables a user to perform very detailed analysis on
the differences in performance between IP addresses.  When retrieving IP address data, the user has the
ability to query for a specific IP address, or to retrieve the data for each individual IP address within a
range by specifying the starting IP address within that range.

Stats for a Single IP
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.ipdeliverability.get_deliverability_stats(
        qd="daysBack:3",
        sendingIpAddress="0.0.0.0"
    )


Stats for Each IP Within a Range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.ipdeliverability.get_deliverability_stats_for_range(
        qd="daysBack:3",
        startingIpAddress="0.0.0.0"
    )


Get Aggregate Deliverability Stats for an IP Range
**************************************************

Retrieving aggregate deliverability stats for an entire range of IP addresses can be useful when performing analysis on
the performance between IP ranges, such as comparing the performance between geographical regions or data centers.

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.intelligence.ipdeliverability.get_agg_stats_for_range(
        qd="daysBack:3",
        startingIpAddress="0.0.0.0"
    )


