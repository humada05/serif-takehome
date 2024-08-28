TLDR: The code is a python script which can take arguments `python keyword_parser.py <input file> <output file> <keywords>...`. For setup, please run these commands:

```bash
git clone [REPO]
cd [REPO]
python -m virtualenv env
source venv/bin/activate
pip install -r requirements.txt
python keyword_parser.py input.json output.json "New York" "PPO"
```

# Serif take-home task
I began by downloading the file directly from the provided link: [Anthem Index JSON](https://antm-pt-prod-dataz-nogbd-nophi-us-east1.s3.amazonaws.com/anthem/2024-08-01_anthem_index.json.gz)


![image info](./pics/file_explorer.png)

Uncompressed, this JSON file is over 20GB! Way too big to even open in a normal text editor. And even though I have an idea of what to expect based off the table of contents provided, I still like to get my hands dirty and look through the data directly. To do this, I went ahead and fetched the first 100 and 1000 lines and put them into two separate files for me to play around with. 

A simple way to achieve this is by using the `head` and `tail` commands to save the output into a file:
```bash
head -n 100 2024-08-01_anthem_index.json > example.json # Fetch the first 100 lines and save them to a file
tail -n 1 2024-08-01_anthem_index.json >> example.json # Fetch and append the last line to complete the JSON
```

With a more manageable file size, we can start by reformatting the data to pretty print the JSON:
```json
{
    "reporting_entity_name": "Anthem Inc",
    "reporting_entity_type": "health insurance issuer",
    "reporting_structure": [
        {
            "reporting_plans": [
                {
                    "plan_name": "ENTPRS DIABETS - PARTNER FUND SERVICES LLC - ANTHEM",
                    "plan_id_type": "EIN",
                    "plan_id": "822089386",
                    "plan_market_type": "group"
                },
                {
                    "plan_name": "LIVE HEALTH ONLINE - PARTNER FUND SERVICES LLC - ANTHEM",
                    "plan_id_type": "EIN",
                    "plan_id": "822089386",
                    "plan_market_type": "group"
                },
                {
                    "plan_name": "PRUDENT BUYER PPO - PARTNER FUND SERVICES LLC - ANTHEM",
                    "plan_id_type": "EIN",
                    "plan_id": "822089386",
                    "plan_market_type": "group"
                },
                {
                    "plan_name": "K HEALTH - PARTNER FUND SERVICES LLC - ANTHEM",
                    "plan_id_type": "EIN",
                    "plan_id": "822089386",
                    "plan_market_type": "group"
                }
            ],
            "in_network_files": [
                {
                    "description": "Florida Blue: BCBS Florida : PPC / PPO Network",
                    "location": "https://anthembcca.mrf.bcbs.com/2024-08_590_10G0_in-network-rates_1_of_2.json.gz?&Expires=1726840840&Signature=09AIyFddAYxKPefRcPGFkozY64td6uYIzoNwijgPGMIuQoI0GkRckSyXWwTayFuMB0mRTTVEWrFstkS3SHYNV94cDpvtURI4gMPQ0cMRScH2htIrBH2EDkOVQjAW2g2lra5yNUZRIxzjMSkIvywhLpwB9CuJNB-PhurfAOoQQ4HsVbXWiSStTSEoWoQkuww0ZRjGb9P6DAqsi0oVB7rUf9KXOWNW8DQqXokgGG~yrbfNQu0zKshytTDuE8qOVr3hr7IArOjmJ5gnqYi1RFB4-Kfit3OdxlQJ-KT7NW-7VgP8OFazRv3fYbzWAI0wBoxz0Ld8XVJFRZuGht~4gXV2bQ__&Key-Pair-Id=K27TQMT39R1C8A"
                },
                {
                    "description": "BCBS Alabama : Preferred Care",
                    "location": "https://anthembcca.mrf.bcbs.com/2024-08_510_01B0_in-network-rates_24_of_29.json.gz?&Expires=1726840840&Signature=ervhRW7L0rYKSQXT~nA7JqlZyEw383AwF7XckPnvjlqIwcrd6~5nqKUFcRoh14MSypATxmw6Cre9ZXeRUk4Pn5PMkZeH4N4UCPw3F9WspyTzc5bnaBSjisVbNKxUEymiXEkmuqjaCV28Ke3MFGFfN07YYDFjdWWUAzyOmiK54LMFQ3zqODHORRKc2avDVn0kH4wMMw4gKCHIiUDiS1uhEM3Mo0WtdAGSDJ4AYQoizabStTGNr7gtMtL2XUOsZ-rpVmpqqMMZepshHmSCVPe~ynOQLiYx-5I0ZJ37sxgGeNNeQV0UjJIo6OcAHSlcgDMgArTMEzg2Emk5Kc3mP~I~Lw__&Key-Pair-Id=K27TQMT39R1C8A"
                },
                {
                    "description": "CareFirst BCBS : Select Preferred Provider",
                    "location": "https://anthembcca.mrf.bcbs.com/2024-08_690_08B0_in-network-rates_9_of_35.json.gz?&Expires=1726840840&Signature=iZIixEMv3YTQvEfMJtSXh-4laO~dXnkqozO34ye1XPi7ILazpP8WA7AkfByWeUw7YxnRxNU1ihb5i4XeQL8UlnTEEmz8BWYFm3YMDwSttSWfUIdMjvK19ReSKlcxOcyZGz8HgZXP8HFtB~6VSJ2rG556vIRa5Ve9vkGrCUPGAKo81hYpxN4aaYOsH~DOgQZDZbN28RX35zDQFydBkikVuI~dzKG9c7wKRQu1bl-lEu1HF7e2EVYTYGPaByDWsAiy7S5rDECrJYpOvlE5k6IPT~xopxo-7pEpnEg7tsm6ILAdipuKeT3kGz2MCNYvDlfram-zD0MnvTa8K6RN-dDIeg__&Key-Pair-Id=K27TQMT39R1C8A"
                },
                {
                    "description": "BCBS Alabama : Preferred Care",
                    "location": "https://anthembcca.mrf.bcbs.com/2024-08_510_01B0_in-network-rates_27_of_29.json.gz?&Expires=1726840840&Signature=dfy7dHkQOIlcnFD5G1rCl9lgkTEao05bUnUeSTWlgAt69yYYSE-lud-w2~L3SngRY8f3jJXYr5HAzmCP2NOHI7EDECFRpwQNrOruYNc~a60HMrU9DwJ1pqFNpgP2bNJNPTr1mtF5QUSZ30AAFWpNBVnj3mBzHXyVJ24TyDnY7yRSnLbUhiQx-HXBwBHiV0LH1UcK2F7UzFb1xh-FYjyrUKBSQw94VIgHAlgarMbNnEmkHmti1PHkp7BZ4bUnjZWEjvasYz9sRMbL0kP3ZVdaHFljCqoUeMGyNln90FZyZFm0VM8hN0BXl31838X4Sk3uqRjkobL5aygmkOVm4jQItQ__&Key-Pair-Id=K27TQMT39R1C8A"
                },
                
                //... I'll truncate this here, but there are many more lines

                {
                    "description": "Highmark BS Northeastern NY : Highmark Blue Shield of Northeastern New York - PPO",
                    "location": "https://anthembcca.mrf.bcbs.com/2024-08_800_72A0_in-network-rates_01_of_02.json.gz?&Expires=1726840840&Signature=hJ9FGMuLBY0LAwyMlrvYHKqpm-93Wm-Wd2Noncz~E6AA5FE1lQngK6eMoLLmEPtCTk0zbQeVJoSZQWUR75U0KlNqMYkailAf9APazY8ZSFc4~5PdsZ71qgk4tZxvfdajCLAVOCUI5N1144C84CA0yFm~CtLW2P7jjsD2w9VI7-8yKFtViMPds7Ty6PGmFWI06l5OT8le4UsInNG5~~bNQoOCVP21XkL6UziocNsqzBYCc6y~CHby5LyZ68vl4MbltQ92RrQWQ~pgV5fS~-sJxqQNwAJAMsKnexnIqDZ4BuQfIU0IvswU0OJ2WPY28LDr8l9BUOQwSNMr5Yj2x6NXng__&Key-Pair-Id=K27TQMT39R1C8A"
                },

                //... even more after this
            ],
            "allowed_amount_file": {
                "description": "Out-of-Network Allowed Amounts Files",
                "location": "https://antm-pt-prod-dataz-nogbd-nophi-us-east1.s3.amazonaws.com/anthem/2024-08-01_anthem-oon-multiplan-empty_allowed-amounts.json.gz"
            }
        }]
}
```

Upon a first glance, we find an in-network file with the description *"Highmark BS Northeastern NY : Highmark Blue Shield of Northeastern New York - PPO"*. The url for this seems to be hosted by anthem, so this is probably a match although technically Highmark is a separate company from Anthem.

Another important observation is that the description fields of the file objects often include details such as:
- the state that the file pertains to
- the health care type (e.g. PPO)

Given this, a logical approach is to iterate through all file objects and return those that match the keywords: "New York" and "PPO."


## Naive approach using the `jq` command

I'm a big fan of the command line, especially when it allows me to craft concise one-liners to solve problems. jq is a powerful command-line JSON processor that can handle a variety of tasks. In this case, we need to:

- Iterate through every Reporting Structure Object (RSO) within the `reporting_structure` array
- Filter and output every file that contains the strings "New York" and "PPO"

here's the command we can run:
```bash
jq '.reporting_structure[] | .in_network_files[], .allowed_amount_file | select(.description | contains("New York") and contains("PPO"))' example.json
```
### Explanation:
`.reporting_structure[]`: Iterates through each item in the reporting_structure array.
`| .in_network_files[], .allowed_amount_file`: For each reporting_structure item, this command accesses and processes each file within the in_network_files array and the allowed_amount_file object.
`select(.description | contains("New York") and contains("PPO"))`: Filters the files to include only those with descriptions that contain both "New York" and "PPO."

One issue that came up with my testing is that `in_network_files` and the `allowed_amount_file` are not required to be filled according to the [CMS table of contents](https://github.com/CMSgov/price-transparency-guide/tree/master/schemas/table-of-contents). So we need to add some empty-checks for each of these. Thus, we're left with:

```bash
jq '.reporting_structure[] | .in_network_files[]?, (.allowed_amount_file? // empty) | select(.description | contains("New York") and contains("PPO"))' example.json
```

### Performance Testing:
Here are some results from running the command on various file sizes:
| Command                                    | File Size   | User Time | System Time | CPU Usage | Total Time  | Throughput |
|--------------------------------------------|-------------|-----------|-------------|-----------|-------------|------------|
| `jq  index_100_lines.json > output`        | 16.6MB      | 0.23s     | 0.02s       | 99%       | 0.252s      | 65.87 MB/s |
| `jq  index_1k_lines.json > output`         | 149.4MB     | 1.71s     | 0.16s       | 99%       | 1.882s      | 79.38 MB/s |
| `jq  index_10k_lines.json > output`        | 1.49GB      | 17.40s    | 2.42s       | 97%       | 20.318s     | 73.33 MB/s |
| `jq  index_100k_lines.json > output`       | 15 GB       | 218.45s   | 119.47s     | 80%       | 7:01.58     | 35.58 MB/s |
| `jq  2024-08-01_anthem_index.json > output`| 22.19GB     | 324.93s   | 185.31s     | 77%       | 10:54.92    | 33.88 MB/s |


It looks like CPU usage and throughput went down once we beyond a couple GB in size. This is likely because `jq` attempts to load the json into memory before it even attempts to start filtering each value in the array. We're talking about 20+ GB of data, so clearly this strategy wont work/scale.

### Next steps
So far we have a working (albeit slow) solution. The next step to optimize this would have the program avoid loading the entire file into memory, all we really need to do is iterate through the `reporting_structure` array and filter for links that we're interested in. It may be possible to do this with more fancy tricks using `jq`, but if all we need to do is iterate through json then why not do this in a simple python script? 


## Faster approach using python and `ijson`
`ijson` is an "iterative JSON parser" for python which allows for us to create an iterable object based off of a user-specified field in the json. In our case, the `reporting_structure` is the most obvious field to use since it maps to a giant array containing every RSO. We can recreate the previous command in python like so:

```python
import ijson
import json

with open('2024-08-01_anthem_index.json', 'r') as input_file, open('filtered_output.json', 'w') as output_file:
    # Parse the JSON file and iterate over items in the 'reporting_structure' array
    reporting_structure_items = ijson.items(input_file, 'reporting_structure.item')

    filtered_files = (
        mrf for item in reporting_structure_items
        for mrf in item.get('in_network_files', []) # iterate through 'in_network_files' in the report structure object
        if 'New York' in mrf['description'] and 'PPO' in mrf['description'] # filter for keywords
    )

    # Write each filtered JSON object as a single line in the output file
    for entry in filtered_files:
        output_file.write(json.dumps(entry) + '\n')

```
### Explanation:
By passing the json file and the path to the array in to `ijson.items()` we create an iterable which we can then filter and output the results into a new file `filtered_output.json`. Note that the `filtered_files` will be instantiated as a generator object, the values will only be fetched during the for loop where we output the files.

We'll also go ahead and add some extra scripting niceties like as argument parser for the input/ouput files and keywords we were interested in.

### Performance Testing:
Immediately we see faster results, along with a more linear progression of the runtime as the size of the file increases:
| Command                                                                                | File Size | User Time | System Time | CPU Usage | Total Time  | Throughput |
|----------------------------------------------------------------------------------------|-----------|-----------|-------------|-----------|-------------|------------| 
| `python keyword_parser.py ./index_100_lines.json output.json "New York" "PPO"`         | 16.6MB    | 0.15s     | 0.03s       | 96%       | 0.182s      | 91.2 MB/s  |
| `python keyword_parser.py ./index_1k_lines.json output.json "New York" "PPO"`          | 149.4MB   | 0.87s     | 0.07s       | 96%       | 0.977s      | 152.9 MB/s |
| `python keyword_parser.py ./index_10k_lines.json output.json "New York" "PPO"`         | 1.49GB    | 8.04s     | 0.49s       | 98%       | 8.649s      | 172.27 MB/s|
| `python keyword_parser.py ./index_100k_lines.json output.json "New York" "PPO"`        | 15 GB     | 81.89s    | 5.29s       | 99%       | 1:27.81     | 170.8 MB/s |
| `python keyword_parser.py 2024-08-01_anthem_index.json output.json "New York" "PPO"`   | 22.19GB   | 114.70s   | 7.43s       | 99%       | 2:02.64     | 180.9 MB/s |


Being able to sift through the 20+ GB of data in around 2 minutes isnt too bad. But there's definitely room for improvment here, since the entire program up until now is reading through the data serially. Next steps here would be to explore implementing multithreading to accelerate the process further.


## Data Analysis
The output of running the script on `2024-08-01_anthem_index.json` results in ~540k files that have descriptions which match keywords: "New York" and "PPO". What's interesting is that most of these links are repeated many times, we can actually find out how many unique links there are by running:

```bash
awk '!seen[$0]++' output_links > unique_links
```

After running this command, we discover that the original 540k lines actually correspond to just 56 unique links, with the rest being duplicates! Furthermore, the links come from a set of 14 domains:
```
anthembcca.mrf.bcbs.com
anthembcbsva.mrf.bcbs.com
anthembcbsga.mrf.bcbs.com
anthembcbsky.mrf.bcbs.com
anthembcbsmo.mrf.bcbs.com
anthembcbsoh.mrf.bcbs.com
empirebcbs.mrf.bcbs.com
anthembcbsin.mrf.bcbs.com
anthembcbsnv.mrf.bcbs.com
anthembcbsco.mrf.bcbs.com
anthembcbsme.mrf.bcbs.com
anthembcbsct.mrf.bcbs.com
anthembcbsnh.mrf.bcbs.com
anthembcbswi.mrf.bcbs.com
```

Another observation is that the files seem to come in pairs of json.gz files. So a MRF like `2024-08_800_72A0_in-network-rates_01_of_02.json.gz` would have a corresponding file with the name `2024-08_800_72A0_in-network-rates_02_of_02.json.gz`.

The files tend to follow the same date-id patterns as well, regardless of which domain its being hosted on. Every file has prefix which is either `2024-08_301_71A0` and `2024-08_800_72A0`, I suspect the id for these represents the location/region the file is for.