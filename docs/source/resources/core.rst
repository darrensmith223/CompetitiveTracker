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

The ``brands`` class enables users to retrieve details about brands, including getting a list of all brands and
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

    response = ct.core.brands.get_all_brands()


Companies
---------

The ``companies`` class enables users to retrieve details about companies, including getting a list of all companies and
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

    response = ct.core.companies.get_all_companies()

Discover
--------

The Discover class enables a user to search for different entities, such as ESPs or Industries, by passing the search
text as a string.  The Discover class can be used in conjunction with other Competitive Tracker classes, particularly
when numerical identifiers are required.  The Discover search capabilities can be used to retrieve the identifier of an
entity from a string or partial string.  The names and identifiers of industries matching a search string can be
retrieved using the `Competitive Tracker API`_, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.discover.search_industries(
        q="example_industry"
    )
    print(response)


Search for Brands
*****************

To search for brands and retrieve the respective brandId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.discover.search_brands(
        q="example_brand"
    )


The search text can be either a complete or a partial string.

Search for Companies
********************

To search for companies and retrieve the respective companyId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.discover.search_companies(
        q="example_company"
    )


The search text can be either a complete or a partial string.


Search for ESPs
***************

To search for ESPs and retrieve the respective espId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.discover.search_esps(
        q="example_ESP"
    )


The search text can be either a complete or a partial string.


Search for Industries
*********************

To search for industries and retrieve the respective industryId, pass the search text using the ``q`` parameter, as shown:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.core.discover.search_industries(
        q="example_industry"
    )

The search text can be either a complete or a partial string.

Domains
-------

Function
********


ESPs
----

The ``esps`` class enables users to retrieve details about ESPs, including getting a list of all ESPs and
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

    response = ct.core.esps.get_all_esps()


Graph
-----

Function
********


Industries
----------

The ``industries`` class enables users to retrieve details about industries, including getting a list of all industries and
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

    response = ct.core.industries.get_all_industries()


Ping
----

Function
********
