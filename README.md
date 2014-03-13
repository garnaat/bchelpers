bchelpers
=========

Handy helpers to make botocore easier to use.

I find myself wanting to use botocore quite often because its very simple
and pared down and it's also always current with AWS functionality.  And
because Python 3.x.

That's great.  But it is pretty low-level and kind of awkward to use.
The long-term fix for that is boto3 but in the mean time I've created
a few helpers to make things a bit easier.

Using bchelpers
---------------

A simple use would be like this:

    from bchelpers.region import Region

	region = Region(region_name='us-west-2', profile='dev')
	ec2 = region.get_service_endpoint('ec2')
	instances = ec2.call('describe-instances',
	                     query='Reservations[*].Instances[*]')

The variable `instances` would now be a list of dictionaries, each containing
the full data for each instance running in this account in this region.

Note the ability to pass a
[jmespath](https://github.com/boto/jmespath) query in the call.  This
query will be run against the raw data from the response so you can
easily tailor the output to include exactly what you want and only
what you want.  Check out the `jmespath` link for full details on all of
the awesome things you can do with it.

I'll probably add more stuff to this over time but I fully expect this to
just go away eventually and be replaced with boto3.

