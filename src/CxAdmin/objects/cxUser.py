from typing import Any, Optional
from datetime import datetime
from CxAdmin.objects.platformStatus import PlatformStatus
from CxAdmin.objects.skill import Skill


class CxUser(dict[str, Any]):
    activeExtension: dict[str, str]
    additionalRoleIds: Optional[str]
    aliasPlatformUserId: Optional[str]
    clientLogLevel: Optional[str]
    created: datetime
    createdBy: str
    defaultTenant: Optional[str]
    email: str
    extensions: list[dict[str, Any]]
    externalId: Optional[str]
    firstName: str
    groups: list[dict[str, str]]
    id: str
    lastName: str
    personalTelephone: Optional[str]
    tenantStatus: PlatformStatus
    roleName: str
    skills: list[Skill]
    state: str
    platformStatus: PlatformStatus
    updated: datetime
    updatedBy: str

    def __init__(
        self,
        activeExtension: dict[str, str],
        additionalRoleIds: Optional[str],
        aliasPlatformUserId: Optional[str],
        clientLogLevel: Optional[str],
        created: datetime,
        createdBy: str,
        defaultTenant: Optional[str],
        email: str,
        extensions: list[dict[str, Any]],
        externalId: Optional[str],
        firstName: str,
        groups: list[dict[str, str]],
        id: str,
        lastName: str,
        personalTelephone: Optional[str],
        tenantStatus: PlatformStatus,
        roleName: str,
        skills: list[Skill],
        state: str,
        platformStatus: PlatformStatus,
        updated: datetime,
        updatedBy: str,
    ):
        self.activeExtension = activeExtension
        self.additionalRoleIds = additionalRoleIds
        self.aliasPlatformUserId = aliasPlatformUserId
        self.clientLogLevel = clientLogLevel
        self.created = created
        self.createdBy = createdBy
        self.defaultTenant = defaultTenant
        self.email = email
        self.extensions = extensions
        self.externalId = externalId
        self.firstName = firstName
        self.groups = groups
        self.id = id
        self.lastName = lastName
        self.personalTelephone = personalTelephone
        self.tenantStatus = tenantStatus
        self.roleName = roleName
        self.skills = skills
        self.state = state
        self.platformStatus = platformStatus
        self.updated = updated
        self.updatedBy = updatedBy

    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxUser":
        return CxUser(
            activeExtension=data["activeExtension"],
            additionalRoleIds=data.get("additionalRoleIds"),
            aliasPlatformUserId=data.get("aliasPlatformUserId"),
            clientLogLevel=data["clientLogLevel"],
            created=datetime.fromisoformat(data["created"][:-1]),
            createdBy=data["createdBy"],
            defaultTenant=data.get("defaultTenant"),
            email=data["email"],
            extensions=data["extensions"],
            externalId=data["externalId"],
            firstName=data["firstName"],
            groups=data["groups"],
            id=data["id"],
            lastName=data["lastName"],
            personalTelephone=data["personalTelephone"],
            tenantStatus=PlatformStatus(data["platformStatus"]),
            roleName=data["roleName"],
            skills=[Skill.from_json(skill) for skill in data["skills"]],
            state=data["state"],
            platformStatus=PlatformStatus(data["status"]),
            updated=datetime.fromisoformat(data["updated"][:-1]),
            updatedBy=data["updatedBy"],
        )
