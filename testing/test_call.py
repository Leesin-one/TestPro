import pytest
import yaml

from calc import Calculator

with open("CalTest.yml") as f:
    data=yaml.safe_load(f)["add"]
    add_datas=data["datas"]
    myid=data["myid"]
    chufa_datas=data["chufadata"]

class TestA:

    def setup_class(self):
        print("开始计算")
        # 实例计算器类
        self.cal = Calculator()
    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect",add_datas,ids=myid)
    def test_add(self,a,b,expect):
        # 调用add方法
        result=self.cal.add(a,b)
        #得到结果后，需要写断言
        # 判定类型参数，result是否为float类型
        if isinstance(result,float):
            # 结果保留2位小时数
            result=round(result,2)
        assert result == expect

    @pytest.mark.parametrize("c,d,expect",chufa_datas, ids=myid)
    def test_chufa(self,c,d,expect):
        if d==0:
            print("输入错误,分母不能为0")
            assert 1==2
        else:
            result = self.cal.div(c, d)
            if isinstance(result,float):
              # 结果保留2位小时数
              result=round(result,2)
              assert result == expect




   # def test_add1(self):
   #     # 实例计算器类
   #     cal = Calculator()
   #     # 调用add方法
   #     result = cal.add(0.1, 0.3)
   #     # 得到结果后，需要写断言
   #     assert result == 0.4
   #
   # def test_add2(self):
   #     # 实例计算器类
   #     cal = Calculator()
   #     # 调用add方法
   #     result = cal.add(-1, -3)
   #     # 得到结果后，需要写断言
   #     assert result == -4
