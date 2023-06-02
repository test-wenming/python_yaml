import yaml

def read_yaml():
    with open('yaml_file', "r", encoding="utf-8") as file:
        file_data = file.read()

        # 将读取到的数据进行格式化
        yaml_data = yaml.safe_load(file_data)[0]['requests']['data']
        yaml_url = yaml.safe_load(file_data)[0]['requests']['url']
        return yaml_data, yaml_url


read_yaml()


