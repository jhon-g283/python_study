# _テストのコードを自動で検知してくれる(pytestで実行)
# テスト対象の関数
def add(x, y):
    return x + y


# テストコード
def test_add():
    # ケースを実行
    res = add(1, 2)
    assert res == 3

def test_add2():
    # ケースを実行
    res = 0
    assert res == 34