---
summary: The OutSystems Security library provides actions to perform several security related operations, such as encrypting and decrypting content or using JSON Web Tokens.
tags: 
locale: en-us
guid: dc098281-2826-4f5c-91cb-da13827f4d8a
app_type: mobile apps, reactive web apps
---
# Security

The OutSystems Security library provides actions to perform several security related operations, such as encrypting and decrypting content or using JSON Web Tokens.

## Actions

### JWT_SetShowPII
Defines whether the personally identifiable information ('PII') is shown on exceptions raised when working with tokens.

_Inputs_

IsPIIShown: mandatory; data type Boolean

Indicates if PII should be shown or not.

_Outputs_

PreviousShowPIIValue; data type Boolean 

The previously defined value. Useful to restore previous state.

### JWT_CreateToken
Creates and signs a JWT token.

_Inputs_

TokenPayload: mandatory; data type TokenPayload Record

The payload of the token to be created.

JWKForSigning: optional; data type Text

JSON Web Key ('JWK') to be used to sign the token. It should include all information necessary to derive the private key. If no key is given, the token is not signed.

_Outputs_

EncodedToken; data type Text

The encoded and signed JWT token.

### JWT_ReadToken
Extracts claims as well as validates a JWT token.

_Inputs_

EncodedToken: mandatory; data type Text

The encoded token to be read and validated.

ValidateSignature : mandatory; data type Boolean

Indicates if the token’s signature should be validated.

ValidationParameters: mandatory; data type ValidationParameters Record

The parameters used to validate the token.

_Outputs_

TokenPayload; data type TokenPayload Record

The payload of the token, including the custom claims.

### AES_NewKey
Generates a new random AES Key.

_Inputs_

NrBits : mandatory; data type Integer

The size of the key in bits. Can be one of the following: 128, 192 or 256.

_Outputs_

Key; data type Binary Data 

 A newly generated cryptographically secure random key.

### AES_Encrypt
Provides authenticated encryption of the text using the provided key (this text will be UTF-8 encoded prior to encryption). Encrypts using AES in Cipher-Block Chaining mode with random initialization vector (IV) and PKCS7 padding. Authenticates by Encrypt-then-MAC with HMAC using the same key, performed over both IV and encrypted message. IV is prepended to the encrypted message.

_Inputs_

Plaintext: mandatory; data type Text 

The plaintext to encrypt.

Key: mandatory; data type Binary Data 

The key to encrypt.

_Outputs_

Ciphertext; data type Binary Data 

The plaintext encrypted with the provided key.

### AES_Decrypt
Decrypts the text using the provided key. Decrypts using AES in Cipher-Block Chaining mode with initialization vector extracted for the start of the ciphertext and PKCS7 padding. Validates the authenticity of the encryption with HMAC using the same key.

_Inputs_

Ciphertext: mandatory ; data type BinaryData 

The encrypted text to decrypt.

Key: mandatory ; data type Binary Data 

The key to decrypt.

_Outputs_

Plaintext; data type Text 

The decrypted ciphertext. This is UTF-8 decoded after decryption.

