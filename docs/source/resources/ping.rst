Ping
====

Pinging the Competitive Tracker service enables you to verify that the service is available, which can be useful when
troubleshooting, as shown below:

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    response = ct.ping.ping_service()
    print(response)


If the service is available, `ping_service()` will return the string `pong`.


Ping the Competitive Tracker Service
------------------------------------

.. code-block:: python

    from competitivetracker import CompetitiveTracker

    ct = CompetitiveTracker("API_KEY")

    ct.ping.ping_service()

