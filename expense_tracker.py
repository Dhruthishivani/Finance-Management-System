import streamlit as st
import datetime
from database import *
from email_alert import send_email_alert

create_tables()

st.title("💰 Smart Expense Tracker Pro")

user = st.text_input("Enter your Email")

menu = st.sidebar.selectbox("Menu", ["Add Expense", "Set Budget", "Group Expense", "Reports"])

# ---------------- ADD EXPENSE ----------------
if menu == "Add Expense":
    st.header("Add Expense")

    amount = st.number_input("Amount", min_value=1.0)
    category = st.selectbox("Category", ["Food","Transport","Entertainment","Shopping","Bills"])
    date = st.date_input("Date")
    month = date.strftime("%Y-%m")

    alert_percent = st.slider("Alert me when budget reaches (%)", 50, 100, 90)

    if st.button("Add"):
        add_expense(user, None, amount, category, str(date), month)

        budget = get_budget(user, category, month)
        spending = sum(x[1] for x in get_category_spending(user, month) if x[0] == category)

        if budget > 0:
            if spending >= (alert_percent / 100) * budget:
                msg = f"You have used {spending} of your {budget} {category} budget."
                try:
                    send_email_alert(user, msg)
                    st.warning("⚠️ Alert Sent to Email!")
                except:
                    st.error("❌ Email failed! Check Gmail App Password.")


        st.success("Expense Added Successfully")

# ---------------- SET BUDGET (MONTHWISE) ----------------
elif menu == "Set Budget":
    st.header("Set Monthly Budget")

    month = st.text_input("Month (YYYY-MM)", datetime.date.today().strftime("%Y-%m"))
    category = st.selectbox("Category", ["Food","Transport","Entertainment","Shopping","Bills"])
    budget = st.number_input("Budget Amount", min_value=1.0)

    if st.button("Save Budget"):
        set_budget(user, category, month, budget)
        st.success("Budget Saved Successfully")

# ---------------- GROUP EXPENSE (SPLITWISE) ----------------
elif menu == "Group Expense":
    st.header("Group Expense Sharing")

    group_name = st.text_input("Create Group Name")
    if st.button("Create Group"):
        gid = create_group(group_name)
        st.success(f"Group Created with ID {gid}")

    member = st.text_input("Add Member Email")
    gid = st.number_input("Group ID", step=1)

    if st.button("Add Member"):
        add_member(gid, member)
        st.success("Member Added")

    g_amount = st.number_input("Group Expense Amount")
    if st.button("Add Group Expense"):
        add_expense(user, gid, g_amount, "Group", str(datetime.date.today()), datetime.date.today().strftime("%Y-%m"))
        st.success("Group Expense Added")

# ---------------- REPORTS ----------------
elif menu == "Reports":
    st.header("📊 Monthly Expense Report")

    month = st.text_input(
        "Enter Month (YYYY-MM)",
        datetime.date.today().strftime("%Y-%m")
    )

    if st.button("Generate Report"):
        data = get_category_spending(user, month)

        if not data:
            st.warning("⚠️ No expenses found for this month.")
        else:
            # ✅ 1. TOTAL MONTHLY SPENDING
            total_spent = sum(x[1] for x in data)
            st.subheader(f"💰 Total Spending for {month}: ₹ {total_spent}")

            st.write("---")
            st.subheader("📂 Category-wise Spending vs Budget")

            # ✅ 2. CATEGORY-WISE BREAKDOWN
            for cat, spent in data:
                budget = get_budget(user, cat, month)

                st.write(f"### {cat}")
                st.write(f"✅ Spent: ₹ {spent}")
                st.write(f"🎯 Budget: ₹ {budget}")

                # ✅ 3. WITHIN / OVER BUDGET STATUS
                if budget == 0:
                    st.info("ℹ️ No budget set for this category")
                elif spent > budget:
                    st.error("❌ Status: Over Budget")
                else:
                    st.success("✅ Status: Within Budget")

                st.write("---")

