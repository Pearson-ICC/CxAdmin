from api.cx import Cx
from Pearson.routingItem_internal import Routing

cx: Cx
dev = False
if dev:
    cx = Cx.fromConfigFile("config.dev.json")
else:
    cx = Cx.fromConfigFile("config.prod.json")

cxLists = cx.lists

routingLists: list[str] = [
    # redacted
]

allRoutes: list[Routing] = []

for routingListID in routingLists:
    routingList = cxLists.getList(routingListID)
    routes = [Routing.from_json(route) for route in routingList.items]
    allRoutes.extend(routes)

# filter by route's queuename == 'EO_Key_FE'

eo_fe_routes: list[Routing] = list(
    filter(lambda route: route.queuename == "EO_Key_FE", allRoutes)
)

print(len(allRoutes))
print(len(eo_fe_routes))

csvLines: list[str] = []
for route in eo_fe_routes:
    csvLines.append(route.to_csv() + "\n")

file = open(f"EO_Key_FE.csv", "w")
file.writelines(csvLines)
file.close()
