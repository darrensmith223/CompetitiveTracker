Domain Info
===========

Cool text about domain info

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.____
    print(response)



Get Brand and Company Details from Domain
*****************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.domain_info.get_domain_info(domain="example.com")

Get the Send Volume and ESPs Used for a List of Domains
*******************************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.domain_info.get_brand_volume_and_esps(domain=["example.com"])
