**SearchEngine Using ElasticSearch**

This Repository includes the frontend,backend implementation for a search query. After configuring the elasticsearch, the sample search engine is use to try the query searches hosting using flask framework.

**Directoryy Structure**

|--templetes : The resultpage for UI

|--app.py : Flask backend to have transactions with Elasticsearch APIs

|--bulkdata.py : Python file that converts JSON to a bulkdata and index to ElasticSearch using Bulk API

|--query.py : ElasticSearch search queries inclusive of advanced queries.

|--search.py : Search API call

|--generateBenchmarking.py : It generates two sets of data - present and - notpresent. I have done basic experiment for Name and PhoneNumber.

**Demo**
* Install ElasticSearch
* Run ElasticSearch
* Run 'bulkdata.py' to add index(uncomment indexing part if not manually addded) and add data
* Run app.py and go to http://127.0.0.1:8000/ which host search portal.
* Search for data. If seaarching using fieldname,provide fieldname:query.


