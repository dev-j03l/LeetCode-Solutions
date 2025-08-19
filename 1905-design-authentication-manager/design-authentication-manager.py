class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.all_tokens = {}
        self.ttl = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.all_tokens[tokenId] = currentTime + self.ttl #this adds the tokenID with its expiry
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.all_tokens:
            if self.all_tokens[tokenId] <= currentTime:
                self.all_tokens.pop(tokenId)
            else:
                self.all_tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        expired = [key for key, expiry in self.all_tokens.items() if expiry <= currentTime]
    
        for key in expired:
            self.all_tokens.pop(key)
        
        return len(self.all_tokens)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)