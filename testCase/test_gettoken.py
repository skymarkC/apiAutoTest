import pytest
import requests
from common.yaml_util import YamlUtil


# 该用例仅为获取token值，不做断言测试。在执行用例前执行一次本py即可。
@pytest.mark.login
def test_api_gettoken():
    # 调用登录接口， 获取响应中的token字段
    url = 'http://10.11.4.239:30700/BASE_URL/api/auth/login'
    formdata = {
        "username": "test-tenantadmin@cmict.chinamobile.com",
        "password": "123456"
    }
    res = requests.post(url, json=formdata)
    # 将获取到的token值， 写入get_token.yaml中，供其他用例统一读取。
    YamlUtil().write_token_yaml('C://Users//SZY//Desktop//pytest-allure//testData//get_token.yaml',
                                res.json()['token'])


if __name__ == '__main__':
    # 先清除、再写入，避免带上历史数据。
    # YamlUtil().clear_token_yaml("C://Users//SZY//Desktop//pytest-allure//testData//get_token.yaml")
    test_api_gettoken()
