class LoopsPractice:
    def numbers(self):
        numbers = list(range(1, 8))
        for i in numbers:
            if i == 5:
                break
            print(i)

practice = LoopsPractice()
practice.numbers()