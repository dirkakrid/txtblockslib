# txtblocks library

This should become some sort of a library for my CLI screen scraping parser project: https://github.com/verbosemode/txtblock

* "show_spanningtree_interface_detail" is a parser for "show spanning-tree interface detail" on Cisco Catalyst switches

That's what the returned data structure looks like atm

	{'stpport': [{'bpdurecv': '4',
		      'bpdusent': '1355228',
		      'ifname': 'GigabitEthernet1/0/21',
		      'vlanid': '0040'},
		     {'bpdurecv': '0',
		      'bpdusent': '931171',
		      'ifname': 'GigabitEthernet1/0/23',
		      'vlanid': '0040'},
		     {'bpdurecv': '0',
		      'bpdusent': '3445197',
		      'ifname': 'GigabitEthernet1/0/24',
		      'vlanid': '0040'},
	 'stpvlan': [{'braddr': 'c40a.acc2.c600',
		      'brprio': '32768',
		      'brsysid': '666',
		      'rootself': 'We are the root of the spanning tree',
		      'vlanid': '0666'},
		     {'braddr': 'c30a.eab7.c300',
		      'brprio': '32768',
		      'brsysid': '1500',
		      'rootaddr': '227a.ef33.ea41',
		      'rootpathcost': '1004',
		      'rootport': 'GigabitEthernet1/0/49',
		      'rootprio': '5596',
		      'vlanid': '1500'}]}

# TODO

OOP interface for using the parser
 - Error handling
 - Convert data to python data types -> VLAN id -> Integer ...
