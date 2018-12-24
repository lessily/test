import allure

allure.step('我是测试步骤')
class Test:

    def test_a(self):
        print('\n aaa')
        allure.attach('描述', '我是测试步骤003的描述～～～')
        assert 1


    def test_b(self):

        print('\n bbb')
        allure.attach('描述', '我是测试步骤001的描述～～～')
        print('\n ccc')
        allure.attach('描述', '我是测试步骤002的描述～～～')


        assert 0