# dtu-api

[Unofficial Scraper API](https://dtu-api.vercel.app/) for [Delhi Technological University (DTU) Website](http://dtu.ac.in)

API Link : https://dtu-api.vercel.app/api

Scrapes the following information from [Official DTU Website](http://dtu.ac.in) :
    - Page Title
    - Current Note
    - Imporatant Updates
    - Current Events
    - Latest News
    - First Year Notices
    - Notices
    - Jobs
    - Tenders
    - Registeration Schedule

---

## Deployment

API is deployed on Vercel. Check out the [API Usage & it's output](https://dtu-api.vercel.app/api)

To deploy on your own, follow the following steps :
    <ol>
        <li>Fork this repository on your system</li>
        <li>Make sure you have [installed Vercel CLI](https://vercel.com/cli)</li>
        <li>Open the repository in your terminal</li>
        <li>Run command `vercel --prod` and follow the instructions</li>
    </ol> 

---

## Output

Kindly [refer to sample.json](./sample.json) for understanding using a compact prettified JSON Output of the Scraper API.


The output for every field is in either one of the two formats :
    
```json
{
    "name" : "Title of information",
    "link" : "link_to_information"
}
```

<center>OR</center>

```json
{
    "name": "Title of information",
    "sub_list": [
        {
            "name": "Title of sub-information 1",
            "link": "link_to_information"
        },
        {
            "name": "Title of sub-information 2",
            "link": "link_to_information"
        } // and so on...
    ]
}
```