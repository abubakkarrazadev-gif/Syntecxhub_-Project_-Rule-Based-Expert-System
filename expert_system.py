"""
Expert System
-------------
Generic forward-chaining inference engine.
"""

from facts import FactBase
from inference_logger import InferenceLogger


class ExpertSystem:

    def __init__(self, rules):
        """
        Initialize the expert system.

        Args:
            rules: List of Rule objects.
        """

        self.rules = rules
        self.logger = InferenceLogger()

    def forward_chain(self, initial_facts):
        """
        Perform forward chaining.

        The engine starts with the user's initial facts
        and repeatedly applies rules whose conditions
        are satisfied.

        Each newly inferred conclusion becomes a new fact.

        The process continues until no additional
        facts can be inferred.
        """

        # Create a fresh fact base
        fact_base = FactBase(initial_facts)

        # Clear previous inference history
        self.logger.clear()

        # Keep track of rules that have already fired
        fired_rules = set()

        print("\nInitial Facts:")

        for fact in sorted(fact_base.get_all()):
            print(f"  - {fact}")

        print("\nStarting forward chaining...")

        while True:

            new_fact_added = False

            for rule in self.rules:

                # Skip rules that have already fired
                if rule.rule_id in fired_rules:
                    continue

                # Check whether all rule conditions exist
                if rule.can_fire(fact_base.get_all()):

                    # Store facts before inference
                    facts_before = fact_base.get_all()

                    # Add the rule to the fired set
                    fired_rules.add(rule.rule_id)

                    # Add the conclusion as a new fact
                    if rule.conclusion not in fact_base:

                        fact_base.add_fact(
                            rule.conclusion
                        )

                        # Record the inference
                        self.logger.log(
                            rule=rule,
                            facts_before=facts_before,
                            conclusion=rule.conclusion
                        )

                        print(
                            f"\n[Rule Fired] {rule.name}"
                        )

                        print(
                            f"  {rule}"
                        )

                        print(
                            f"  New Fact: {rule.conclusion}"
                        )

                        new_fact_added = True

            # If no new fact was produced,
            # inference is complete.
            if not new_fact_added:
                break

        print("\nForward chaining completed.")

        return fact_base.get_all()

    def get_inference_log(self):
        """
        Return the inference history.
        """

        return self.logger.get_steps()

    def display_reasoning(self):
        """
        Display the complete reasoning path.
        """

        self.logger.display()