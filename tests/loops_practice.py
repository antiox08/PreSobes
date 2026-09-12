class LoopsPractice:
    def numbers(self) -> None:
        numbers = list(range(1, 8))
        for i in numbers:
            print(i)
            if i == 5:
                break

    def words(self) -> None:
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    def value(self) -> None:
        num = [x**2 for x in range(5) if x > 3]
        print(num)
