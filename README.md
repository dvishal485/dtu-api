# dtu-api

[Unofficial Scraper API](https://dtu-api.vercel.app/) for [Delhi Technological University (DTU) Webpage](http://dtu.ac.in) and [results page](http://exam.dtu.ac.in/result.htm)

API Link : https://dtu-api.vercel.app/

Scrapes the following information from [Official DTU Webpage](http://dtu.ac.in) :
<ul>
    <li>Page Title</li>
    <li>Last Updated Date & Time</li>
    <li>Top Menu Bar</li>
    <li>Menu Bar</li>
    <li>Sliding Image Showcase</li>
    <li>Side Menu</li>
    <li>Current Note</li>
    <li>Imporatant Updates</li>
    <li>Current Events</li>
    <li>Latest News</li>
    <li>First Year Notices</li>
    <li>Notices</li>
    <li>Jobs</li>
    <li>Tenders</li>
    <li>Registeration Schedule</li>
</ul>

About the results, the scraper extracts the following from [results webpage](http://exam.dtu.ac.in/result.htm) :
<ul>
    <li>Exam Name</li>
    <li>Details</li>
    <li>Serial Number</li>
    <li>Date</li>
</ul>

This all pretty much sums up the whole webpage contents!

---

## Usage

API output have been classified into two different types :

1. To extract the usually required data which usually is <b>variable over time</b>, use `api` link : [https://{server_url}/api](https://dtu-api.vercel.app/api)

1. To extract data for full webpage ( required for cloning the webpage ) which is usually <b>constant over time</b>, use the `webpage` link : [https://{server_url}/webpage](https://dtu-api.vercel.app/webpage)

1. To obtain details for results' page, use the `exam` link, [refer to https://{server_url}/exam](https://dtu-api.vercel.app/exam)

---

## Deployment

API is deployed on Vercel. Check out the [API Usage](#usage) and [Output formats](#output_formats)


- Deploy on vercel directly through deployment button

    [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fdvishal485%2Fdtu-api)

- To deploy to vercel on your own, follow the following steps :
    <ol>
        <li>Fork this repository on your system</li>
        <li>Make sure you have <a href="https://vercel.com/cli">installed Vercel CLI</a></li>
        <li>Open the repository in your terminal</li>
        <li>Run command <code>vercel --prod</code> and follow the instructions</li>
    </ol> 

- To deploy on `localhost` or on `VPS` :

    1. Install python requirements

        ```
        pip install -r requirements.txt
        ```

    2. Execute [server.py](./server.py)

        ```
        python server.py
        ```
        or
        ```
        python3 server.py
        ```

---

## Output Formats

Kindly [refer to sample.json](./sample.json) for understanding using a compact prettified JSON Output of the Scraper API ([Variable Data API](#usage))


The output for the `api` and `webpage` for every field is in either one of the two formats or simply a string :
    
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
            "sub_list": [
                {
                    "name": "Title of sub-information 1",
                    "link": "link_to_information"
                },
            ]
        }
    ]
}
```

If the output is for an image sample, then output will be in format :
```json
{
    "name": "Name of image",
    "image_link": "link_of_image"
}
```

For `exam` link, [directly refer to an example](https://dtu-api.vercel.app/exam).

---

## License & Copyright

  - This Project is [Apache-2.0](./LICENSE) Licensed
  - Copyright 2021 [Vishal Das](https://github.com/dvishal485)