import requests
import yaml
import pytest

from read_yaml import read_yaml


class Test_CallYaml:

    @pytest.mark.parametrize('case_information', read_yaml()[0])
    def test_read_yaml(self, case_information):
        print(f"这是url：{read_yaml()[1]}###########")
        print(f"这是data：{case_information}###########")
        response = requests.post(read_yaml()[1], data=case_information)
        print(response.json())


if __name__ == '__main__':
    pytest.main(['-sv', 'python_yaml.py'])



