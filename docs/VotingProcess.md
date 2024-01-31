<p><a target="_blank" href="https://app.eraser.io/workspace/AQgo9v7DnuFwT9pplvrx" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Voting Process 
```
<a href="https://app.eraser.io/workspace/AQgo9v7DnuFwT9pplvrx?elements=KRK8aAvYfmcuzW_2E1vjLw">View on Eraser<br /><img src="https://app.eraser.io/workspace/AQgo9v7DnuFwT9pplvrx/preview?elements=KRK8aAvYfmcuzW_2E1vjLw&type=embed" /></a>
```
**Code for sequence diagram**

```
order Election Authority, Registrar, Voter, Bulletin Board(BB), Tallier, Trusted Server
Election Authority[icon: user, color:darkorchid] > Election Authority: Runs setup
Election Authority > Bulletin Board(BB) [icon: database, color: green]: Eligble voters, candidate list, election public key, registrar public key, encryption and commitment public parameters, and zk proof key pair
Voter[icon: user, color: darkorchid] > Voter: registervoter(id) -->(c_id, cr_id, t_ic)
Voter > Registrar[icon: user, color: darkorchid]: Commitment c_id and identity id
Registrar > Registrar: Register(): adds identity and commitment to list L, computes merkle tree root rtL, and signs pair (L, rtL)
Registrar > Bulletin Board(BB): Commitments, Merkle tree root rtL, list of voters, and registrar signature
opt [label: verify] {
  Voter > Bulletin Board(BB): Verify published commitment to their identity
}
Voter > Voter: Vote(): generates ballot B, with encrypted vote e_v, pseudonym cr_id, and disjoint proof π_id
if[label: if valid(B)] {
  Voter > Bulletin Board(BB): Append(B)
} else [label: if ! valid(B)] {
 Voter > Bulletin Board(BB): Ballot B
 Voter < Bulletin Board(BB): Rejects Ballot B
}
opt [label: verify] {
  Voter > Bulletin Board(BB): Verify Ballot B is appended to BB
}
loop[label: null ballots] {
  Trusted Server [icon: server, color: blue] > Bulletin Board(BB): Adds a null ballot B
}
Bulletin Board(BB) > Tallier[icon: user, color: darkorchid]: Gets all data from BB
Tallier > Tallier: Calls tally(BB,sk_T)-> s,Π
Tallier > Bulletin Board(BB): Publishes election result: s and proof of correct talling: Π
opt[label verify]{
  Voter > Bulletin Board(BB): verifyTally(BB,s,Π)
}
```



<!--- Eraser file: https://app.eraser.io/workspace/AQgo9v7DnuFwT9pplvrx --->