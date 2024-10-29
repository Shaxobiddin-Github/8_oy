from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class FoodAnonThrottle(AnonRateThrottle):
    scope = "food_anon"

class FoodAnonRateThrottle2(AnonRateThrottle):
    scope = "food_anon_2"