#!/usr/bin/python3.4
# coding: utf-8

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开应用首页
        self.browser.get('http://localhost:8000')

        # 标题和头部包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 应用邀请他输入一个待办事项

        # 他在一个文本框中输入"Buy peacock feathers"

        # 按回车后,页面更新
        # 待办事项中显示"1: Buy peacock feathers"

        # 页面中又显示了一个文本框,可以输入其他待办事项
        # 输入"Use peacock feathers to make a fly"

        # 页面再次更新,清单中显示了这两个单板事项

        # 网站生成唯一URL
        # 页面中有文字解说这个功能

        # 访问那个URL,待办事项还在


if __name__ == '__main__':
    unittest.main(warnings='ignore')
