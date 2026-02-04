import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Disbursement Dashboard",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("## 📊 Dashboard")

# ---------------- KPI ROW ----------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "This Month Disbursement",
    "₹ 16,70,000",
    "-94.2% vs Last Month"
)

kpi2.metric(
    "Outstanding Amount",
    "₹ 16,23,07,807",
    "+10,000"
)

kpi3.metric(
    "Overdue Amount",
    "₹ 1,94,61,728",
    "-1,000"
)

kpi4.metric(
    "Active Borrowers",
    "1,532",
    "+5"
)

st.markdown("---")

# ---------------- TREND DATA ----------------
months = ["OCT", "NOV", "DEC", "JAN", "FEB"]

approved = [1900000, 2050000, 2300000, 2600000, 2200000]
disbursed = [1800000, 2100000, 2400000, 2700000, 2150000]

col1, col2 = st.columns(2)

# ---------------- LOAN APPROVED ----------------
with col1:
    fig, ax = plt.subplots()
    ax.plot(months, approved, marker="o")
    ax.set_title("Loan Approved – Monthly Trend")
    ax.set_ylabel("Amount (₹)")
    st.pyplot(fig)

# ---------------- LOAN DISBURSEMENT ----------------
with col2:
    fig, ax = plt.subplots()
    ax.plot(months, disbursed, marker="o")
    ax.set_title("Loan Disbursement – Monthly Trend")
    ax.set_ylabel("Amount (₹)")
    st.pyplot(fig)

st.markdown("---")

# ---------------- RECOVERY SECTION ----------------
r1, r2, r3 = st.columns(3)

r1.metric(
    "This Month Recovery",
    "₹ 98,79,522",
    "+10.6%"
)

r2.metric(
    "This Month Due Recovery",
    "₹ 9,87,952",
    "+10,001"
)

r3.metric(
    "Total Due Recovery",
    "₹ 19,54,629",
    "No Change"
)

st.markdown("---")

# ---------------- PENDING CASES ----------------
st.subheader("Pending Cases")

p1, p2, p3, p4 = st.columns(4)

p1.metric("Pending FI", "0", "Last Month: 0")
p2.metric("Pending PL", "4", "+4 New")
p3.metric("Pending CAM", "2", "Same")
p4.metric("Pending TVR", "3", "Same")

st.markdown("---")

# ---------------- UPDATES ----------------
allow, cal = st.columns([2, 1])

with allow:
    st.subheader("Updates")
    st.info(
        "IFS – Integrated Finance Solutions is a tested and proven solution "
        "built using the latest technology framework and includes Android-based "
        "mobility solutions tailored for finance operations."
    )

with cal:
    st.subheader("📅 Calendar")
    st.date_input("Select Date")

# ---------------- FOOTER ----------------
st.caption("© 2026 Integrated Finance Solutions | MIS Dashboard")
