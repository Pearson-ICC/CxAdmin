import src.CxAdmin
from src.CxAdmin.objects.platformStatus import PlatformStatus

cx = src.CxAdmin.Cx.fromConfigFile("config.prod.json")
users = cx.users.getAllUsers()
csv: list[str] = []
csv += ["First Name,Last Name,Email,Role\n"]

blacklist_words = ["lifesize", "serenova", "api"]
for user in users:
    if user.platformStatus.value == PlatformStatus.accepted.value:
        if not any(word in user.email for word in blacklist_words):
            csv += [f"{user.firstName},{user.lastName},{user.email},{user.roleName}\n"]

file = open(f"users.csv", "w")
file.writelines(csv)
file.close()
