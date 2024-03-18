text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper())  # is the text all uppercase?
print(text.upper())  # convert to uppercase

new_text = text.upper()
print(text, new_text)
print("bannannnana".count("n"))
print("banababanan".index("ana"))
print("banabanabanan".replace("ana", "XXYYZZ"))
sentence = "Hello, kind-sir; how many! I be of service today?"
print(sentence.replace(",", "").replace(";", "").replace("!", "").replace("?", ""))

punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

bob_text = "Bob goes to. Bob finds. Bob is. Bob will."
print(bob_text.find("Bob"))
print(bob_text.rfind("Bob"))

i = 0
while i < len(bob_text):
    i = bob_text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1
