# Merkle-Tree
python implementation of a simple Merkle tree

**running instructions:** once script is running, program will  wait for user input. input options are as follows:

create merkle tree:
'1 <node> <node> <node> ...... <node>' (make sure number of nodes is a power of 2)

print proof of inclusion for given node:
'2 <node index (from creation)>'

check validity of proof of inclusion:
'3 <node to check> <root of tree> <proof of inclusion>'
(checks that the given proof of inclusion is correct for given node and tree root)

find nonce which generates hash beginning with at least given number of '0's:
'4 <number of wanted '0's>'
