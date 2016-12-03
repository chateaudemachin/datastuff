# Data Science and the Nations Event Data
Data used during the event [Data Science meets the Nations](https://www.facebook.com/events/1804163043167931/).
## Requirements
Please make sure that you have *Python* and *pip* are installed on your machine.
It would be good to have some libraries to manipulate and analyse data like _numpy_, _scipy_, _scikit-learn_ and _matplotlib_.
Once you have *pip* installed you can install a library by doing:
```pip install library-name```

## Data Structure
All the data is stored in CSV format.
### Uplands Nation Event Attendance Data
This data is present under the folder _event_data/_.

Each filename in the _event_data/_ folder is in form: **_[DATE]_ + _[NAME]_.csv**. The first line of each file is a header in the form: "Name,Status", while the rest of the rows contain names and statuses of people attending the event on Facebook.
The status can be either of the following: *Going*, *Maybe* or *Invited*.

For example the event _Cleaning Day II_ that happened on the 6th of March is stored in the file **"MAR 6 Cleaning Day II"**. The first lines of this file look like this:
```
Name,Status
"Anton Lönnebo",Going
"Annie Ekman",Going
"Daniel Ahlbom",Going
"Måns Bergkvist",Going
"Gabriel Granbacka",Going
"Dóra Dombovári",Going
"Gábor Kertész",Going
"Sebastian Andersson Kurko",Going
```

### Purchase Data from Foobar
This data is present in the file _purchase_data/purchases.csv_.

The first lines of this file look like this:
```purchase_id,product_id,name,qty,date_created
"4996478d-d93d-4c53-bc6f-55dcc9c141b1","883ecf58-3504-4eca-bc8d-6f30aea70bbc","Kaffe","1","2016-09-01 06:25:30.236768+00"
"ae331889-aa15-434d-92ec-9b31910fc9c9","883ecf58-3504-4eca-bc8d-6f30aea70bbc","Kaffe","1","2016-09-01 06:52:53.590181+00"
"b0558914-58ff-456b-993d-0091d5f22b0d","883ecf58-3504-4eca-bc8d-6f30aea70bbc","Kaffe","1","2016-09-01 07:50:50.680759+00"
```
