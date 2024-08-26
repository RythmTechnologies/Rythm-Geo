import json
from rest_framework.views import APIView
from rest_framework.response import Response

class GeoView(APIView):
    
    def get(self, request):
        try:
            # JSON dosyasını oku
            with open("geo_app/countries+states+cities.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            country_name = request.query_params.get('country', None)
            state_name = request.query_params.get('state', None)
            city_name = request.query_params.get('city', None)

            if country_name:
                country_name = country_name.capitalize()
                print(country_name)
            if state_name:
                state_name = state_name.capitalize()
                print(state_name)
            if city_name:
                city_name = city_name.capitalize()

            result = []

            for item in data:
                formatted_country_name = item['name'].capitalize()  

                if country_name and formatted_country_name == country_name.capitalize():
                    result.append({
                        "id": item["id"],
                        "name": formatted_country_name,
                        "iso3": item["iso3"],
                        "iso2": item["iso2"],
                        "numeric_code": item["numeric_code"],
                        "phone_code": item["phone_code"],
                        "capital": item["capital"],
                        "currency": item["currency"],
                        "currency_name": item["currency_name"],
                        "currency_symbol": item["currency_symbol"],
                        "tld": item["tld"],
                        "native": item["native"],
                        "region": item["region"],
                        "region_id": item["region_id"],
                        "subregion": item["subregion"],
                        "subregion_id": item["subregion_id"],
                        "nationality": item["nationality"],
                        "timezones": item["timezones"],
                        "translations": item["translations"],
                        "latitude": item["latitude"],
                        "longitude": item["longitude"],
                        "emoji": item["emoji"],
                        "emojiU": item["emojiU"],
                        "states": item["states"]
                    })
                    break

                elif state_name:
                    # Eyalet adını kontrol etme
                    for state in item.get('states', []):
                        if state_name.lower() == state['name'].lower():
                            # Eyalet bulundu, şehirleri döndür
                            result.append({
                                "country": formatted_country_name,
                                "state": {
                                    "id": state["id"],
                                    "name": state["name"],
                                    "state_code": state["state_code"],
                                    "latitude": state["latitude"],
                                    "longitude": state["longitude"],
                                    "type": state["type"],
                                    "cities": state["cities"]
                                }
                            })

                elif city_name:
                    # Şehir adını kontrol etme
                    for state in item.get('states', []):
                        for city in state.get('cities', []):
                            if city_name.lower() == city['name'].lower():
                                # Şehir bulundu, şehir ve bağlı olduğu ülke ve eyaleti döndür
                                result.append({
                                    "country": formatted_country_name,
                                    "state": state['name'],
                                    "city": {
                                        "id": city["id"],
                                        "name": city["name"].capitalize(),
                                        "latitude": city["latitude"],
                                        "longitude": city["longitude"]
                                    }
                                })

            if not result:
                return Response({"error": True, "msg": "No matching country, state, or city found."}, status=404)

            return Response({"error": False, "msg": "Search results.", "data": result}, status=200)
        
        except FileNotFoundError:
            return Response({"error": True, "msg": "JSON file not found."}, status=500)
        
        except json.JSONDecodeError:
            return Response({"error": True, "msg": "Failed to decode JSON."}, status=500)
        
        except Exception as e:
            return Response({"error": True, "msg": f"An unexpected error occurred: {str(e)}"}, status=500)
