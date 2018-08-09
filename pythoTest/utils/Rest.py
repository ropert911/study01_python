import requests

__all__ = [
    'Rest'
]


class Rest:
    def get(self, url, params=None, key='data', timeout=5):
        ret = None
        try:
            ret = requests.get(url, params=params, timeout=timeout)
            ret = ret.json()[key]
        except Exception as e:
            raise
        return ret

    def ap_statistic(self):

        user_list = self.get("http://192.168.20.91:10015/inner/user/user/queryUserListWithAreaTreeByIds",
                             params={'queryall': 'true'})
        ap_list = self.get("http://192.168.20.91:10015/inner/device/management/getapStatistics",
                           params={'queryall': 'true'})
        # print("user_list",user_list)
        for i in user_list:
            print(i.get('userId'))
            topAreaList = i.get('topAreaList')
            for j in topAreaList:
                print("  id:", j.get('id'), "level", j.get('level'))

        # print("ap_list", ap_list)
        for i in ap_list:
            print(" topId", i.get('topId'), " total:", i.get('total'),
                  'enableAp', i.get('enableAp'), 'disAp', i.get('disAp'))

ism = Rest()
ism.ap_statistic()
