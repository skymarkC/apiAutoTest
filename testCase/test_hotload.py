import pytest
import allure
from common.log import logger
from common.yaml_util import YamlUtil
from common.function_def import FunctionDef


@pytest.mark.test
@allure.title("测试热加载函数")
@allure.description("测试热加载函数功能是否正常")
@pytest.mark.parametrize('args_name', YamlUtil().read_testcase_yaml(
    "C://Users//SZY//Desktop//pytest-allure//testData//api_hotload.yaml"))
def test_hot_load(args_name):

    token = FunctionDef(YamlUtil()).hot_load(args_name['token'])
    logger.info('步骤1.yaml文件中调用外部函数获取的值：{}'.format(token))

    test_parm = FunctionDef(YamlUtil()).hot_load(args_name['validate']['test_parm'])
    logger.info('步骤2.yaml文件中获取外部变量的值：{}'.format(test_parm))
