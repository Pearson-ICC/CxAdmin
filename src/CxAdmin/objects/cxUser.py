from typing import Any, Optional
from datetime import datetime
from CxAdmin.objects.platformStatus import PlatformStatus
from CxAdmin.objects.skill import Skill


class CxUser(dict[str, Any]):
    activeExtension: dict[str, str]
    additionalRoleIds: str
    ailasPlatformUserId: str
    clientLogLevel: Optional[str]
    created: datetime
    createdBy: str
    defaultTenant: str
    email: str
    extensions: list[dict[str, Any]]
    externalId: Optional[str]
    firstName: str
    groups: list[dict[str, str]]
    id: str
    lastName: str
    personalTelephone: Optional[str]
    platformStatus: PlatformStatus
    roleName: str
    skills: list[Skill]
    state: str
    status: PlatformStatus
    updated: datetime
    updatedBy: str

    def __init__(
        self,
        activeExtension: dict[str, str],
        additionalRoleIds: str,
        ailasPlatformUserId: str,
        clientLogLevel: Optional[str],
        created: datetime,
        createdBy: str,
        defaultTenant: str,
        email: str,
        extensions: list[dict[str, Any]],
        externalId: Optional[str],
        firstName: str,
        groups: list[dict[str, str]],
        id: str,
        lastName: str,
        personalTelephone: Optional[str],
        platformStatus: PlatformStatus,
        roleName: str,
        skills: list[Skill],
        state: str,
        status: PlatformStatus,
        updated: datetime,
        updatedBy: str,
    ):
        self.activeExtension = activeExtension
        self.additionalRoleIds = additionalRoleIds
        self.ailasPlatformUserId = ailasPlatformUserId
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
        self.platformStatus = platformStatus
        self.roleName = roleName
        self.skills = skills
        self.state = state
        self.status = status
        self.updated = updated
        self.updatedBy = updatedBy

    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxUser":
        return CxUser(
            activeExtension=data["activeExtension"],
            additionalRoleIds=data["additionalRoleIds"],
            ailasPlatformUserId=data["ailasPlatformUserId"],
            clientLogLevel=data["clientLogLevel"],
            created=datetime.fromisoformat(data["created"]),
            createdBy=data["createdBy"],
            defaultTenant=data["defaultTenant"],
            email=data["email"],
            extensions=data["extensions"],
            externalId=data["externalId"],
            firstName=data["firstName"],
            groups=data["groups"],
            id=data["id"],
            lastName=data["lastName"],
            personalTelephone=data["personalTelephone"],
            platformStatus=PlatformStatus(data["platformStatus"]),
            roleName=data["roleName"],
            skills=[Skill.from_json(skill) for skill in data["skills"]],
            state=data["state"],
            status=PlatformStatus(data["status"]),
            updated=datetime.fromisoformat(data["updated"]),
            updatedBy=data["updatedBy"],
        )
