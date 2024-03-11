class Codec:
    def __init__(self):
        self.base="http://tinyurl.com/"
        self.encodeMap={}
        self.decodeMap={}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortUrl=self.base+str(1+len(self.encodeMap))
            self.encodeMap[longUrl]=shortUrl
            self.encodeMap[shortUrl]=longUrl
        return self.encodeMap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.encodeMap[shortUrl]
         