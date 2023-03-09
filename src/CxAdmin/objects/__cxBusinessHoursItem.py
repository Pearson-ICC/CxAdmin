from typing import Any
from CxAdmin.jsonable import JSONSerializable


class CxBusinessHoursItem(JSONSerializable):
    """
    +---------------------------+---------+----------------------------+
    | Parameter                 | Type    | Description                |
    +===========================+=========+============================+
    | tenantId                  | UUID    | The tenant's unique        |
    |                           |         | identifier.                |
    +---------------------------+---------+----------------------------+
    | createdBy                 | UUID    | The unique identifier of   |
    |                           |         | the user who created the   |
    |                           |         | business hours object.     |
    +---------------------------+---------+----------------------------+
    | updated                   | string  | The date and time, in UTC  |
    |                           |         | format, when the object    |
    |                           |         | was last updated.          |
    +---------------------------+---------+----------------------------+
    | name                      | string  | The human-readable name of |
    |                           |         | the business hours object. |
    +---------------------------+---------+----------------------------+
    | timezone                  | string  | The location to which the  |
    |                           |         | business hours apply. The  |
    |                           |         | location is in TZ database |
    |                           |         | format (continent/city -   |
    |                           |         | for example, *America/New  |
    |                           |         | York*).                    |
    +---------------------------+---------+----------------------------+
    | active                    | boolean | A flag indicating whether  |
    |                           |         | or not the business hours  |
    |                           |         | object is in use.          |
    +---------------------------+---------+----------------------------+
    | description               | string  | A short description of the |
    |                           |         | business hours object.     |
    +---------------------------+---------+----------------------------+
    | *[day]*startTimeMinutes   | string  | The time at which the      |
    |                           |         | business hours start on a  |
    |                           |         | particular day of the      |
    |                           |         | week. The time is the      |
    |                           |         | number of minutes since    |
    |                           |         | midnight. For example, set |
    |                           |         | this parameter to *480* to |
    |                           |         | indicate that the business |
    |                           |         | hours start at 8:00 AM.    |
    |                           |         |                            |
    |                           |         | If the value of            |
    |                           |         | *[day]*startTimeMinutes    |
    |                           |         | is the same as             |
    |                           |         | *[day]*endTimeMinutes,     |
    |                           |         | the business hours apply   |
    |                           |         | to the entire day.         |
    |                           |         |                            |
    |                           |         | **Note:** the day of the   |
    |                           |         | week is a three-letter     |
    |                           |         | abbreviation - for         |
    |                           |         | example, *mon* for Monday. |
    +---------------------------+---------+----------------------------+
    | *[day]*endTimeMinutes     | string  | The time at which the      |
    |                           |         | business hours end on a    |
    |                           |         | particular day of the      |
    |                           |         | week. The time is the      |
    |                           |         | number of minutes since    |
    |                           |         | midnight. For example, set |
    |                           |         | this parameter to *1020*   |
    |                           |         | to indicate that the       |
    |                           |         | business hours end at 5:00 |
    |                           |         | PM.                        |
    |                           |         |                            |
    |                           |         | If the value of            |
    |                           |         | *[day]*endTimeMinutes is   |
    |                           |         | the same as                |
    |                           |         | *[day]*startTimeMinutes,   |
    |                           |         | the business hours apply   |
    |                           |         | to the entire day          |
    |                           |         |                            |
    |                           |         | **Note:** the day of the   |
    |                           |         | week is a three-letter     |
    |                           |         | abbreviation - for         |
    |                           |         | example, *mon* for Monday. |
    +---------------------------+---------+----------------------------+
    | created                   | string  | The date and time, in      |
    |                           |         | UTC format, when the       |
    |                           |         | object was created.        |
    +---------------------------+---------+----------------------------+
    | updatedBy                 | UUID    | The unique identifier of   |
    |                           |         | the user who last updated  |
    |                           |         | the object.                |
    +---------------------------+---------+----------------------------+
    | id                        | UUID    | The unique identifier of   |
    |                           |         | the business hours object. |
    +---------------------------+---------+----------------------------+
    | exceptions                | string  | An object a list of        |
    |                           |         | exceptions to a tenant's   |
    |                           |         | business hours - for       |
    |                           |         | example, business hours on |
    |                           |         | a public holiday. For more |
    |                           |         | information, see [Create   |
    |                           |         | an exception to business   |
    |                           |         | hours](Cre                 |
    |                           |         | ate_exception.htm){.MCXref |
    |                           |         | .xref}.                    |
    +---------------------------+---------+----------------------------+
    """

    def __init__(
        self,
        tenantId: str,
        createdBy: str,
        updated: str,
        name: str,
        timezone: str,
        active: bool,
        description: str,
        startTimeMinutes: dict[str, Any],
        endTimeMinutes: dict[str, Any],
        created: str,
        updatedBy: str,
        id: str,
        exceptions: list[str],
    ):
        self.tenantId = tenantId
        self.createdBy = createdBy
        self.updated = updated
        self.name = name
        self.timezone = timezone
        self.active = active
        self.description = description
        self.startTimeMinutes = startTimeMinutes
        self.endTimeMinutes = endTimeMinutes
        self.created = created
        self.updatedBy = updatedBy
        self.id = id
        self.exceptions = exceptions

    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxBusinessHoursItem":
        startTimeMinutes: dict[str, Any] = {}
        endTimeMinutes: dict[str, Any] = {}

        for key, value in data.items():
            if key.endswith("StartTimeMinutes"):
                startTimeMinutes[key] = value
            elif key.endswith("EndTimeMinutes"):
                endTimeMinutes[key] = value

        return CxBusinessHoursItem(
            tenantId=data["tenantId"],
            createdBy=data["createdBy"],
            updated=data["updated"],
            name=data["name"],
            timezone=data["timezone"],
            active=data["active"],
            description=data["description"],
            startTimeMinutes=startTimeMinutes,
            endTimeMinutes=endTimeMinutes,
            created=data["created"],
            updatedBy=data["updatedBy"],
            id=data["id"],
            exceptions=data["exceptions"],
        )

    def __str__(self) -> str:
        return f"CxBusinessHoursItem({self.name}, {self.id})"

    def __repr__(self) -> str:
        return self.__str__()

    def getBusinessHours(self) -> dict[str, tuple[int, int]]:
        """returns an *unordered* dict of
        ```json
        {
          "mon": (start minute, end minute),
          ...[tue, wed, thu, fri, sat]...
          "sun": (start minute, end minute)
        }
        ```
        """

        # Create dict of opening times
        openingTimes: dict[str, int] = dict()
        for day, time in self.startTimeMinutes.items():
            openingTimes[day] = time

        # Create dict of closing times
        closingTimes: dict[str, int] = dict()

        for day, time in self.endTimeMinutes.items():
            closingTimes[day] = time

        # Create dict of business hours
        businessHours: dict[str, tuple[int, int]] = dict()

        # now construct a dict of {original dicts' keys, (both values in tuple)}
        openingKeys = list(openingTimes.keys())
        closingKeys = list(closingTimes.keys())
        daysList = [day[:3] for day in list(openingTimes.keys())]

        for i in range(0, len(daysList)):
            day = daysList[i]
            openTime = openingTimes[openingKeys[i]]
            closeTime = closingTimes[closingKeys[i]]

            businessHours[day] = (openTime, closeTime)

        return businessHours

    def to_json(self) -> dict[str, Any]:
        return {
            "tenantId": self.tenantId,
            "createdBy": self.createdBy,
            "updated": self.updated,
            "name": self.name,
            "timezone": self.timezone,
            "active": self.active,
            "description": self.description,
            "startTimeMinutes": self.startTimeMinutes,
            "endTimeMinutes": self.endTimeMinutes,
            "created": self.created,
            "updatedBy": self.updatedBy,
            "id": self.id,
            "exceptions": self.exceptions,
        }
