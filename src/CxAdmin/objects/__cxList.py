from typing import Any
from CxAdmin.csvable import CSVAble
from CxAdmin.jsonable import JSONSerializable


class CxListType(JSONSerializable):
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
    ):
        self.tenantID = tenantID
        self.description = description
        self.createdBy = createdBy
        self.updated = updated
        self.name = name
        self.fields = fields
        self.created = created
        self.updatedBy = updatedBy
        self.active = active
        self.id = id

    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxListType":
        return CxListType(
            tenantID=data["tenantId"],
            description=data["description"],
            createdBy=data["createdBy"],
            updated=data["updated"],
            name=data["name"],
            fields=data["fields"],
            created=data["created"],
            updatedBy=data["updatedBy"],
            active=data["active"],
            id=data["id"],
        )

    def to_json(self) -> dict[str, Any]:
        asDict = {
            "tenantID": self.tenantID,
            "description": self.description,
            "createdBy": self.createdBy,
            "updated": self.updated,
            "name": self.name,
            "fields": self.fields,
            "created": self.created,
            "updatedBy": self.updatedBy,
            "active": self.active,
            "id": self.id,
        }
        return asDict


class CxList(JSONSerializable, CSVAble):
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
    | id | `UUID` | The list's unique identifier. |
    | shared | `boolean` | Whether or not the list is shared to child tenants of this tenant. Valid values are true and false. |
    | items | `object` | The list items that make up the list, along with their unique identifiers, and (if available) a description of the list item. |
    """

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
        listItems: list[dict[str, Any]],
    ):
        self.tenantId = tenantId
        self.listType = listType
        self.createdBy = createdBy
        self.listTypeID = listTypeID
        self.updated = updated
        self.name = name
        self.created = created
        self.updatedBy = updatedBy
        self.active = active
        self.id = id
        self.shared = shared
        self.listItems = listItems

    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxList":
        return CxList(
            tenantId=data["tenantId"],
            listType=CxListType.from_json(data["listType"]),
            createdBy=data["createdBy"],
            listTypeID=data["listTypeId"],
            updated=data["updated"],
            name=data["name"],
            created=data["created"],
            updatedBy=data["updatedBy"],
            active=data["active"],
            id=data["id"],
            shared=data["shared"],
            listItems=data["items"],
        )

    def toCSV(self, headers: bool = False) -> list[str]:
        """
        Constructs a CSV of the data items of the CxList for reupload to the tenant.
        """
        data: list[list[str]] = []
        if headers:
            headings = list(self.listItems[0].keys())
            data.append(headings)

        for item in self.listItems:
            thisRow = list(item.values())
            data.append(thisRow)

        # convert list of lists to CSV
        csvData: list[str] = []
        for row in data:
            csvData.append(",".join(row))

        return csvData

    def __str__(self) -> str:
        return f"CxList({self.name}, {self.id})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_json(self) -> dict[str, Any]:
        return {
            "tenantId": self.tenantId,
            "listType": self.listType,
            "createdBy": self.createdBy,
            "listTypeID": self.listTypeID,
            "updated": self.updated,
            "name": self.name,
            "created": self.created,
            "updatedBy": self.updatedBy,
            "active": self.active,
            "id": self.id,
            "shared": self.shared,
            "listItems": self.listItems,
        }
