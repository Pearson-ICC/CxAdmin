![](readme/logo.jpg)

# CxAdmin

CxAdmin is a Python API client for the CxEngage API. It is a work in progress and is not yet complete.

All objects are designed to mirror their CxEngage counterparts. For example, a CxList object has the exact same properties as a list on the CxEngage platform.
Together with the way this program is designed, this means you can fetch items from CxEngage, manipulate them locally, and then upload them back to CxEngage, without having to worry about the API.

This API is designed to be easily expandable. If you would like to add functionality, please feel free to submit a pull request.

## To Do
- [] Any object to CSV

## Usage – Contents
* [Set up API client](#set-up-api-client)
* [Queues](#queues)
* [Lists](#lists)
* [Users](#users)
* [Groups](#groups)
* [Environment](#environment)
* [Flows](#flows)
* [Statistics](#statistics)

### Set up API client

```python
import CxAdmin

cx = CxAdmin.Cx(
    baseURL="your_base_url", # https://eu-west-1-prod-api.cxengage.net for EU, https://api.cxengage.net for US
    apiKey="your_api_key",
    apiSecret="your_api_secret",
    tenantID="your_tenant_id",
)
```

or

```python
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

### Queues

#### Get list of queues
```python
cx.queues.getQueues()
```
or
```python
cx.queues.get() # same as getQueues()
```

#### Get active queues
```python
cx.queues.getActiveQueues()
```

### Lists

#### Get all lists
```python
cx.lists.get()
```

#### Get list by ID
```python
cx.lists.getList(listId)
```

#### Get list as CSV
```python
cx.lists.getListCSV(listId)
```

### Users

#### Get all users

```python
cx.users.getAllUsers()
```
or
```python
cx.users.get() # same as getAllUsers()
```

### Groups

#### Get all groups

```python
cx.groups.getGroups()
```
or
```python
cx.groups.get() # same as getGroups()
```

### Environment

#### Get tenant
    
```python
cx.environment.getTenant()
```
or
```python
cx.environment.get() # same as getTenant()
```

#### Get regions
    
```python
cx.environment.getRegions()
```

### Flows

#### Get all flows

```python
cx.flows.getFlows()
```
or
```python
cx.flows.get() # same as getFlows()
```

### Statistics

```python
cx.statistics.getInteractions(between: (datetime, datetime))
```
