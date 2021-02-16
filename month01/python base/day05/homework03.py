list01 = ["a",(1,2,3),{"b":"B","c":"C"}]
list02 = list01
list03 = list01[:]
list02[0] = "b"
print(list01[0]) # b


list02[2]["b"] = "BB"
print(list02[2]["b"]) # "BB"

list03[0] = "bb"
print(list01[0]) # "b"