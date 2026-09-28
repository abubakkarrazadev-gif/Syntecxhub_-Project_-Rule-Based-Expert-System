"""
Facts Base
----------
Stores the initial facts provided by the user.
"""


class FactBase:
    def __init__(self, facts=None):
        """Initialize the fact base."""
        self.facts = set(facts or [])

    def add_fact(self, fact):
        """Add a new fact to the fact base."""
        self.facts.add(fact)

    def add_facts(self, facts):
        """Add multiple facts."""
        self.facts.update(facts)

    def has_fact(self, fact):
        """Check whether a fact exists."""
        return fact in self.facts

    def has_all(self, facts):
        """Check whether all required facts exist."""
        return all(fact in self.facts for fact in facts)

    def get_all(self):
        """Return all facts."""
        return set(self.facts)

    def __contains__(self, fact):
        """Allow: if fact in fact_base."""
        return fact in self.facts

    def __len__(self):
        """Return number of facts."""
        return len(self.facts)