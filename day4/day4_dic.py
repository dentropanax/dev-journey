person = {"이름": "주한", "나이": 30, "키": 175}
print(person["이름"])
person["나이"] +=1
print(f"내년엔 {person['나이']}살이에요")
for key in person:
    print(f"{key}: {person[key]}")
    