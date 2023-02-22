import pytest
import allure
import requests
import os
from common.log import logger
from common.yaml_util import YamlUtil


@pytest.mark.smoke
@allure.title("题目管理接口测试")
@allure.description("断言题目管理接口的响应码是否正常")
@pytest.mark.parametrize('args_name', YamlUtil().read_testcase_yaml(
    "C://Users//SZY//Desktop//pytest-allure//testData//api_question_data.yaml"))
# 用例通过yaml文件完成数据驱动， 本用例读取api_question_data.yaml中的两个接口用例， 下面的test_api_question方法会调用执行两次，并分别断言。
def test_api_question(args_name):

    logger.info('步骤1.获取yaml文件中的接口用例：{}'.format(args_name))  # 调用日志模块打印

    logger.info('步骤2.获取接口响应内容')
    url = args_name['request']['url']
    header = {
        "Authorization": args_name['token']
    }
    res = requests.post(url, headers=header)
    logger.info('   响应内容：{}'.format(res.json()))

    logger.info('步骤3.进行断言')
    code = res.json()['code']
    # 异常处理机制
    try:
        assert code == args_name['validate']['code']   # 传参都正常时，返回信息code=200， token校验有误/过期时，返回401
        logger.info('   断言内容：{} == {}'.format(code, args_name['validate']['code']))
    except AssertionError as e:
        logger.error('  断言异常！：{}，请排查......'.format(e))


if __name__ == '__main__':
    test_api_question()
