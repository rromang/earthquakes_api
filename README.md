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

7. 

