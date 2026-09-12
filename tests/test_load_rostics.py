import random


def test_load_simulation_runs_ten_iterations() -> None:
    """Учебный пример цикла без time.sleep()."""
    count = 0
    while count < 10:
        load = random.randint(0, 100)
        assert 0 <= load <= 100
        count += 1
    assert count == 10
