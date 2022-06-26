# API for Earthquake Information

## Main idea:
> While working for one of the final projects for the Data Analytics Bootcamp last year, my teammates and I  encountered that some of the datasets available were not as large as we would've like. We chose our project to be related to earthquakes. The main reason: the USGS has readily available data from their website. However, when wanting to download data, it is basically limited to about 2 months worth of data, if wanting to include events with very low magnitude. I decided to test how to create and deply an API that was updated somewhat regularly with the monthly data from USGS.


### Objectives:

+ Obtain the information from: https://www.usgs.gov/programs/earthquake-hazards/earthquakes
+ Place the information collected as part of a database to be accessed for data exploration, data visualization,training the model(s), etc.
+ Create and deploy an API with the information.
+ Regularly maintain the database and the API by updating and adding the new earthquake information so the dataset is relatively large.

### Steps:

1. Import the necessary dependencies.

![Screen Shot 2022-06-26 at 12 17 33 PM](https://user-images.githubusercontent.com/80008461/175830394-798e23df-83f6-462c-81ce-1cd753b9e3a1.png)

2. Database were created ahead of time for a different project. Connect to the databases and access the data.

![Screen Shot 2022-06-26 at 12 19 31 PM](https://user-images.githubusercontent.com/80008461/175830606-44c7e5b6-778d-4c14-bd33-ba2f798f433b.png)


3. Read table from database.

![Screen Shot 2022-06-26 at 12 23 40 PM](https://user-images.githubusercontent.com/80008461/175830610-a867c461-50b6-4084-aad8-0f9a77455433.png)


4. Get additional data from USGS website.

![Screen Shot 2022-06-26 at 12 26 27 PM](https://user-images.githubusercontent.com/80008461/175830674-fd1b9a2b-e6d5-4aaa-9cd7-c155e75acbaf.png)

5. Append the new data to database.

![Screen Shot 2022-06-26 at 12 28 01 PM](https://user-images.githubusercontent.com/80008461/175830728-ef0c82bf-94bb-421d-8cf1-3430138ad93f.png)

6. Read the updated table from database.

![Screen Shot 2022-06-26 at 12 29 00 PM](https://user-images.githubusercontent.com/80008461/175830772-632c7521-9fc3-41fa-87c8-6de337839cc1.png)

7. Since the USGS given id is unique it can be used to double check duplicate values.

![Screen Shot 2022-06-26 at 1 04 14 PM](https://user-images.githubusercontent.com/80008461/175832046-d8c68944-fec1-4206-af68-605664806a21.png)

8. Drop any duplicates found.

![Screen Shot 2022-06-26 at 1 08 42 PM](https://user-images.githubusercontent.com/80008461/175832078-06eb128d-4a57-487e-9b02-b30b0bc334cf.png)

9. Update database to remove duplicates by replacing the table. (Note: A duplicated table should be created in the database before any replacing in case something catastrophic happens. However, I chose to keep a backup as a csv file.) (Note: After data base is updated in jupyter notebook. Open SQLite studio an update the primary key, if using sqlite and/or make sure the id column is used as a primary key in pgadmin)

![Screen Shot 2022-06-26 at 1 10 11 PM](https://user-images.githubusercontent.com/80008461/175832169-977631cc-9d95-43fc-9e9d-5a279f874951.png)
![Screen Shot 2022-06-26 at 1 13 59 PM](https://user-images.githubusercontent.com/80008461/175832214-d09ceaf3-3c5d-44dc-baa6-7cf958d3691a.png)
![Screen Shot 2022-06-26 at 1 14 08 PM](https://user-images.githubusercontent.com/80008461/175832217-b55479c5-df5d-4633-bdfa-9e0f231aa8c4.png)

10. 

