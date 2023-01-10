from typing import Any

class CxListType:
    """
    The type of list object in CxEngage.

    | Parameter | Type | Description |
    | --- | --- | --- |
    | tenantId | `UUID` | The tenant’s unique identifier. |
    | description | `string` | A description of the list type object. |
    | createdBy | `UUID` | The unique identifier of the Platform Administrator who created the list type object. |
    | updated | `string` | The date and time, in UTC format, when the list type object was last modified. |
    | name | `string` | The name of the list type. |
    | fields | `sub object` | An object containing a list of fields for the list type. For each field, you must specify the following parameters: type—The value type for the field. Value options are string, boolean, or number. The first field specified in the object must have a value of string in the type parameter. name—A unique name for the field. label—A label to be displayed in the user interface. required—A flag to indicate whether this is a required field. Valid options are true or false. The first field specified in the object must have a value of true for the required parameter. |
    | created | `string` | The date and time, in UTC format, when the list type was created. |
    | updatedBy | `UUID` | The unique identifier of the Platform Administrator who last updated the list type object. |
    | active | `string` | Whether or not the list type is enabled. Valid values are true and false. |
    | id | `UUID` | The list type object’s unique identifier. |
    """

    tenantID: str
    description: str
    createdBy: str
    updated: str
    name: str
    fields: str
    created: str
    updatedBy: str
    active: str
    id: str

    def __init__(
        self,
        tenantID: str,
        description: str,
        createdBy: str,
        updated: str,
        name: str,
        fields: str,
        created: str,
        updatedBy: str,
        active: str,
        id: str,
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxListType": ...

class CxList:
    """
    A list includes the following parameters:

    | Parameter | Type | Description |
    | --- | --- | --- |
    | tenantId | `UUID` | The unique identifier of the tenant. |
    | listType | `object` |  A JSON object containing details of the list type. This parameter is only returned if you have `MANAGE_ALL_LISTS` permission. [Learn more about the content of the listType object](https://api-docs.cxengage.net/Rest/Content/List_Types/Return_list_type_object.htm#ListTypeObjectParams).
    | createdBy | `UUID` | The unique identifier of the user who created the list. |
    | listTypeId | `UUID` | The unique identifier of the list type assigned to this list. |
    | updated | `string` | The date and time, in UTC format, when the list was last modified. |
    | name | `string` | The name of the list. |
    | created | `string` | The date and time, in UTC format, when the list type was created. |
    | updatedBy | `UUID` | The unique identifier of the user who last updated the list. |
    | active | `string` | Whether or not the list is enabled. Valid values are true and false. |
    | id | `UUID` | The list’s unique identifier. |
    | shared | `boolean` | Whether or not the list is shared to child tenants of this tenant. Valid values are true and false. |
    | items | `object` | The list items that make up the list, along with their unique identifiers, and (if available) a description of the list item. |
    """

    tenantId: str
    listType: CxListType
    createdBy: str
    listTypeID: str
    updated: str
    name: str
    created: str
    updatedBy: str
    active: str
    id: str
    shared: str
    items: list[dict[str, Any]]

    def __init__(
        self,
        tenantId: str,
        listType: CxListType,
        createdBy: str,
        listTypeID: str,
        updated: str,
        name: str,
        created: str,
        updatedBy: str,
        active: str,
        id: str,
        shared: str,
        items: list[dict[str, Any]],
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxList": ...
    def constructDataCSV(self) -> str: ...
