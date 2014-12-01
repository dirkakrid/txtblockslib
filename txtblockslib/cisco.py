#!/usr/bin/env python

from txtblocks import TextElement, TextBlock, BlockParser

def show_spanningtree_interface_detail(text):
    stpvlanid = TextElement('^VLAN(?P<vlanid>\d+) is executing the')
    stpvlanbrinfo = TextElement('Bridge Identifier has priority (?P<brprio>\d+), sysid (?P<brsysid>\d+), address (?P<braddr>([0-9a-f]{4}\.){2}[0-9a-f]{4})')
    stpvlanrootbr = TextElement('Current root has priority (?P<rootprio>\d+), address (?P<rootaddr>([0-9a-f]{4}\.){2}[0-9a-f]{4})')
    stprootport = TextElement('Root port is \d+ \((?P<rootport>.+)\), cost of root path is (?P<rootpathcost>\d+)')
    stpvlan = TextBlock('stpvlan', [stpvlanid, stpvlanbrinfo, stpvlanrootbr, stprootport], '^VLAN\d+ is executing the', oneliner=True)

    port = TextElement('^Port \d+ \((?P<ifname>.+)\) of VLAN(?P<vlanid>\d+) is')
    bpdusent = TextElement('BPDU: sent (?P<bpdusent>\d+),')
    bpdurecv = TextElement('BPDU: sent \d+, received (?P<bpdurecv>\d+)')
    stpport = TextBlock('stpport', [port, bpdusent, bpdurecv], '^Port \d+', oneliner=True)
    
    blocks = BlockParser([stpport, stpvlan])

    result = blocks.parse(text)

    return result

