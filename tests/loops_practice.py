class LoopsPractice:
    def numbers(self):
        numbers = list(range(1, 8))
        for i in numbers:
            if i == 5:
                break
            print(i)

    def words(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)
