# Crowdfunding Back End

Catherine Blentweyne

## Planning

### bandtogethr

bandtogthr is a platform to raise funds to get international metal bands to come to include Perth on their tour downunder.

### Intended Audience/User Stories

This site is inteded to help international (and interstate) heavy metal bands to come to Perth. It is designed to support bands with smaller audiences that would not be able to tour Perth and is not intended for high-profile or mainstream metal bands that would perform in large venues.  

At present (Django sprint) a member of a band can create a band, and a tour for their band. There is only one owner.
It is planned to implement in future deployments the option for any band member to create a tour and have a verification method to ensure only bands meeting the criteria are using the site.

Individuals (supporters) can pledge to any open campaign.

### Front End Pages/Functionality

- Home page
  - Recently added tours
  - Recently added bands
  - Login/Sign-up link
  - If user logged in, suggested bands/tours based on selected genres
  - All of above would provide option to 'view all', or click directly on item to view details
- Login / Sign-up page
  - Enter sign-in details for existing users
  - Enter details to create an account
- Bands page
  - Displays all bands listed on website, with options to filter by various options e.g. genre, open tour, etc
  - Each band listing links to band details page
- Band details page
  - Displays info on invidiual band
  - Option to make pledge (if current open tour)
- Tours page
  - Displays all tours listed on website, with options to filter by various options e.g. genre, open tour, etc. Default is open tours.
  - Each tour listing links to tour details page
- Tour details page
  - Displays info on invidiual bantourd
  - Option to make pledge (if current open tour)

### API Spec

{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page.

It might look messy here in the PDF, but once it's rendered it looks very neat!

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL          | HTTP Method | Purpose                                                             | Request Body | Success Response Code             | Authentication/Authorisation                                       |
| ------------ | ----------- | ------------------------------------------------------------------- | ------------ | --------------------------------- | ------------------------------------------------------------------ |
| /home/  | GET | 
| /projects/   | GET         | Return all projects                                                | Request body | 200                               | N/A                                                                |
| /projects/   | POST        | Creates new project                                                 | Request body | 201                               | Must be logged in                                                  |
| /projects/1/ | GET         | Returns project with ID of '1'                                      | Request body | 200                               | N/A                                                                |
| /projects/1/ | PUT         | Updates project with ID of '1'                                      | Reqest body  | 200                               | Must be logged in; and must be project owner (or admin or band ???) |
| /projects/1/ | DELETE      | Deletes project project with ID of '1' (and all associated plenges) | Request body | Must be logged in and must be ??? |
| /pledges/    | POST        | Create new pledge                                                   | Request body | 201                               | Must be logged in                                                  |
| /pledges/<?> | GET         | Returns all pledges of logged in user                               | Request body | 200                               | Must be logged in and pledge owner                                 |

### DB Schema

![]( {{ ./relative/path/to/your/schema/image.png }} )
