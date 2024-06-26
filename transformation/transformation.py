

class Transformation(object):
    def __init__(self):
        pass

    def get_road_from_api(self,geocode_datas):
        if "address" in geocode_datas:
            road =  (
                geocode_datas["address"]["road"] 
                if "road" in geocode_datas["address"] 
                else geocode_datas["address"]["suburb"] 
                if "suburb" in geocode_datas["address"]
                else "not known"
            )

        else:
            road = "address not found in map"
        return road
