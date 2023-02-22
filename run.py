import pytest
import os

# 用例统一在run.py文件中执行。
if __name__ == '__main__':
    pytest.main(['-m=smoke', '-s', '--alluredir', './report/'])  # 执行标记为smoke的冒烟测试用例，并生成报告
    os.system('allure serve ./report/')   # 打开报告
    # pytest.main()
