![](readme/logo.jpg)

# CxAdmin

CxAdmin is a Python API client for the CxEngage API. It is a work in progress and is not yet complete.

All objects are designed to mirror their CxEngage counterparts. For example, a CxList object has the exact same properties as a list on the CxEngage platform.
Together with the way this program is designed, this means you can fetch items from CxEngage, manipulate them locally, and then upload them back to CxEngage, without having to worry about the API.

This API is designed to be easily expandable. If you would like to add functionality, please feel free to submit a pull request.

## To Do
- [] Any object to CSV
- [X] Any object to JSON

## Usage – Contents
* [Set up API client](#set-up-api-client)
* [Get Everything](#get-everything)
* [Queues](#queues)
* [Lists](#lists)
* [Users](#users)
* [Groups](#groups)
* [Business Hours](#hours)
* [Environment](#environment)
* [Flows](#flows)
* [Statistics](#statistics)

### Set up API client

```py
import CxAdmin

cx = CxAdmin.Cx(
    baseURL="your_base_url", # https://eu-west-1-prod-api.cxengage.net for EU, https://api.cxengage.net for US
    apiKey="your_api_key",
    apiSecret="your_api_secret",
    tenantID="your_tenant_id",
)
```

or

```py
import CxAdmin

cx = CxAdmin.Cx.fromConfigFile("config.json")
```

> Example config.json

```json
{
    "baseURL": "https://eu-west-1-prod-api.cxengage.net",
    "apiKey": "73668f12-4da1-9991-p182-83ufb38193pa",
    "apiSecret": "biglongjumblystringoflettersandnumbershere",
    "tenantID": "893jwa23-85k2-895k-1562-93pot7367185"
}
```

### Get Everything

#### Get everything

```py
from CxAdmin import Cx
import json

cx: Cx
dev = True
if dev:
    cx = Cx.fromConfigFile("config.dev.json")
else:
    cx = Cx.fromConfigFile("config.prod.json")

for item in cx.items:
    print(item)
    out = item.get()
    name = str(item)[13:]
    name = name[: name.index(".")]
    file = open(f"output/{name}.json", "w")
    output = json.dumps(out)
    file.write(output)
```

This will fetch all items from CxEngage and save them to `output/` as JSON files.

### Queues

#### Get list of queues
```py
cx.queues.getQueues()
```
or
```py
cx.queues.get() # same as getQueues()
```

#### Get active queues
```py
cx.queues.getActiveQueues()
```

### Lists

#### Get all lists
```py
cx.lists.get()
```

#### Get list by ID
```py
cx.lists.getList(listId)
```

#### Get list as CSV
```py
cx.lists.getListCSV(listId)
```

#### Convert list object to CSV
```py
myList = cx.lists.getList(listId) # get a list
csv: list[str] = myList.toCSV() # convert to CSV, returns a list of strings
```

### Users

#### Get all users

```py
cx.users.getAllUsers()
```
or
```py
cx.users.get() # same as getAllUsers()
```

### Groups

#### Get all groups

```py
cx.groups.getGroups()
```
or
```py
cx.groups.get() # same as getGroups()
```

### Hours

#### Get list of business hours
```py
hours = cx.hours.get()
```

#### Get info for a specific business hours object (example)
```py
for hour in hours:
    print(f"{hour.name} - {hour.getBusinessHours()})
```
### Environment

#### Get tenant
    
```py
cx.environment.getTenant()
```
or
```py
cx.environment.get() # same as getTenant()
```

#### Get regions
    
```py
cx.environment.getRegions()
```

### Flows

#### Get all flows

```py
cx.flows.getFlows()
```
or
```py
cx.flows.get() # same as getFlows()
```

### Statistics

```py
cx.statistics.getInteractions(between: (datetime, datetime))
```
