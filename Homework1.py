class City:
    def __init__(self, city_name, region_name, country_name, num_citizens, zip_code, area_code):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.num_citizens = num_citizens
        self.zip_code = zip_code
        self.area_code = area_code

    def get_full_address(self):
        return f"City: {self.city_name}, Region: {self.region_name}, Country: {self.country_name}, Population: {self.num_citizens}, ZIP: {self.zip_code}, Area Code: {self.area_code}"



city = City("Bratislava","Bratislava", "Slovensko", 475503, "85101", "14")
print(city.get_full_address())