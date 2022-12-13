from api.cx import Cx

cx: Cx
dev = False
if dev:
    cx = Cx.fromConfigFile("config.dev.json")
else:
    cx = Cx.fromConfigFile("config.prod.json")

queues = cx.queues.getQueues()
text = ""
text += f"ID,Name\n"
for queue in queues:
    queueNameDelimited = queue.name.replace(",", " ")
    text += f"{queue.id},{queueNameDelimited}\n"

with open("queues.csv", "w") as file:
    file.write(text)
