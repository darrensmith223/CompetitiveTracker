Intelligence
============

Cool text about intelligence

Includes the following classes:

* `competitivetracker.intelligence.brand`
* `competitivetracker.intelligence.campaign`
* `competitivetracker.intelligence.domain`
* `competitivetracker.intelligence.ipdeliverability`


Brand
-----

Cool text about Brand Intelligence

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.brand.get_top_domains(brandId=1)
    print(response)

Get Top Domains for a Brand
***************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.intelligence.brand.get_top_domains(brandId=1)


Campaign
--------

Cool text about Campaign Intelligence

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

Cool text about Domain Intelligence

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

Cool text about IP Deliverability Intelligence

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


