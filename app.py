import os

import streamlit as st

from crew import run_customer_support_crew


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Customer Support System",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🤖 AI Customer Support System")

st.markdown(
    """
    ### Three-Agent Sequential AI Workflow

    **Agent 1** → Direct Answer  
    **Agent 2** → Web Research  
    **Agent 3** → Save Conversation
    """
)

st.divider()


# ============================================================
# CUSTOMER QUERY
# ============================================================

st.subheader("💬 Customer Query")

customer_query = st.text_area(
    "Enter your question or support request:",
    height=150,
    placeholder=(
        "Example: What is CrewAI and how is it used?"
    )
)


# ============================================================
# BUTTON
# ============================================================

submit_button = st.button(
    "🚀 Submit Query",
    type="primary",
    use_container_width=True
)


# ============================================================
# PROCESS
# ============================================================

if submit_button:

    if not customer_query.strip():

        st.warning(
            "Please enter a customer query."
        )

        st.stop()


    # ========================================================
    # PROGRESS DISPLAY
    # ========================================================

    st.divider()

    st.subheader(
        "⚙️ Agent Workflow"
    )

    progress_placeholder = st.empty()


    # ========================================================
    # PROGRESS CALLBACK
    # ========================================================

    def update_progress(
        stage,
        status,
        message
    ):

        if stage == "agent1":

            progress_placeholder.info(
                "🤖 **Agent 1** — " + message
            )

        elif stage == "agent2":

            progress_placeholder.info(
                "🌐 **Agent 2** — " + message
            )

        elif stage == "agent3":

            progress_placeholder.info(
                "💾 **Agent 3** — " + message
            )

        elif stage == "tasks":

            progress_placeholder.info(
                "📋 " + message
            )

        elif stage == "crew":

            progress_placeholder.info(
                "⚙️ " + message
            )

        elif stage == "complete":

            progress_placeholder.success(
                "✅ " + message
            )


    # ========================================================
    # EXECUTE CREW
    # ========================================================

    try:

        result = run_customer_support_crew(
            customer_query,
            progress_callback=update_progress
        )


    except Exception as e:

        progress_placeholder.error(
            "❌ Workflow failed."
        )

        st.exception(e)

        st.stop()


    # ========================================================
    # RESULTS
    # ========================================================

    st.divider()

    st.header(
        "📋 Support Results"
    )


    # ========================================================
    # CUSTOMER QUERY
    # ========================================================

    with st.expander(
        "💬 Customer Query",
        expanded=True
    ):

        st.write(
            customer_query
        )


    # ========================================================
    # AGENT 1
    # ========================================================

    st.subheader(
        "🤖 Agent 1 — Direct Answer"
    )

    st.info(
        result["agent1_answer"]
    )


    # ========================================================
    # AGENT 2
    # ========================================================

    st.subheader(
        "🌐 Agent 2 — Web Research Answer"
    )

    st.success(
        result["agent2_answer"]
    )


    # ========================================================
    # AGENT 3
    # ========================================================

    st.subheader(
        "💾 Agent 3 — Documentation"
    )

    st.success(
        result["agent3_answer"]
    )


    # ========================================================
    # DOWNLOAD FILE
    # ========================================================

    file_path = (
        "output/customer_support_history.txt"
    )


    if os.path.exists(file_path):

        st.divider()

        st.subheader(
            "📄 Conversation History"
        )

        with open(
            file_path,
            "rb"
        ) as file:

            st.download_button(
                label="⬇️ Download Conversation History",
                data=file,
                file_name="customer_support_history.txt",
                mime="text/plain",
                use_container_width=True
            )

        st.success(
            "Conversation saved successfully."
        )