import pytest
import yaml
import os

from pytest_sum.cal_new import Calcalator

yaml_file_path = os.path.dirname("__file__") + "./CalTest_new.yml"

with open(yaml_file_path,encoding="UTF-8") as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']["add_data"]
    add_myid = datas['add']["add_ids"]

    sub_datas = datas["sub"]["sub_data"]
    sub_ids = datas["sub"]["sub_ids"]

    mul_datas =  datas["mul"]["mul_data"]
    mul_ids = datas["mul"]["mul_ids"]

    div_datas = datas["div"]["div_data"]
    div_ids = datas["div"]["div_ids"]

@pytest.fixture(scope="function")
def test_scope():
    print("开始计算")
    yield
    print("计算结束")

@pytest.fixture(scope="class")
def get_cal():
    print("计算器实例化")
    cal = Calcalator()
    return cal




@pytest.fixture(params=add_datas,ids=add_myid)
def get_add_datas(request):
    add_data = request.param
    print(f"获取到的数据结果是:{add_data}")
    yield add_data

@pytest.fixture(params=sub_datas,ids=sub_ids)
def get_sub_datas(request):
    sub_data = request.param
    print(f"获取到的数据结果是:{sub_data}")
    yield sub_data

@pytest.fixture(params=mul_datas,ids=mul_ids)
def get_mul_datas(request):
    mul_data = request.param
    print(f"获取到的数据结果是:{mul_data}")
    yield mul_data

@pytest.fixture(params=div_datas,ids=div_ids)
def get_div_datas(request):
    div_data = request.param
    print(f"获取到的数据结果是:{div_data}")
    yield div_data
