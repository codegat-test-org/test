from collections import defaultdict

d: dict[str, list[any]] = defaultdict(list)

d["numbers"].append("123")
d["numbers"].append("456")

print(d.items())