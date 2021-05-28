Intelligence
============

Competitive Intelligence enables a user to get information about the email programs of different organizations by
accessing data across a number of different facets.  Intelligence includes the following classes:

* `competitivetracker.intelligence.brand`
* `competitivetracker.intelligence.campaign`
* `competitivetracker.intelligence.domain`
* `competitivetracker.intelligence.ipdeliverability`


Brand
-----

Brand Intelligence enables a user to access details about the top sending domains for a brand.  Where the numerical
brandId is needed, the brandId can be retrieved by either retrieving the complete list of all brands with corresponding
brandId using `competitivetracker.core.brands`, or by searching for brands with a search text string using
`competitivetracker.core.discover`.  The top sending domains for a brand can be retrieved using the
`Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.brand.get_top_domains(brandId=1)
    print(response)


.. _Competitive Tracker API: http://api.edatasource.com/docs/#/competitive


Get Top Domains for a Brand
***************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.brand.get_top_domains(brandId=1)


Campaign
--------

Campaign Intelligence enables a user to get details about a specific campaign that was delivered by a sender.  Where
the numerical campaignId is needed, the campaignId can be retrieved from the results of any campaign query function.
For example, the campaignId can be retrieved from `competitivetracker.intelligence.domain.get_campaigns()` and
`competitivetracker.search.search()`.  The campaign details can be retrieved for a specific campaignId by using
the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.campaign.get_campaign(campaignId=1)
    print(response)


Get the Details for a Specific Campaign
***************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.campaign.get_campaign(campaignId=1)


Get Target Country for a Campaign
*********************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.campaign.get_target_country(campaignId=1)


Domain
------

Domain Intelligence enables a user to get details about a sending domain.  The details for all campaigns delivered from
a sending domain over the past 3 days can be retrieved using the `Competitive Tracker API`_, as shown below:

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

    response = ct.intelligence.domain.get_campaigns(
        domain="example.com",
        qd="daysBack:3"
    )


Get the Number of Campaigns Sent by a Domain Per Week
*****************************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.domain.get_campaigns_per_week(domain="example.com")


Get the Average Campaign Volume for a Domain
********************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.domain.get_average_volume_per_campaign(
        domain="example.com",
        qd="daysBack:3"
    )


Get the Total Volume Sent for a Domain
**************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.domain.get_total_volume(
        domain="example.com",
        qd="daysBack:3"
    )


Get Sending Volume Over Time for a Domain
*****************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.domain.get_volumes(
        domain="example.com",
        qd="daysBack:3"
    )


Get Volume Data for a Domain by Day of the Week
***********************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.domain.get_dow_avg_volume(domain="example.com")


Get ISP Placement for a Domain
******************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.domain.get_isp_placements(
        domain="example.com",
        qd="daysBack:3"
    )


IP Deliverability
-----------------

IP Deliverability Intelligence enables a user to get deliverability details from an IP address or range of IP addresses
that are used to send email.  The deliverability details of a sending IP address from the past 3 days can be retrieved
using the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.ipdeliverability.get_deliverability_stats(
        qd="daysBack:3",
        sendingIpAddress="0.0.0.0"
    )
    print(response)


Get Deliverability Stats by IP
******************************

Stats for a Single IP
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.ipdeliverability.get_deliverability_stats(
        qd="daysBack:3",
        sendingIpAddress="0.0.0.0"
    )


Stats for Each IP Within a Range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.ipdeliverability.get_deliverability_stats_for_range(
        qd="daysBack:3",
        startingIpAddress="0.0.0.0"
    )


Get Aggregate Deliverability Stats for an IP Range
**************************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.ipdeliverability.get_agg_stats_for_range(
        qd="daysBack:3",
        startingIpAddress="0.0.0.0"
    )


