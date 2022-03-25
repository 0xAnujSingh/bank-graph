from api.models import Bank, Branch

def listBanks_resolver (obj, info):
    try:
        banks = [bank.to_dict() for bank in Bank.query.all()]
        payload = {
            "success": True,
            "banks": banks
        }
        
        return payload
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def getBank_resolver (obj, info, id):
    try:
        bank = Bank.query.get(id)
        payload = {
            "success": True,
            "bank": bank
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def getBankBranch_resolver (obj, info, district):
    try:
        if district:
            branches = Branch.query.filter(Branch.bank_id == obj.id, Branch.district == district)
        else:
            branches = Branch.query.filter(Branch.bank_id == obj.id)
    except Exception as error:
        print(str(error))
        branches = []

    return branches

def getBranch_resolver(obj, info, ifsc):
    try:
        branch = Branch.query.filter(Branch.ifsc == ifsc)

        payload = {
            "success": True,
            "branch": branch[0]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def getBranchBank_resolver(obj, info):
    print(obj.bank_id)

    payload = getBank_resolver(obj, info, obj.bank_id)

    if payload['success']:
        return payload['bank']
    
    return None