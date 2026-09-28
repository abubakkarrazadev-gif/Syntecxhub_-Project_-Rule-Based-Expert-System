"""
Rule Definitions
----------------
Contains the Rule class and the knowledge base
used by the expert system.
"""


class Rule:
    """
    Represents an IF-THEN rule.

    Example:

        IF fever AND cough
        THEN respiratory_infection
    """

    def __init__(
        self,
        rule_id,
        name,
        conditions,
        conclusion,
        description=""
    ):
        self.rule_id = rule_id
        self.name = name
        self.conditions = set(conditions)
        self.conclusion = conclusion
        self.description = description

    def can_fire(self, facts):
        """
        Check whether all conditions required by
        this rule are present in the fact base.
        """

        return self.conditions.issubset(facts)

    def get_condition_text(self):
        """Return conditions as readable text."""

        return " AND ".join(
            sorted(self.conditions)
        )

    def __str__(self):
        """Return a readable IF-THEN representation."""

        return (
            f"IF {self.get_condition_text()} "
            f"THEN {self.conclusion}"
        )


# ==================================================
# KNOWLEDGE BASE
# ==================================================

RULES = [

    Rule(
        rule_id="R1",
        name="Respiratory Infection Rule",
        conditions=[
            "fever",
            "cough"
        ],
        conclusion="respiratory_infection",
        description=(
            "Infers a possible respiratory infection "
            "when fever and cough are present."
        )
    ),

    Rule(
        rule_id="R2",
        name="Flu Rule",
        conditions=[
            "respiratory_infection",
            "sore_throat"
        ],
        conclusion="flu",
        description=(
            "Infers flu when a respiratory infection "
            "and sore throat are present."
        )
    ),

    Rule(
        rule_id="R3",
        name="Influenza Rule",
        conditions=[
            "flu",
            "body_ache"
        ],
        conclusion="likely_influenza",
        description=(
            "Infers likely influenza when flu and "
            "body ache are present."
        )
    ),

    Rule(
        rule_id="R4",
        name="Viral Infection Rule",
        conditions=[
            "fever",
            "fatigue"
        ],
        conclusion="possible_viral_infection",
        description=(
            "Infers a possible viral infection when "
            "fever and fatigue are present."
        )
    ),

    Rule(
        rule_id="R5",
        name="Respiratory Problem Rule",
        conditions=[
            "cough",
            "shortness_of_breath"
        ],
        conclusion="possible_respiratory_problem",
        description=(
            "Infers a possible respiratory problem "
            "when cough and shortness of breath are present."
        )
    ),

    Rule(
        rule_id="R6",
        name="Medical Attention Rule",
        conditions=[
            "possible_respiratory_problem",
            "fever"
        ],
        conclusion="requires_medical_attention",
        description=(
            "Infers that medical attention may be required "
            "when a respiratory problem and fever are present."
        )
    ),
]