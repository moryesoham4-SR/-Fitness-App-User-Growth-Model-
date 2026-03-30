import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="Fitness App Growth Model", layout="wide")
st.title("💪 Fitness App User Growth Model")

# =========================
# USER INPUT FORM
# =========================
st.sidebar.header("📥 Enter Parameters")

with st.sidebar.form("input_form"):
    initial_users = st.number_input("Initial Users", min_value=100)
    days = st.slider("Days", 7, 365)

    retention_rate = st.slider("Retention Rate", 0.0, 1.0)
    churn_rate = st.slider("Churn Rate", 0.0, 1.0)
    new_user_ratio = st.slider("New User Ratio", 0.0, 1.0)

    submit = st.form_submit_button("🚀 Run Model")

# =========================
# RUN ONLY AFTER INPUT
# =========================
if submit:

    data = []
    current_users = initial_users

    for day in range(days):
        retained_users = current_users * retention_rate
        dropouts = current_users * churn_rate
        new_users = current_users * new_user_ratio

        predicted_users = retained_users + new_users - dropouts

        data.append([
            day + 1,
            current_users,
            new_users,
            retained_users,
            dropouts,
            predicted_users
        ])

        current_users = predicted_users

    df = pd.DataFrame(data, columns=[
        "Day", "Current Users", "New Users",
        "Retained Users", "Dropouts", "Predicted Users"
    ])

    # =========================
    # METRICS
    # =========================
    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="Fitness App Growth Model", layout="wide")
st.title("💪 Fitness App User Growth Model")

# =========================
# USER INPUT FORM
# =========================
st.sidebar.header("📥 Enter Parameters")

with st.sidebar.form("input_form"):
    initial_users = st.number_input("Initial Users", min_value=100)
    days = st.slider("Days", 7, 365)

    retention_rate = st.slider("Retention Rate", 0.0, 1.0)
    churn_rate = st.slider("Churn Rate", 0.0, 1.0)
    new_user_ratio = st.slider("New User Ratio", 0.0, 1.0)

    submit = st.form_submit_button("🚀 Run Model")

# =========================
# RUN ONLY AFTER INPUT
# =========================
if submit:

    data = []
    current_users = initial_users

    for day in range(days):
        retained_users = current_users * retention_rate
        dropouts = current_users * churn_rate
        new_users = current_users * new_user_ratio

        predicted_users = retained_users + new_users - dropouts

        data.append([
            day + 1,
            current_users,
            new_users,
            retained_users,
            dropouts,
            predicted_users
        ])

        current_users = predicted_users

    df = pd.DataFrame(data, columns=[
        "Day", "Current Users", "New Users",
        "Retained Users", "Dropouts", "Predicted Users"
    ])

    # =========================
    # METRICS
    # =========================
    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)

    col1.metric("Initial Users", initial_users)
    col2.metric("Final Users", int(df["Predicted Users"].iloc[-1]))
    col3.metric("Days", days)

    # =========================
    # GRAPHS
    # =========================
    st.subheader("📈 Visualizations")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Growth", "New Users", "Retained", "Dropouts", "Combined"
    ])

    with tab1:
        fig1, ax1 = plt.subplots()
        ax1.plot(df["Day"], df["Current Users"], label="Current Users")
        ax1.plot(df["Day"], df["Predicted Users"], label="Predicted Users")
        ax1.legend()
        st.pyplot(fig1)

    with tab2:
        fig2, ax2 = plt.subplots()
        ax2.plot(df["Day"], df["New Users"])
        st.pyplot(fig2)

    with tab3:
        fig3, ax3 = plt.subplots()
        ax3.plot(df["Day"], df["Retained Users"])
        st.pyplot(fig3)

    with tab4:
        fig4, ax4 = plt.subplots()
        ax4.plot(df["Day"], df["Dropouts"])
        st.pyplot(fig4)

    with tab5:
        fig5, ax5 = plt.subplots()
        ax5.plot(df["Day"], df["New Users"], label="New Users")
        ax5.plot(df["Day"], df["Retained Users"], label="Retained")
        ax5.plot(df["Day"], df["Dropouts"], label="Dropouts")
        ax5.legend()
        st.pyplot(fig5)

    # =========================
    # DATA TABLE
    # =========================
    st.subheader("📋 Data Table")
    st.dataframe(df)

    st.download_button("⬇️ Download CSV", df.to_csv(index=False), "data.csv")

# =========================
# BEFORE INPUT MESSAGE
# =========================
else:
    st.info("👈 Please enter values in sidebar and click 'Run Model'")
(3)

    col1.metric("Initial Users", initial_users)
    col2.metric("Final Users", int(df["Predicted Users"].iloc[-1]))
    col3.metric("Days", days)

    # =========================
    # GRAPHS
    # =========================
    st.subheader("📈 Visualizations")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Growth", "New Users", "Retained", "Dropouts", "Combined"
    ])

    with tab1:
        fig1, ax1 = plt.subplots()
        ax1.plot(df["Day"], df["Current Users"], label="Current Users")
        ax1.plot(df["Day"], df["Predicted Users"], label="Predicted Users")
        ax1.legend()
        st.pyplot(fig1)

    with tab2:
        fig2, ax2 = plt.subplots()
        ax2.plot(df["Day"], df["New Users"])
        st.pyplot(fig2)

    with tab3:
        fig3, ax3 = plt.subplots()
        ax3.plot(df["Day"], df["Retained Users"])
        st.pyplot(fig3)

    with tab4:
        fig4, ax4 = plt.subplots()
        ax4.plot(df["Day"], df["Dropouts"])
        st.pyplot(fig4)

    with tab5:
        fig5, ax5 = plt.subplots()
        ax5.plot(df["Day"], df["New Users"], label="New Users")
        ax5.plot(df["Day"], df["Retained Users"], label="Retained")
        ax5.plot(df["Day"], df["Dropouts"], label="Dropouts")
        ax5.legend()
        st.pyplot(fig5)

    # =========================
    # DATA TABLE
    # =========================
    st.subheader("📋 Data Table")
    st.dataframe(df)

    st.download_button("⬇️ Download CSV", df.to_csv(index=False), "data.csv")

# =========================
# BEFORE INPUT MESSAGE
# =========================
else:
    st.info("👈 Please enter values in sidebar and click 'Run Model'")