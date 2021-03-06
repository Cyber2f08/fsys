from src.ocec import typeval, conchk
import requests, json
import config as cfg

header = {
    "Accept": "application/json"
}

cefile = 'certs/certs.pem'

#ID is supposed to be an integer check it's value by using typeval


def _get_user_info(id):
    if typeval(id, int)[0] != True:
        return "Value Err. \nNote: ID is supposed to be a type of (int) and not ({0})".format(typeval(id, int)[1])
    rs = requests.get(f"https://users.roblox.com/v1/users/{id}", headers=header, verify = False)
    if conchk(rs) != True:
        return "Endpoint Err.";
    rs = json.loads(rs.text)
    return rs;

def _get_user_primary_group(id):
    if typeval(id, int)[0] != True:
        return "Value Err. \nNote: ID is supposed to be a type of (int) and not ({0})".format(typeval(id, int)[1])
    rs = requests.get(f"https://groups.roblox.com/v1/users/{id}/groups/primary/role", verify = False)
    if conchk(rs) != True:
        return "Endpoint Err."
    rs = json.loads(rs.text)
    return rs;

def _get_muser_info(id):
    if typeval(id, int)[0] != True:
        return "Value Err. \nNote: ID is supposed to be a type of (int) and not ({0})".format(typeval(id, int)[1])
    dump = []
    rps = _get_user_info(id)
    gprm = _get_user_primary_group(id)
    dump.append(rps)
    dump.append(gprm)
    return dump;

def _get_roblox_info(platform="windows"):
    dp = []
    if platform == "windows":
        rbver = "http://setup.roblox.com/version"
        rbiover = "http://setup.roblox.com/versionStudio"
        verqtio = "http://setup.roblox.com/versionQTStudio"
        #deplhto = "http://setup.roblox.com/DeployHistory.txt"
        rs = requests.get(rbver, verify = cefile)
        if rs.status_code != 200:
            dp.append("Information Err.")
        
        rb = requests.get(rbiover,verify = cefile)
        if rb.status_code != 200:
            dp.append("Information Err.")
        
        ve = requests.get(verqtio, verify = cefile)
        if ve.status_code != 200:
            dp.append("Informatio Err.")

        dp.append(rs.text)
        dp.append(rb.text)
        dp.append(ve.text)
        dp.append((rs.status_code, rb.status_code, ve.status_code))
    elif platform == "macos":
        rbver = "http://setup.roblox.com/mac/version"
        rbiover = "http://setup.roblox.com/mac/versionStudio"
        #deplhto = "http://setup.roblox.com/DeployHistory.txt"
        rs = requests.get(rbver, verify = cefile)
        if rs.status_code != 200:
            dp.append("Information Err.")
        
        rb = requests.get(rbiover, verify = cefile)
        if rb.status_code != 200:
            dp.append("Information Err.")
        
        dp.append(rs.text)
        dp.append(rb.text)
        dp.append((rs.status_code, rb.status_code))
    return dp;
