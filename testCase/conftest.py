# conftest.py用于在多个py文件之间共享前置配置
import pytest
from common.yaml_util import YamlUtil


# scope='function':每个方法前执行一次；scope='class'：类执行开始时执行一次；scope='module'：在当前.py 脚本里面所有用例开始前只执行一次;
# scope='session'：跨多个.py文件之前执行一次。
@pytest.fixture(scope='session', autouse=False)
def clear_yaml():
    YamlUtil().clear_token_yaml("C://Users//SZY//Desktop//pytest-allure//testData//get_token.yaml")
