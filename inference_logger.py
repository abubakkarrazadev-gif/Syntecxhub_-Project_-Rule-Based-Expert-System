"""
Inference Logger
----------------
Records and displays the reasoning path generated
by the forward-chaining inference engine.
"""


class InferenceLogger:

    def __init__(self):
        """Initialize an empty inference history."""

        self.steps = []

    def log(
        self,
        rule,
        facts_before,
        conclusion
    ):
        """
        Record one inference step.

        Args:
            rule: Rule that was fired.
            facts_before: Facts available before the rule fired.
            conclusion: Newly inferred fact.
        """

        step_number = len(self.steps) + 1

        step = {
            "step": step_number,
            "rule_id": rule.rule_id,
            "rule_name": rule.name,
            "conditions": sorted(rule.conditions),
            "conclusion": conclusion,
            "description": rule.description,
            "facts_before": sorted(facts_before)
        }

        self.steps.append(step)

    def get_steps(self):
        """Return all recorded inference steps."""

        return list(self.steps)

    def clear(self):
        """Clear the inference history."""

        self.steps.clear()

    def display(self):
        """Display the complete inference reasoning path."""

        print("\n" + "=" * 60)
        print("INFERENCE / REASONING PATH")
        print("=" * 60)

        if not self.steps:
            print("\nNo rules were fired.")
            print("=" * 60)
            return

        for step in self.steps:

            print(
                f"\nStep {step['step']}"
            )

            print("-" * 50)

            print(
                f"Rule ID: {step['rule_id']}"
            )

            print(
                f"Rule: {step['rule_name']}"
            )

            print("\nConditions:")

            for condition in step["conditions"]:
                print(
                    f"  ✓ {condition}"
                )

            print("\nConclusion:")

            print(
                f"  → {step['conclusion']}"
            )

            if step["description"]:

                print("\nDescription:")

                print(
                    f"  {step['description']}"
                )

        print("\n" + "=" * 60)