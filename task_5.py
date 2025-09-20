class TestCase:

    def __init__(self):
        self.steps = {}
        self.result = None

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        print("{")
        print("    'Шаги': {")
        sorted_steps = sorted(self.steps.items())
        for i, (step_num, step_text) in enumerate(sorted_steps):
            if i < len(sorted_steps) - 1:
                print(f"            {step_num}: '{step_text}', ")
            else:
                print(f"            {step_num}: '{step_text}'")
        print("    }, ")
        print(f"    'Ожидаемый результат': '{self.result}'")
        print("}")
        print()
