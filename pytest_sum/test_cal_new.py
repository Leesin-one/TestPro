import allure
import pytest

@allure.feature("测试计算器")
class TestCalcator():

    @pytest.mark.run(order=0)
    @allure.story("测试加法")
    def test_add(self,test_scope,get_cal,get_add_datas):
        # try:
        # self.cal = Calculator()
        # cal = Calculator()
        with allure.step("两数相加"):
            result = get_cal.add(get_add_datas[0],get_add_datas[1])
        # except Exception as e :
        #     print(e)
        if isinstance(result,float):
            result=round(result,2)
        assert  result == get_add_datas[2]

    # @pytest.mark.parametrize("sub1,sub2,sub_sum",sub_datas,ids=sub_ids)
    @pytest.mark.run(order=1)
    @allure.story("测试减法")
    def test_sub(self,test_scope,get_cal,get_sub_datas):
        # self.cal = Calculator()
        with allure.step("两数相减"):
            sub_result = get_cal.sub(get_sub_datas[0],get_sub_datas[1])
        if isinstance(sub_result,float):
           sub_result = round(sub_result,2)
        assert sub_result == get_sub_datas[2]

    # @pytest.mark.parametrize("mul_1,mul_2,mul_sum",mul_datas,ids=mul_ids)
    @pytest.mark.run(order=2)
    @allure.story("测试乘法")
    def test_mul(self,test_scope,get_cal,get_mul_datas):
        with allure.step("两数相乘"):
            mul_result = get_cal.mul(get_mul_datas[0],get_mul_datas[1])
        if isinstance(mul_result,float):
           mul_result = round(mul_result,2)
        assert mul_result == get_mul_datas[2]

    @pytest.mark.usefixtures("test_scope")
    @pytest.mark.run(order=3)
    @allure.story("测试除法")
    def test_div(self,get_cal, get_div_datas):
        try:
            with allure.step("两数相除"):
                div_result = get_cal.div(get_div_datas[0], get_div_datas[1])
        except Exception as e:
            print(e)
            if isinstance(div_result, float):
               div_result = round(div_result, 2)
        assert div_result == get_div_datas[2]

