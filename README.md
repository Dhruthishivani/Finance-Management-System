# Finance-Management-System

**Functionalities included in the application**

● Users can log their daily expenses

● Expenses are categorized (e.g., "Food," "Transport," "Entertainment").

● Users can set monthly budgets for each category.

● The system alerts users if they exceed their budget for the category.

● Show Total spending per month

● Compare spending vs budget per category

● Allowing users to have different budgets for different months

● Custom alerts, example: alert user when only 10% budget is left

● Email notifications to user for alert

● Allowing users to share expenses, amongst a group

**Steps to execute the project are as follows**

1) Clone the repository
2) Inside vscode terminal, do pip install streamlit
3) To get email notification, go to https://myaccount.google.com/apppasswords

Select:
App → Mail
Device → Windows / Other
Click Generate
Google will give you a 16-digit password which has to be pasted in the line no 6 of email_alert.py file 

4) In terminal run:  streamlit run expense_tracker.py

**Steps to operate the application:**

**1) From the left dropdown menu, select "Set Budget" and add the below data individually and save the budget**  

Month :2025-11

Food:10,000 

Transport:5,000 

Entertainment :5000

Shopping:2500 

Bills :7500

Message will pop up as "Budget Saved Successfully"

**2) From the left dropdown menu , select "Add Expenses" and add the following data**

Adjust the Alert me when budget reaches (%) to 70%
Date: (choose date of November from the calendar)

Amount:500,
Category:Bills

Amount:400,
Category:Bills

Amount:400,
Category:Bills

Since the Alert me when budget reaches (%) is 70% , email notification will be received on reaching 3500rs. The same email notification can be received on other categories as well.

**3) Adding values in Shopping category**


Amount:400,
Category:Shopping

Amount:899,
Category:Shopping


Amount:2000,
Category:Shopping
 
**4) Adding values in Shopping Food**

Amount:200,
Category:Food

Amount:200,
Category:Food

Amount:400,
Category:Food

**5) Adding values in Entertainment category**

Amount:400,
Category:Entertainment

Amount:700,
Category:Entertainment

Amount:350,
Category:Entertainment

**6) Adding values in transport category**

Amount:350,
Category:transport

Amount:400,
Category:transport

Amount:250,
Category:transport


**7) After adding these values, select the Reports section from the left drop down menu, and enter 2025-11. Then all the reports per category will be category 
The total amount spent, amount spent on each category and if the budget per category is exceeded or not, all of these will be shown**


**8) Select on the group expenses dropdown from the left and the Group Expense Sharing option will be available** 

Create Group Name: "demo",
Add Member Email: (add email) ,
Group ID: "123",
Group Expense Amount:"1200"



