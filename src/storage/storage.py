from kybra import query, update,StableBTreeMap,Principal,ic,opt,nat,null

from storage_structure import Storage, generate_id

storages = StableBTreeMap[Principal,Storage](
    memory_id=0,max_key_size=1000,max_value_size=10000
)

@update
def postAdvertisement(Rent:int, OwnerPrincipal:Principal, Path:str, TimePeriod:str, Space:int) -> opt[Principal]:
    adId = generate_id(Path+TimePeriod)
    newAdvertisement : Storage = {
        "Rent" : Rent,
        "OwnerPrincipal" : OwnerPrincipal,
        "Path" : Path,
        "RenterPrincipal" : None,
        "TimePeriod" : TimePeriod,
        "Space" : Space
    }
    
    if not storages.contains_key(adId):
        storage = storages.insert(adId, newAdvertisement)
        if storage:
            ic.print("Advertisement created")
            return adId
        else:
            ic.print("Advertisement not created")
            return None
    else:
        ic.print("Advertisement already exists")
        return adId
#   h3fdq-ulnmn-5gi5t-wnzsg-2ytdn-z5hm3-ldpjs-hm5to-mrwwe-y3opj-3g2  
@update
def deleteAdvertisement(Id:Principal) -> opt[str]:
    if storages.contains_key(Id):
        storage = storages.remove(Id)
        if storage:
            ic.print("Advertisement deleted")
            return "Advertisement deleted"
        else:
            ic.print("Advertisement not deleted")
            return None
    else:
        ic.print("Advertisement does not exist")
        return None
    
@update
def addRentee(Id:Principal, RenterPrincipal:Principal) -> opt[Principal]:
    if storages.contains_key(Id):
        storage = storages.get(Id)
        if storage:
            ic.print("Advertisement found")
            storage["RenterPrincipal"] = RenterPrincipal
            ic.print( storage["RenterPrincipal"])
            return storage["RenterPrincipal"]
        else:
            ic.print("Advertisement not found")
            return None
    else:
        ic.print("Advertisement does not exist")
        return None
    
@update
def removeRentee(Id:Principal) -> opt[Principal]:
    if storages.contains_key(Id):
        storage = storages.get(Id)
        if storage:
            ic.print("Advertisement found")
            storage["RenterPrincipal"] = None
            ic.print("Rentee removed")
            return  storage["RenterPrincipal"]
        else:
            ic.print("Advertisement not found")
            return None
    else:
        ic.print("Advertisement does not exist")
        return None
    
@query
def getAdvertisement(Id:Principal) -> opt[Storage]:
    storage = storages.get(Id)
    if storage:
        ic.print("Advertisement found")
        return storage
    else:
        ic.print("Advertisement not found")
        return None


