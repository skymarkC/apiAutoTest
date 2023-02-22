import json


class FunctionDef:

    def __init__(self, obj):
        # 获取一个对象
        self.obj = obj

    def hot_load(self, data):
        # hot_load方法用于在yaml文件中调用外部函数，实现热加载。
        # parameter:data  即为yaml文件中的 ${fun(param)}
        if data:
            # 保存原数据类型
            data_type = type(data)
            # 数据类型可能(string，int,float,list,dict)，需要先数据转换
            if isinstance(data, dict) or isinstance(data, list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            for _ in range(1, str_data.count("${")+1):
                if "${" in str_data and "}" in str_data:
                    index = str_data.index("${")
                    indexend = str_data.index("}", index)
                    old_value = str_data[index:indexend+1]
                    # 获取对象属性
                    if "(" in old_value:
                        fun_name = old_value[2:old_value.index("(")]
                        fun_values = old_value[old_value.index("(")+1:old_value.index(")")]
                        fun_values_new = fun_values.split(",")
                        # *fun_values_new 解包 列表
                        if fun_values_new != " ":
                            # getattr() 函数用于返回一个对象属性值。 self.obj为对象名称
                            new_value = getattr(self.obj, fun_name)(*fun_values_new)
                            str_data = str_data.replace(old_value, str(new_value))
                        else:
                            new_value = getattr(self.obj, fun_name)()
                            str_data = str_data.replace(old_value, str(new_value))
                    else:
                        fun_name = old_value[2:old_value.index("}")]
                        new_value = getattr(self.obj, fun_name)
                        str_data = str_data.replace(old_value, str(new_value))
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        return data
