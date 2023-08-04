# Book Library 
   [View the life project here.](https://book-library-2e28b631fcb4.herokuapp.com/)

The aim of this web application is simply to provide the user a site whereby they can view an online record of their book library. The user can upload books they have purchaed or read and update the status of what categories of books they are interested in, own, and are seeking to read. This online library is designed to be an accesible and easy to use library to help keep track of your books through categories and descriptions. 

![Screenshot 2023-08-04 203201](https://github.com/magz-dev/book-library/assets/97630146/fd76bc94-131a-4ee1-805d-3669bd81ba6f)

## User Experience (UX)
### User Stories
#### First Time Visitor Goals
a. As a First Time Visitor, I want to easily understand the main purpose of the site.

b. As a First Time Visitor, I want to be able to easily navigate throughout the site to find the relevant content.

#### Returning Visitor Goals
a. As a Returning Visitor, I want to find information about the books I am reading.

b. As a Returning Visitor, I want to be able to view the details of my books.

#### Frequent User Goals
a. As a Frequent User, I want to be able to add, update, or delete my book records and descriptions.

## Features
* Resposive on all devices
* [Wireframes](https://github.com/magz-dev/book-library/files/12264668/New.Project.1.pdf)
  
### Frameworks, Libraries & Programs Used
* Bootstrap 4
* Git
* GitHub
* Balsamiq
* Flask
* SQLAlchemy
* Psycopg2
* Postgresql
  
### Languages Used
* HTML5
* CSS3
* Python
  
## Testing
The PEP8 checker, W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
![Screenshot 2023-08-04 002310](https://github.com/magz-dev/book-library/assets/97630146/aba652b3-6357-4642-9c04-c0105cd9984a)


### Further Testing

* Developer Tools - Lighthouse report:
  
![Screenshot 2023-08-04 223652](https://github.com/magz-dev/book-library/assets/97630146/af1943b7-c5a8-4fdc-84e4-28e204a959b4)


![Screenshot 2023-08-04 223056](https://github.com/magz-dev/book-library/assets/97630146/e2944f20-f8ca-4593-bbdf-ed4af857d22f)

* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone and Android mobile devices.
* A large amount of testing was done to ensure that all pages were working correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
* On some mobile devices the 'sumbit' button on the form for adding new books is partially covered by copyright footer.
  
## Deployment
#### The project was deployed to Heroku. The steps to deploy are as follows:
1. Navigate to the “Deploy” tab of your app.
2. In the Deployment method section, select “Connect to GitHub”.
3. Search for your repo and click Connect.
4. Now click "Enable Automatic Deploys" to ensure that any changes made on GitHub are automatically deployed on Heroku.
5. Click "Deploy Branch".
6. Now, we have our project in place, and we have an empty database ready for use. Click the “More” button and select “Run console”.
7. Type python3 into the console and click Run.
* Let’s now create the tables with the commands we used before:
  `from taskmanager import db`
  `db.create_all()`
  `exit()`
8. The app should be up and running now, so click the “Open app” button.
  


### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository.
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
7. Press Enter. Your local clone will be created.



## Credits
### Code
* Bootstrap 4 - Bootstrap Library used throughout the project to add style. Bootstrap 4 was also used to make the site responsive by using the Bootstrap Grid System.
* [W3Schools]((https://www.w3schools.com/default.asp))
* Code Institute's learning content
  
### Media
* The background photo was taken from a non-copyrighted google image search.

### Acknowledgements
* Tutor support from the Code Institute.
* My Mentor for helpful comments and supportive feedback.

  



















    















