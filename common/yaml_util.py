import yaml


# yaml_util用与统一封装处理yaml文件的方法。
class YamlUtil:

    PARM = 'FOR_TEST'

    # 读取测试用例的yaml数据
    def read_testcase_yaml(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 写入yml文件
    def write_token_yaml(self, file_path, data):
        with open(file_path, mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除yml文件
    def clear_token_yaml(self, file_path):
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.truncate()
