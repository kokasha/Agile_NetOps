import jxmlease
from pprint import pprint

input_data='''
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/14.1R4/junos">
    <system-uptime-information xmlns="http://xml.juniper.net/junos/14.1R4/junos">
        <current-time>
            <date-time junos:seconds="1532753694">2018-07-28 06:54:54 EET</date-time>
        </current-time>
        <system-booted-time>
            <date-time junos:seconds="1532553911">2018-07-25 23:25:11 EET</date-time>
            <time-length junos:seconds="199783">2d 07:29</time-length>
        </system-booted-time>
        <protocols-started-time>
            <date-time junos:seconds="1532553973">2018-07-25 23:26:13 EET</date-time>
            <time-length junos:seconds="199721">2d 07:28</time-length>
        </protocols-started-time>
        <last-configured-time>
            <date-time junos:seconds="1532038829">2018-07-20 00:20:29 EET</date-time>
            <time-length junos:seconds="714865">1w1d 06:34</time-length>
            <user>lab</user>
        </last-configured-time>
        <uptime-information>
            <date-time junos:seconds="1532753694">6:54AM</date-time>
            <up-time junos:seconds="199813">2 days,  7:30</up-time>
            <active-user-count junos:format="1 user">1</active-user-count>
            <load-average-1>0.50</load-average-1>
            <load-average-5>1.16</load-average-5>
            <load-average-15>0.96</load-average-15>
        </uptime-information>
    </system-uptime-information>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
'''

xml_parsed = jxmlease.parse(input_data)
pprint(xml_parsed.get_cdata())
