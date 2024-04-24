# HWSETA_test24
## TITLE: Developer Test
#### author: HWSETA Systems





#### Instructions
* Download the Odoo base Module
- You will need the starting module to begin the test from https://github.com/ashertee/HWSETA_test24
- Fork the repository to you local machine and download the odoo module from the github location above
- 
* Install Odoo
 The test will require Odoo 12. You will need to install it and then copy the module into your installation.
 You can Odoo 12 from:
[https://www.odoo.com/page/download]
 
* Scenario
Learners need to be registered against qualifications, each of those qualifications has a set of unit standards.
Each of those unit standards have credits tied to them.

Your task is to fill in the missing elements in the provided Odoo module.
* Tasks
##### Adding Field to the Learner Class
Add a field to the Learner Class that links the Learner to the Qualification Master Table.
##### Note:
Qualifications from the Master Table can be re-used multiple times for multiple learners
###### add field to qual master table that shows minimum credits required to pass
###### compare the minimum credits to the credits achieved by learner based on which unit standards are achieved to determine if the qualification is achieved
###### add a status field for these qualifications, to show a pass or fail state
###### In the master table of qualifications, we need a function (get_total_credits) that fetches a sum of all the unit standards attached to the qualification, and the result needs to be put into the total_credit field
###### Create a function that will check if the learner has the same id_number as another learner 
###### Create five qualifications
###### The first qualification is Computer Science, minimum pass mark is 20
###### It has 3 unit standards (101, 102, 103) of 10 credits each
###### The second qualification is Accounting, minimum pass mark is 15
###### It has 3 unit standards (101, 102, 103) of 8 credits each
###### The third qualification is Agriculture, minimum pass mark is 12
###### It has 3 unit standards (101, 102, 103) of 6 credits each
###### The fourth qualification is Vetinery Nursing, minimum pass mark is 12
###### It has 3 unit standards (101, 102, 103) of 6 credits each
###### The fifth qualification is Data Science, minimum pass mark is 30
###### It has 3 unit standards (101, 102, 103) of 10 credits each


##### Create three learners

###### The first learner is Dylan
###### Dylan applied for Computer Science, and passed 101 and 102
###### Dylan applied for Accounting, and passed 101
###### The second learner is Dean
###### Dean applied for Computer Science, and passed 101 and 103
###### Dean applied for Accounting, and passed 101 and 102
###### The third learner is Carol
###### Carol applied for Agriculture, and passed 101 and 103
###### Carol applied for Vetinery Nursing, and passed 101 and 102
###### Carol applied for Data Science, and passed 101 and 102
##### export a list of passed and failed qualifications

    
##### Bonus Points
###### import another learner with any 2 qualifications, of which one is a pass and one is a fail based on the unit standards that have been imported
###### any additional items added to the module that were not in the instructions will be graded accordingly

* Submission of Test
  ##### Once you have completed the test and ready to submit, Create a pull request of your forked repo with your name as the commit message
  ##### Then after, provide a database dump of your database, your exported files, and your completed module in zip format. Email all of your files to: tafadzwam@hwseta.org.za