### CryptoRandomInt
Generates a random number using a cryptographic random number generator, within a range defined by a minimum value (‘MinVal') and maximum value ('MaxVal').

_Inputs_

MinValue: mandatory ; data type Integer

The minimum value (inclusive) for the range of numbers to be considered. 

MaxValue: mandatory ; data type Integer 

The maximum value (exclusive) for the range of numbers to be considered. 

_Outputs_

RandomNumber; data type Integer 

The randomly generated number from the specified range.

### GenerateSecurePassword
Generates a secure password using a cryptographic random number generator. 

_Inputs_

Length: mandatory ; data type Integer

The length of the password to be generated. The length must be at least 6 characters.

IncludeUppercaseLetters: optional ; data type Boolean

Indicates if the generated password should include upper case letters. If no value is given, defaults to false.

If set to true, the generated password will include at least 1 upper case letter.

IncludeNumbers: optional ; data type Boolean

Indicates if the generated password should include numbers. If no value is given, defaults to false.

If set to true, the generated password will include at least 1 number.

IncludeSpecialCharacters: optional ; data type Boolean

Indicates if the generated password should include special characters (!"#$%&'()*+,-./:;<=>?@[]^_`{|}~). If no value is given, defaults to false.

If set to true, the generated password will include at least 1 special character.

_Outputs_

Password; data type Text 

The randomly generated password.

### ComputeHash
Computes the hash of the given data (this data will be UTF-8 encoded prior to hashing).

_Inputs_

Data: mandatory ; data type Text 

The data to hash. 

Algorithm: optional ; data type Text 

The algorithm to use. Default algorithm is SHA512. Check .NET's HashAlgorithm.Create documentation for a full list of available algorithms.

_Outputs_

Hash; data type Binary Data 

The hash computed from the given data.

### ComputeMAC
Computes the MAC of the given data (this data will be UTF-8 encoded prior).

_Inputs_

Data: mandatory ; data type Text

The data to compute the MAC. 

Key: mandatory ; data type Binary Data 

The binary key

Algorithm: optional ; data type Text 

The algorithm to use. Default algorithm is HMACSHA512. Check .NET's HMAC.Create documentation for a full list of available algorithms.

_Outputs_

Mac ; data type Binary Data 

The MAC computed from the given data.

### RSA_NewKey
Generates a new RSA key.

_Inputs_

NrBits: mandatory ; data type Integer 

The number of bits in the key.

_Outputs_

Key; data type Text 

A newly generated RSA key represented in XML, containing both the public and the private elements of the key.

### RSA_GetPublicKey
Extracts the public key from an RSA key represented in XML.

_Inputs_

Key: mandatory ; data type Text 

The XML representation of the RSA key.

_Outputs_

PublicKey; data type Text 

The XML representation of the RSA key only containing the public elements.

### RSA_KeyFromPEM
Reads an RSA key from a PEM file.

_Inputs_

PEM: mandatory ; data type Text

The contents of the PEM file. Supports files as long as key is enclosed between -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY----- .

_Outputs_

Key; data type Text 

The XML representation of the RSA key read from the PEM file, containing both the public and the private elements of the key.

### RSA_Decrypt
Decrypts a ciphertext encrypted with RSA.

_Inputs_

CipherText: mandatory ; data type Binary Data

The ciphertext to decrypt.

Key: mandatory ; data type Text 

The key to decrypt (this should be the XML representation of the RSA key).

Padding: optional; data type Text 

The padding mode to be used. Can be one of the following: OAEPSHA1, OAEPSHA256, OAEPSHA384, OAEPSHA512. If no value is given, defaults to OAEPSHA1.

_Outputs_

Plaintext; data type Text 

The decrypted cyphertext. This is UTF-8 decoded after decryption.

### RSA_Encrypt
Encrypts a text with RSA (this text will be UTF-8 encoded prior to encryption).

_Inputs_

Plaintext: mandatory ; data type Text 

The plaintext to encrypt. 

Key: mandatory ; data type Text 

The key to encrypt (this should be the XML representation of the RSA key)

Padding: optional ; data type Text 

The padding mode to be used. Can be one of the following: OAEPSHA1, OAEPSHA256, OAEPSHA384, OAEPSHA512. If no value is given, defaults to OAEPSHA1.

_Outputs_

Ciphertext; data type Binary Data 

The encrypted plaintext.

### RSA_Sign
Signs textual data with an RSA key to provide guarantees the text was produced by the owner of that key (this text will be UTF-8 encoded prior to encryption).

_Inputs_

Plaintext: mandatory ; data type Text 

The plaintext to sign.

Key: mandatory ; data type Text 

The key to sign the data with (this should be the XML representation of the RSA key).

Algorithm: optional ; data type Text 

The hash algorithm to sign with. Default algorithm is SHA512. Check .NET's  HashAlgorithm.Create documentation for a full list of available algorithms.

Padding: optional ; data type Text

The padding mode to be used. Can be one of the following: PSS, PKCS1. If no value is given, defaults to PSS.

_Outputs_

Signature; data type Binary Data 

The resulting signature.

### RSA_VerifySignature
Verifies the signature of a piece of data against the corresponding RSA public key.

_Inputs_

Data: mandatory ; data type Binary Data 

The data that was signed.

Signature: mandatory ; data type Binary Data 

The signature to verify.

PublicKey: mandatory ; data type Text 

The public key to verify the signature against (this should be the XML representation of the RSA key only containing the public elements).

Algorithm: optional ; data type Text 

The hash algorithm used to sign. Default algorithm is SHA512. Check .NET's  HashAlgorithm.Create documentation for a full list of available algorithms.

Padding: optional; data type Text 

The padding mode to be used. Can be one of the following: PSS, PKCS1. If no value is given, defaults to PSS.

_Outputs_

IsValid; data type Boolean

True if the signature is verified by the given key.

## Structures

### CustomClaim
Represents the name/value pair of a custom claim.

_Attributes_

Name: mandatory ; data type Text Length: 500000

Name of the claim.

Value: mandatory ; data type Text Length: 500000

Value of the claim.

### TokenPayload
Represents a JSON Web Token (JWT) payload.

_Attributes_

Issuer: mandatory ; data type Text Length: 500000

iss claim

Subject: mandatory ; data type Text Length: 500000

sub claim

Audience: mandatory ; data type Text Length: 500000

aud claim

ExpirationTime: mandatory ; data type DateTime 

exp claim

NotBefore: mandatory ; data type DateTime 

nbf claim

IssuedAt: mandatory ; data type DateTime 

iat claim

JWTId: mandatory ; data type Text Length: 500000

jti claim

CustomClaims: mandatory ; data type CustomClaim Record List 

The remaining claims present in the token.

### ValidationParameters
Configuration parameters to be used when validating a JSON Web Token (JWT).

_Attributes_

ValidateLifetime: mandatory ; data type Boolean 

Indicates if the token's expiration date should be validated.

ValidateAudience: mandatory ; data type Boolean 

Indicates if the token's audience should be validated.

ValidateIssuer: mandatory ; data type Boolean 

Indicates if the token's issuer should be validated.

ValidAudience: mandatory ; data type Text Length: 500000

Value to be used when validating the audience.

ValidIssuer: mandatory ; data type Text Length: 500000

Value to be used when validating the issuer.

IssuerSigningJWK: mandatory ; data type Text Length: 500000

The JSON Web Key to be used to verify the token’s signature.
