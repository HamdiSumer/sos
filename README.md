# SOS Web Application Guideline

For deployment the https://www.pythonanywhere.com/ has been used

As a database choice; sqlite has been used.

# Deployed URL is as follows:
## http://appinstance26.pythonanywhere.com/

# Used DB Model:


![image](https://github.com/HamdiSumer/sos/assets/58032358/12cfc54a-7650-4b3f-8274-22b69fcd0628)

This is the structure of our database on Django side. We have used DJANGO ORM to communicate between tables and insert/edit/delete them.
---
Purpose of this application is to reach people seeking assistance during times of crisis.
---

# User Side
## Main Page


![image](https://github.com/HamdiSumer/sos/assets/58032358/01725744-bb61-4233-9432-018c75a3b297)

Users can register and log in to the platform.


![image](https://github.com/HamdiSumer/sos/assets/58032358/fd32a4e8-8974-4661-98a4-3180e36173e3)


![image](https://github.com/HamdiSumer/sos/assets/58032358/bee5dcf5-3f7e-451f-96cd-34628e9b17dc)

By navigating in navbar various actions can be done which is sending request and donations.

Registered & Logged in user can request the items that is provided by the company.


![image](https://github.com/HamdiSumer/sos/assets/58032358/1fbcb04e-9972-470a-ba7a-de6f0bc4e2d9)


Donations can also be made which is handled in database.


![image](https://github.com/HamdiSumer/sos/assets/58032358/aa6ba685-ffb9-4995-bf75-9852f269c434)

For donations there is no need to create an account and private data is not mandatory

---

# Admin Side
There is also an Admin portal to manage the procurement/donation/inventory process according to the 
inventory data and follow/insert/delete/retrieve the incoming donations or requests.

---
Since Django has been used as backend service, the data can be edited and managed through the url:

# Django Admin Page
## http://appinstance26.pythonanywhere.com/admin
### <font color="coral"> Credentials are provided in a seperate file! </font>


![image](https://github.com/HamdiSumer/sos/assets/58032358/824f67cc-5e6f-4cbc-b7cd-d4f3ee85c3ef)


# Webpage Admin Page


![image](https://github.com/HamdiSumer/sos/assets/58032358/27b25dc2-428d-41ce-a915-1002025a6006)

This part is to monitor and follow the data flow. It can be reached by navigating to the 
Admin Portal on navigation bar which is the URL:

## http://appinstance26.pythonanywhere.com/administration/

* On this part the inventory, donations and requests can be viewed and deleted.


* Moreover procurement has been implemented where you can order missing items if enough cash is available.
Otherwise it is not possible. Moreover, different suppliers have different rates for the items so the
expected cost is calculated on procurement page.


![image](https://github.com/HamdiSumer/sos/assets/58032358/6f136095-32e2-43c4-bd47-50754e88d081)


* Inventory system has also been implemented where requests can be met only if enough
item is available in inventory.


![image](https://github.com/HamdiSumer/sos/assets/58032358/514af2c1-740f-4728-ae43-1e5959ad7dde)


* Donation system is also working where you can donate items that increases the quantities in
inventory. When cash has been donated it is multiplyed by the currency and send to the inventory as Turkish Lira.


![image](https://github.com/HamdiSumer/sos/assets/58032358/e4cee2d3-9e20-4d33-9e6e-c25f718af814)


* Report system has been implemented. For this part we have used PowerBI, hence, <font color="coral"> to
view the report in a dynamic way where filtering is possible log-in into the powerbi via metu mail may be required.</font> The
screenshot of the report has been provided in 'report_queries' folder under 'app-instance-26' folder if it cannot be viewed.
The sql queries to retrieve the required performance measure is also been provided under 'report_queries' folder.
* The Report looks like this if you cannot enter via metu mail on power bi:


 ![image](https://github.com/HamdiSumer/sos/assets/58032358/9937285c-7876-407d-8c5d-7c1cab0d36a7)
