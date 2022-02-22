Core
====

The Core module contains several classes which can be used to get details of entities available within
the Competitive Tracker platform, such as entity identifiers.  Core includes the following classes:

* `competitivetracker.core.brands`
* `competitivetracker.core.companies`
* `competitivetracker.core.discover`
* `competitivetracker.core.domains`
* `competitivetracker.core.esps`
* `competitivetracker.core.graphs`
* `competitivetracker.core.industries`
* `competitivetracker.core.ping`


Brands
------

The ``brands`` class enables users to retrieve details about brands, including a list of all brands and
the respective brandId.  Brands can be used in conjunction with other Competitive Tracker classes when the
brandId is required.  All brands and the respective brandId can be retrieved using the
`Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.brands.get_all_brands()
    print(response)


.. _Competitive Tracker API: http://api.edatasource.com/docs/#/competitive

Get All Brands
**************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.brands.get_all_brands()


Get Brand Details From ID
*************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.brands.get_brand_details(brandId=1)


Get All Domains for a Brand
***************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.brands.get_all_brand_domains(brandId=1)


Companies
---------

The ``companies`` class enables users to retrieve details about companies, including a list of all companies and
the respective companyId.  Companies can be used in conjunction with other Competitive Tracker classes when the
companyId is required.  All companies and the respective companyId can be retrieved using the
`Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.companies.get_all_companies()
    print(response)


Get All Companies
*****************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.companies.get_all_companies()


Get Company Details From ID
***************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.companies.get_company_details(companyId=1)


Get All Brands for a Company
****************************


.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.companies.get_all_company_brands(companyId=1)


Discover
--------

The Discover class enables a user to search for different entities, such as ESPs or Industries, by passing the search
text as a string.  The Discover class can be used in conjunction with other Competitive Tracker classes, particularly
when numerical identifiers are required.  The Discover search capabilities can be used to retrieve the identifier of an
entity from a string or partial string.  For example, the names and identifiers of industries matching a search string
can be retrieved using the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.discover.search_industries(
        q="example_industry"
    )
    print(response)


Search for Any Match
********************

To search across all entities and return the name and ID of any match for a string, pass the search text using
the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.discover.search(
        q="example_text"
    )

The search text can be either a complete or a partial string.


Search for Brands
*****************

To search for brands and retrieve the respective brandId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.discover.search_brands(
        q="example_brand"
    )


The search text can be either a complete or a partial string.

Search for Companies
********************

To search for companies and retrieve the respective companyId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.discover.search_companies(
        q="example_company"
    )


The search text can be either a complete or a partial string.


Search for ESPs
***************

To search for ESPs and retrieve the respective espId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.discover.search_esps(
        q="example_ESP"
    )


The search text can be either a complete or a partial string.


Search for Industries
*********************

To search for industries and retrieve the respective industryId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.discover.search_industries(
        q="example_industry"
    )

The search text can be either a complete or a partial string.


Search for Domains
******************

To search for domains and retrieve the respective domainId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.discover.search_domains(
        q="example_domain"
    )

The search text can be either a complete or a partial string.


Domains
-------

The ``domains`` class enables users to retrieve details about domains, including a list of all domains and
the respective domainId.  Domains can be used in conjunction with other Competitive Tracker classes when the
domainId is required.  All domains and the respective domainId can be retrieved using the
`Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.domains.get_all_domains()
    print(response)


Get All Domains
***************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.domains.get_all_domains()

Get Domain Details From ID
**************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.domains.get_domain_details(domainId=1)


ESPs
----

The ``esps`` class enables users to retrieve details about ESPs, including a list of all ESPs and
the respective espId.  Esps can be used in conjunction with other Competitive Tracker classes when the
espId is required.  All ESPs and the respective espId can be retrieved using the
`Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.esps.get_all_esps()
    print(response)


Get All ESPs
************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.esps.get_all_esps()

Get ESP Details From ID
***********************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.esps.get_esp_details(espId=1)


Graph
-----

Graphs enable a user to retrieve a complete mapping for a company of the various brands and company details.  The
Graphs class provides different methods of identifying and retrieving these details, including searching by text, as
well as by domain.  This class makes it easier to identify the company details with a single endpoint, rather than
having to leverage multiple endpoints to identify the companyId, retrieve company details, and retrieve the brands for
the company.  For example, company details for a company can be retrieved from a search text, as shown below:


.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.graph.get_company(q="example_text")
    print(response)


Get Company Details From String
*******************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.graph.get_company(q="example_text")


Get Company Details From Domain
*******************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.graph.get_company_from_domain(domainName="example_domain")


Get Company Details From ID
***************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.graph.get_company_from_id(companyId=1)


Industries
----------

The ``industries`` class enables users to retrieve details about industries, including a list of all industries and
the respective industryId.  Industries can be used in conjunction with other Competitive Tracker classes when the
industryId is required.  All industries and the respective industryId can be retrieved using the
`Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.industries.get_all_industries()
    print(response)



Get All Industries
******************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.industries.get_all_industries()


Get Industry Details From ID
****************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.industries.get_industry_details(industryId=1)


Get All Brands for an Industry
******************************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.industries.get_all_industry_brands(industryId=1)


Ping
----

Ping enables a user to verify that the core module is accessible.  The Core ping is separate from the Competitive
Tracker ping because the Core module interfaces with a different underlying service than the primary Competitive
Tracker service.


Ping the Core Service
*********************

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.core.ping.ping_service()
