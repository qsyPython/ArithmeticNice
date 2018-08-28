
def toLowerCase(relString):
    if isinstance(relString,str):
        for c in relString:
            if c.isupper():
                relString = relString.replace(c,chr(ord(c) + 32))
    return relString


def main():
  oldString = "AHELLO";
  print(toLowerCase(oldString))
if __name__ == '__main__':
    main();