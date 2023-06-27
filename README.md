# SOS Web Application

For deployment the https://www.pythonanywhere.com/ has been used

As a database choice; sqlite has been used.

# Deployed URL is as follows:
## http://appinstance26.pythonanywhere.com/

Purpose of this application is to reach people seeking assistance during times of crisis.
--

# User Side
Users can register and log in to the platform.

By navigating in navbar various actions can be done which is sending request and donations.

Registered & Logged in user can request the items that is provided by the company.

Donations can also be made which is handled in database.

For donations there is no need to create an account and private data is not mandatory

---

# Admin Side
There is also an Admin portal to manage the procurement process according to the inventory data
and follow/delete the incoming donations or requests.

---
Since Django has been used as backend service, the data can be edited and managed through the url:

# Django Admin Page
## http://appinstance26.pythonanywhere.com/admin
### <font color="coral"> Credentials are provided in a seperate file! </font>

# Webpage Admin Page
This part is to monitor and follow the data flow. It can be reached by navigating to the Admin Portal on navigation bar which is the URL:

## http://appinstance26.pythonanywhere.com/administration/

* On this part the inventory, donations and requests can be viewed and deleted.


* Moreover procurement has been implemented where you can order missing items if enough cash is available. Otherwise it is not possible. Moreover, different suppliers have different rates for the items so the expected cost is calculated on procurement page.


* Inventory system has also been implemented where requests can be met only if enough item is available in inventory.


* Donation system is also working where you can donate items that increases the quantities in inventory. When cash has been donated it is multiplyed by the currency and send to the inventory as Turkish Lira.


* Report system has been implemented. For this part we have used PowerBI, hence, <font color="coral"> to view the report in a dynamic way where filtering is possible log-in into the powerbi via metu mail may be required.</font> The screenshot of the report has been provided in 'report_queries' folder under 'app-instance-26' folder if it cannot be viewed. The sql queries to retrieve the required performance measure is also been provided under 'report_queries' folder.