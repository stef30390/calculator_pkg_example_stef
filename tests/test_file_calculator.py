from calculator_pkg_example_stef.file_calculator import FileCalculator


def test_file_calculator() -> None:
    assert FileCalculator().add_file() == 6.0, "Add File failed!"