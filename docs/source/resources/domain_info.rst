Domain Info
===========

Domain info provides users access to the details of a domain, such as what brand(s) it is associated with, the company,
what ESPs are used by the brand, and other useful details that a user can leverage when researching a domain.  Domain info
is also incredibly useful when used in conjunction with the other Competitive Tracker classes, especially when the brandId,
companyId, industryId, and/or ESP Id is needed for a particular function.  All of these details can be accessed using
the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.domain_info.get_domain_info(domain="example.com")
    print(response)


.. _Competitive Tracker API: http://api.edatasource.com/docs/#/competitive

Get Brand and Company Details from Domain
*****************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.domain_info.get_domain_info(domain="example.com")

Get the Send Volume and ESPs Used for a List of Domains
*******************************************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.domain_info.get_brand_volume_and_esps(domains=["example.com"])
