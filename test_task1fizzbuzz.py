import task1fizzbuzz as t


class TestTask1fizzbuzz:
    def test_fizz_buzz_fizz(self):
        assert t.fizz_buzz(3) == 'Fizz'

    def test_fizz_buzz_buzz(self):
        assert t.fizz_buzz(5) == 'Buzz'
