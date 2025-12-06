# Simple circuit breaker pattern (conceptual example)

class MinistryService:
    def __init__(self):
        self.failures = 0
        self.limit = 3
        self.online = True

    def call(self):
        if not self.online:
            return "Service temporarily disabled (circuit open)"
        
        # simulate failure
        self.failures += 1
        
        if self.failures >= self.limit:
            self.online = False
            return "Circuit opened - ministry dependency isolated"
        
        return "Success"


service = MinistryService()
print(service.call())
print(service.call())
print(service.call())
print(service.call())  # circuit opens
