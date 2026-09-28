"""
Streamlit GUI
-------------
Graphical interface for the Rule-Based Expert System.
"""

import streamlit as st

from expert_system import ExpertSystem
from rules import RULES


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Rule-Based Expert System",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🧠 Rule-Based Expert System")

st.write(
    "A rule-based inference system using "
    "IF-THEN rules and forward chaining."
)

st.info(
    "Educational demonstration: conclusions are "
    "generated only from the configured rules."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("System Information")

st.sidebar.write("The system uses:")

st.sidebar.write("• Facts")
st.sidebar.write("• IF-THEN Rules")
st.sidebar.write("• Forward Chaining")
st.sidebar.write("• Multi-Step Inference")
st.sidebar.write("• Inference Logging")


# ============================================================
# INITIAL USER FACTS
# ============================================================

initial_facts = [
    "fever",
    "cough",
    "sore_throat",
    "body_ache",
    "fatigue",
    "shortness_of_breath"
]


# ============================================================
# FACT SELECTION
# ============================================================

st.header("1. Select Initial Facts")

selected_facts = st.multiselect(
    "Choose the facts/symptoms provided by the user:",
    options=initial_facts
)


# ============================================================
# RUN INFERENCE
# ============================================================

col1, col2 = st.columns(2)

with col1:
    run_inference = st.button(
        "🚀 Run Inference",
        type="primary",
        use_container_width=True
    )

with col2:
    clear_selection = st.button(
        "🗑️ Clear Selection",
        use_container_width=True
    )

if clear_selection:
    st.rerun()

if run_inference:

    if not selected_facts:

        st.warning(
            "Please select at least one fact."
        )

    else:

        # Create a fresh expert system
        system = ExpertSystem(RULES)

        # Run forward chaining
        final_facts = system.forward_chain(
            set(selected_facts)
        )

        # Get reasoning history
        inference_log = system.get_inference_log()

        # ====================================================
        # INITIAL FACTS
        # ====================================================

        st.header("2. Initial Facts")

        for fact in sorted(selected_facts):

            st.write(
                f"🔵 `{fact}`"
            )

        # ====================================================
        # INFERRED CONCLUSIONS
        # ====================================================

        st.header("3. Inferred Conclusions")

        inferred_facts = (
            final_facts -
            set(selected_facts)
        )

        if inferred_facts:

            for fact in sorted(inferred_facts):

                st.success(
                    f"✓ {fact}"
                )

        else:

            st.info(
                "No new conclusions were inferred."
            )

        # ====================================================
        # INFERENCE / REASONING PATH
        # ====================================================

        st.header("4. Inference / Reasoning Path")

        if not inference_log:

            st.info(
                "No rules were triggered."
            )

        else:

            for step in inference_log:

                with st.expander(
                    f"Step {step['step']} — "
                    f"{step['rule_id']} — "
                    f"{step['rule_name']}",
                    expanded=True
                ):

                    st.write("**Conditions:**")

                    for condition in step["conditions"]:

                        st.write(
                            f"✓ `{condition}`"
                        )

                    st.write(
                        f"**Conclusion:** "
                        f"`{step['conclusion']}`"
                    )

                    st.write(
                        f"**Description:** "
                        f"{step['description']}"
                    )

        # ====================================================
        # FINAL KNOWLEDGE BASE
        # ====================================================

        st.header("5. Final Knowledge Base")

        for fact in sorted(final_facts):

            st.write(
                f"• `{fact}`"
            )


# ============================================================
# RULE REFERENCE
# ============================================================

st.divider()

st.header("Available Rules")

for rule in RULES:

    with st.expander(
        f"{rule.rule_id} — {rule.name}"
    ):

        st.write(
            f"**IF:** `{rule.get_condition_text()}`"
        )

        st.write(
            f"**THEN:** `{rule.conclusion}`"
        )

        st.write(
            f"**Description:** {rule.description}"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Rule-Based Expert System | "
    "Forward Chaining Demonstration"
)