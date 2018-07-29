class FilterModule(object):
    def jt_parse_intf_terse(self,intf):
        if intf:
            intf_obj = intf['logical-interface']
            if isinstance(intf_obj,dict):
                if intf_obj['name'][:3] in ['ge-','xe-']:
                    data = dict()
                    data['name'] = intf_obj['name']
                    data['vrf'] = intf_obj['vrfname']
                    data['op_status'] = intf_obj['oper-status']
                    result = data
                else:
                    result = "-1"
            else:
                result = list()
                #print(intf_obj)
                for sub_intf in intf_obj:
                    if sub_intf['name'][:3] in ['ge-','xe-']:
                        data = dict()
                        data['name'] = sub_intf['name']
                        data['vrf'] = sub_intf['vrfname']
                        data['op_status'] = sub_intf['oper-status']
                        result.append(data)
                    else:
                        result = '-1'
        else:
            result = '-1'
        print(result)
        return result
            
    def filters(self):
        return {'jt_parse_intf_terse': self.jt_parse_intf_terse}
