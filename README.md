# rsa_pychat
RSA PyChat is a Python 3.10 based TCP messaging application that uses the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem) "RSA (cryptosystem) - Wikipedia") to secure communication. Currently this version does not use [OAEP](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding "Optimal asymmetric encryption padding - Wikipedia"), however this may be likely to change. This version includes a basic implementation of RSA, as well as an implementation of [SHA256](https://en.wikipedia.org/wiki/SHA-2 "SHA-2 - Wikipedia").

# Basic Operation
We take for example a conversation between Alice (A) and Bob (B), with Alice being the sender and Bob the recipient.

The basic operation on Alice's end is as follows:
```mermaid
flowchart TD
  start["Start"] --> inp["Take message.\nm"]
  inp --> rsaSend["Encode m with B's public key k1.\nc = RSA_enc(m; k1)"]
  inp --> shaSend["Hash m.\nm_hash = SHA256(m)"]
  shaSend --> makeSig["Encode m_hash with RSA using A's private key k2.\ns = RSA_enc(m_hash; k2)"]
  rsaSend --> transmit["Transmit both c and s bundled together.\n T = (c, s)"]
  makeSig --> transmit
  transmit --> e["End"]
```

... and on Bob's end:
```mermaid
flowchart TD
  Start --> rec["Receive T."]
  rec --> decSig["Decrypt s using A's public key k3.\nm_hash* = RSA_dec(s; k3)"]
  rec --> decMes["Decrypt c using B's private key k4.\nm* = RSA_dec(c; k4)"]
  decMes --> hashMes["Hash m*.\nm*_hash = SHA256(m*)"]
  hashMes --> checkEq{"Check equality.\nm*_hash == m_hash* ?"}
  decSig --> checkEq
  checkEq -- Yes --> disp["Received m*."]
  disp --> e["End"]
  checkEq -- No --> err[["Error in message receipt."]]
```
