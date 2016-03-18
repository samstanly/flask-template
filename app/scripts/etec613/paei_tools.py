import os
def get_paei_questions():
    with open("app/scripts/etec613/questions.txt","r") as f:
        lines=f.readlines()
    lines=[i.strip() for i in lines if i.strip()]

    questions=[]
    qid=0
    prefix="UNKNOWN PREFIX"
    for line in lines:
        if line[0].isdigit():
            qid=int(line.split("]")[0])
            prefix=line.split("]")[1].strip()
        else:
            text=line[:-4]
            code=line[-2]
            question=[prefix+" "+text,code]
            questions.append(question)

    return questions

def get_paei_results(form):
    letters="cwavdxfyhz"
    results={letter:0 for letter in letters}
    for key in form:
        qid,code=key.split("-")
        answer=int(form[key])
        results[code]+=answer

    results["B"]=results["c"]+results["w"]
    results["L"]=results["a"]+results["v"]
    results["P"]=results["d"]+results["x"]
    results["H"]=results["f"]+results["y"]
    results["R"]=results["h"]+results["z"]

    return results


