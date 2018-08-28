
def toLowerCase(relString):
    # if isinstance(relString,str):
    #     for c in relString:
    #         if c.isupper():
    #             relString = relString.replace(c,chr(ord(c) + 32))#小写Ascll码比大写Ascll大32
    # return relString
    a = [1,2,3,4,5]
    for item in a[:]:
        print(a)
        a.remove(item)
        print(a)
def main():
  oldString = "AHELLO";
  print(toLowerCase(oldString))
if __name__ == '__main__':
    main();