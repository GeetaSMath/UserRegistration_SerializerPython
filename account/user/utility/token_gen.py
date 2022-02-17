import jwt

class TokenGenerate():
    def encode_token(self, username, password):
        """
            desc: this function will encode the payload into a token
            param: id: it is a user id
            return: token id
        """
        key = 'geetasmath123654';
        payload = {"username": username, "password":password}
        token = jwt.encode(payload, key,)
        return token

    def decode_token(self, encoded):
        """
            desc: this function will decode the token into a payload
            param: token_id: it is a token which is generated at the time of adding a user
            return: decoded user id
        """
        key = 'geetasmath123654'
        decoded = jwt.decode(encoded, key, algorithms=["HS256"])
        print(decoded)
        return decoded['username'], decoded['password']