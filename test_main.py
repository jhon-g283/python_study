import unittest # testのためのライブラリ
import testTarget # test対象のライブラリ

class TestFunc(unittest.TestCase): # テストのためのクラス
    def test_func(self): # 関数テストのためのメソッド
        value1 = 1 # 引数1
        value2 = 2 # 引数2
        expected = 3 # 期待値
        actual = testTarget.func(value1, value2) # 関数実行結果
        self.assertEqual(expected, actual) # 合否判断（結果比較）
    def test_func2(self): # 関数テストのためのメソッド
        value1 = 1 # 引数1
        value2 = 1 # 引数2
        expected = False # 期待値
        actual = testTarget.func2(value1, value2) # 関数実行結果
        self.assertEqual(expected, actual) # 合否判断（結果比較）

if __name__ == '__main__':
    unittest.main()