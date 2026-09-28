"""
Main Application
----------------
Command-line interface for the Rule-Based Expert System.
"""

from expert_system import ExpertSystem
from rules import RULES


# ============================================================
# DISPLAY FUNCTIONS
# ============================================================

def display_header():
    """Display the application header."""

    print("\n" + "=" * 60)
    print("             RULE-BASED EXPERT SYSTEM")
    print("=" * 60)

    print("\nThis system uses:")
    print("  • IF-THEN rules")
    print("  • Facts")
    print("  • Forward chaining")
    print("  • Multi-step inference")
    print("  • Inference logging")


def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 60)
    print("MAIN MENU")
    print("=" * 60)

    print("1. Start Inference")
    print("2. View Available Rules")
    print("3. View Available Facts")
    print("4. Exit")


# ============================================================
# RULE DISPLAY
# ============================================================

def display_rules():
    """Display all rules in the knowledge base."""

    print("\n" + "=" * 60)
    print("AVAILABLE RULES")
    print("=" * 60)

    for rule in RULES:

        print(f"\n{rule.rule_id} - {rule.name}")

        print(
            f"IF {rule.get_condition_text()}"
        )

        print(
            f"THEN {rule.conclusion}"
        )

        print(
            f"Description: {rule.description}"
        )

    print("\n" + "=" * 60)


# ============================================================
# FACT DISPLAY
# ============================================================

def display_available_facts():
    """Display facts that the user can provide."""

    facts = set()

    for rule in RULES:
        facts.update(rule.conditions)

    print("\n" + "=" * 60)
    print("AVAILABLE FACTS / SYMPTOMS")
    print("=" * 60)

    for fact in sorted(facts):
        print(f"  • {fact}")

    print("\n" + "=" * 60)


# ============================================================
# USER INPUT
# ============================================================

def get_user_facts():
    """
    Ask the user to enter facts one at a time.

    The user types 'done' when finished.
    """

    print("\n" + "=" * 60)
    print("ENTER FACTS / SYMPTOMS")
    print("=" * 60)

    print("\nEnter one fact at a time.")
    print("Type 'done' when you have finished.")

    facts = set()

    while True:

        user_input = input("\nEnter fact: ").strip().lower()

        if user_input == "done":
            break

        if not user_input:
            print("Please enter a fact.")
            continue

        if user_input in facts:
            print(
                f"'{user_input}' is already in the fact base."
            )
            continue

        facts.add(user_input)

        print(
            f"Added fact: {user_input}"
        )

    return facts


# ============================================================
# RESULT DISPLAY
# ============================================================

def display_conclusions(
    initial_facts,
    final_facts
):
    """Display newly inferred conclusions."""

    new_facts = (
        final_facts -
        set(initial_facts)
    )

    print("\n" + "=" * 60)
    print("INFERRED CONCLUSIONS")
    print("=" * 60)

    if not new_facts:

        print("\nNo new conclusions were inferred.")

        return

    for conclusion in sorted(new_facts):

        print(
            f"  → {conclusion}"
        )


def display_final_knowledge_base(final_facts):
    """Display all facts after inference."""

    print("\n" + "=" * 60)
    print("FINAL KNOWLEDGE BASE")
    print("=" * 60)

    for fact in sorted(final_facts):

        print(
            f"  • {fact}"
        )


# ============================================================
# INFERENCE
# ============================================================

def start_inference():
    """Start an inference session."""

    initial_facts = get_user_facts()

    if not initial_facts:

        print("\nNo facts were provided.")

        return

    print("\n" + "=" * 60)
    print("STARTING EXPERT SYSTEM")
    print("=" * 60)

    system = ExpertSystem(RULES)

    final_facts = system.forward_chain(
        initial_facts
    )

    system.display_reasoning()

    display_conclusions(
        initial_facts,
        final_facts
    )

    display_final_knowledge_base(
        final_facts
    )

    print("\n" + "=" * 60)
    print("INFERENCE SESSION COMPLETED")
    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    display_header()

    while True:

        display_menu()

        choice = input(
            "\nSelect an option (1-4): "
        ).strip()

        if choice == "1":

            start_inference()

        elif choice == "2":

            display_rules()

        elif choice == "3":

            display_available_facts()

        elif choice == "4":

            print("\nThank you for using the Rule-Based Expert System.")

            print("\nProgram terminated.")

            break

        else:

            print(
                "\nInvalid option."
                " Please select 1, 2, 3, or 4."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()