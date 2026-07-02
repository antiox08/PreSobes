import random
import time


class LoadTesting:

    def test_load_testing_rostics(self) -> None:
        count = 0
        while count < 10:
            load = random.randint(0, 100)

            print(f"Current load: {load}%")

            if load > 85:
                print("Too much load detected")
            time.sleep(0.2)
            count += 1


practice = LoadTesting()
practice.test_load_testing_rostics()
