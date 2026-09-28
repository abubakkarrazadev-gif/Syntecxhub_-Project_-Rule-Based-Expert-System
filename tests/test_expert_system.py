import sys
import os
import unittest

# Add the main project directory to Python's import path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)

from expert_system import ExpertSystem
from rules import RULES


class TestExpertSystem(unittest.TestCase):

    def setUp(self):
        """Create a fresh expert system before every test."""

        self.system = ExpertSystem(RULES)

    # ========================================================
    # TEST 1
    # ========================================================

    def test_single_rule(self):
        """Test the first inference rule."""

        facts = {
            "fever",
            "cough"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "respiratory_infection",
            final_facts
        )

    # ========================================================
    # TEST 2
    # ========================================================

    def test_two_step_inference(self):
        """Test two levels of forward chaining."""

        facts = {
            "fever",
            "cough",
            "sore_throat"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "respiratory_infection",
            final_facts
        )

        self.assertIn(
            "flu",
            final_facts
        )

    # ========================================================
    # TEST 3
    # ========================================================

    def test_three_step_inference(self):
        """Test complete three-step inference."""

        facts = {
            "fever",
            "cough",
            "sore_throat",
            "body_ache"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "respiratory_infection",
            final_facts
        )

        self.assertIn(
            "flu",
            final_facts
        )

        self.assertIn(
            "likely_influenza",
            final_facts
        )

    # ========================================================
    # TEST 4
    # ========================================================

    def test_no_matching_rule(self):
        """Test when no rule can be triggered."""

        facts = {
            "headache"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertEqual(
            final_facts,
            {"headache"}
        )

    # ========================================================
    # TEST 5
    # ========================================================

    def test_duplicate_fact(self):
        """Test that duplicate facts are handled."""

        facts = [
            "fever",
            "fever",
            "cough",
            "cough"
        ]

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "fever",
            final_facts
        )

        self.assertIn(
            "cough",
            final_facts
        )

        self.assertIn(
            "respiratory_infection",
            final_facts
        )

    # ========================================================
    # TEST 6
    # ========================================================

    def test_viral_infection_rule(self):
        """Test R4: fever + fatigue."""

        facts = {
            "fever",
            "fatigue"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "possible_viral_infection",
            final_facts
        )

    # ========================================================
    # TEST 7
    # ========================================================

    def test_respiratory_problem_rule(self):
        """Test R5: cough + shortness of breath."""

        facts = {
            "cough",
            "shortness_of_breath"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "possible_respiratory_problem",
            final_facts
        )

    # ========================================================
    # TEST 8
    # ========================================================

    def test_medical_attention_multi_step(self):
        """
        Test R5 followed by R6.

        cough + shortness_of_breath
                    ↓
        possible_respiratory_problem
                    ↓
        + fever
                    ↓
        requires_medical_attention
        """

        facts = {
            "fever",
            "cough",
            "shortness_of_breath"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "possible_respiratory_problem",
            final_facts
        )

        self.assertIn(
            "requires_medical_attention",
            final_facts
        )

    # ========================================================
    # TEST 9
    # ========================================================

    def test_original_facts_are_preserved(self):
        """Test that original user facts remain in the knowledge base."""

        facts = {
            "fever",
            "cough",
            "sore_throat"
        }

        final_facts = self.system.forward_chain(facts)

        self.assertIn(
            "fever",
            final_facts
        )

        self.assertIn(
            "cough",
            final_facts
        )

        self.assertIn(
            "sore_throat",
            final_facts
        )

    # ========================================================
    # TEST 10
    # ========================================================

    def test_inference_log_created(self):
        """Test that inference steps are recorded."""

        facts = {
            "fever",
            "cough",
            "sore_throat",
            "body_ache"
        }

        self.system.forward_chain(facts)

        log = self.system.get_inference_log()

        self.assertEqual(
            len(log),
            3
        )

        self.assertEqual(
            log[0]["rule_id"],
            "R1"
        )

        self.assertEqual(
            log[1]["rule_id"],
            "R2"
        )

        self.assertEqual(
            log[2]["rule_id"],
            "R3"
        )


# ============================================================
# TEST RUNNER
# ============================================================

if __name__ == "__main__":
    unittest.main()