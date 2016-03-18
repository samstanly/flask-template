import os.path, json
import sys
def get_hash_reports():
    print("sys.path:\n%s"%str(sys.path))
    filename="report.json"
    if not os.path.isfile(filename):
        filename="app/scripts/ican/"+filename
    if not os.path.isfile(filename):
        return []
    with open(filename,"r") as f:
        data=f.read()
    reports= json.loads(data)
    return get_sorted_reports(reports)

def get_secret():
    print("sys.path:\n%s"%str(sys.path))
    filename="secret.txt"
    if not os.path.isfile(filename):
        filename="app/scripts/ican/"+filename
    if not os.path.isfile(filename):
        return ""
    with open(filename,"r") as f:
        data=f.read()
    return data.strip()

def get_sorted_reports(reports):
    sorted_reports=sorted(reports,key=lambda k:k["score"])
    return list(reversed(sorted_reports))

def get_best(reports,key,get_highest=1):
    value=-1
    best=0
    for report in reports:
        if "score" not in report or not report["score"]:
            continue
        if key in report and (value==-1 or
                              (get_highest and report[key]>value) or
                              (not get_highest and report[key]<value)):
            best=report
            value=report[key]
    if best and "author" in best:
        return best["author"]
    return "unknown"

def get_hash_winners(reports):
    keys= ("avalanche_score","collision_score","lev_score","uniformity_score")
    winners={key:get_best(reports,key) for key in keys}
    winners["time"]=get_best(reports,"time",get_highest=0)
    return winners

if __name__=="__main__":
    print("REPORT:")
    print(get_hash_reports())
    print("\nWINNERS:")
    print(get_hash_winners(get_hash_reports()))
