def get_students():
    students={}
    try:
        with open("app/scripts/ican/hash-students.txt","r") as f:
            for line in f.readlines():
                if line.strip():
                    split=line.split("\t")
                    if len(split)==2:
                        students[split[0].strip()]=split[1].strip()
    except FileNotFoundError:
        print("file not found?")
        pass
    return students

