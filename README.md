**User-Keep API**
-----------------------
A flask api with MongoDB database for saving users and their details.

**Description**
---------------
This web api is developed using flask and will use a Mongo Database for storing the data entered by the user.

**API reference**
------------------
- /admin/create_user
  - Method - POST
  - #send a post request with the body containing user details as a json formatted string to save a new user in database

- /admin/get_users
  - Method - GET
  - #send a get request to view the all user details saved

- /admin/get_user/<user_id>
  - Method - GET
  - #send a get request to view the details of a single user specified by object_id.
  - #object_id is assigned to every user object saved in MongoDB
 
- /admin/update/<user_id>
  - Method - PUT
  - #send a put request to change the user details specified by object id. You have to send the details to be changed in form of a json string

- /admin/delete/<user_id>
  - Method - DELETE
  - #send a DELETE request to delete the user details specified by object id.

**Requirements**
----------------
- Python (3.8 or above)
- Flask, PyMongo packages.
- A mongodb (local or Mongo Atlas, change it with any mongodb service in file test1/admin_component/bp1.py

**How to run the server**
--------------------------

  python test_main.py
