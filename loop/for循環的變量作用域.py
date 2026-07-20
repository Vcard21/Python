"""
假設
for x in range(1,100):
    print(x)
print(x)
這樣外圈的print可以運作嗎?
可以，但在規範是不允許、不建議這麼做。
"""
i = 0
for i in range(5):
    print(i)

print(i)
# 如果真的想要在外部調用臨時變量，可以在循環前先定義好

