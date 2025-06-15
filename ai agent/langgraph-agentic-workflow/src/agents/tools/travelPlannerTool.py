class TravelPlannerTool:
    def plan_itinerary(self, location, days):
        return f"Here is a {days}-day itinerary for {location}:\nDay 1: Explore local attractions\nDay 2: Adventure activities\nDay 3: Relax and shopping."

    def suggest_budget_hotels(self, location):
        return f"Suggested budget hotels in {location}:\n1. Hotel X - ₹2500/night\n2. Hotel Y - ₹2000/night\n3. Hotel Z - ₹1800/night."

    def calculate_total_cost(self, hotel_cost, days, other_expenses, budget):
        total_cost = (hotel_cost * days) + other_expenses
        if total_cost <= budget:
            return f"The total cost for the trip is ₹{total_cost}, which is within your budget of ₹{budget}."
        else:
            return f"The total cost for the trip is ₹{total_cost}, which exceeds your budget of ₹{budget}. Consider adjusting your plans."