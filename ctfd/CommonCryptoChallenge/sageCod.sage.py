

# This file was *autogenerated* from the file sageCod.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0xa96e6f96f6aedd5f9f6a169229f11b6fab589bf6361c5268f8217b7fad96708cfbee7857573ac606d7569b44b02afcfcfdd93c21838af933366de22a6116a2a3dee1c0015457c4935991d97014804d3d3e0d2be03ad42f675f20f41ea2afbb70c0e2a79b49789131c2f28fe8214b4506db353a9a8093dc7779ec847c2bea690e653d388e2faff459e24738cd3659d9ede795e0d1f8821fd5b49224cb47ae66f9ae3c58fa66db5ea9f73d7b741939048a242e91224f98daf0641e8a8ff19b58fb8c49b1a5abb059f44249dfd611515115a144cc7c2ca29357af46a9dc1800ae9330778ff1b7a8e45321147453cf17ef3a2111ad33bfeba2b62a047fa6a7af0eef = Integer(0xa96e6f96f6aedd5f9f6a169229f11b6fab589bf6361c5268f8217b7fad96708cfbee7857573ac606d7569b44b02afcfcfdd93c21838af933366de22a6116a2a3dee1c0015457c4935991d97014804d3d3e0d2be03ad42f675f20f41ea2afbb70c0e2a79b49789131c2f28fe8214b4506db353a9a8093dc7779ec847c2bea690e653d388e2faff459e24738cd3659d9ede795e0d1f8821fd5b49224cb47ae66f9ae3c58fa66db5ea9f73d7b741939048a242e91224f98daf0641e8a8ff19b58fb8c49b1a5abb059f44249dfd611515115a144cc7c2ca29357af46a9dc1800ae9330778ff1b7a8e45321147453cf17ef3a2111ad33bfeba2b62a047fa6a7af0eef); _sage_const_0x10001 = Integer(0x10001); _sage_const_0x23 = Integer(0x23); _sage_const_0x67fbf6baae6748f5bcd78a68a7b6519362572fb0fca6ec5ab9ffe389e79920504f0856043d513baf02ff256d9bd42f0f537e117c2bf5ecd1437ebfb9d2d2f33ce9d35a4614e07584018f10734205bd78be87476d73816fa69698825eccd81f7886f81c34a9192e7b08c944ca681f4d876ffab00926f98d4f7454e85f3465c75d14802e6e935590874bbc0ea7f02c171165e7aa40e394b7dba06faf532d38c1984c150324b99d76b0795aed6668a0c67a5bf147a9f6bbde214a6a631c677fb38d427dedd015391b4f54db673173415a74cc421d22632150ffdf6f557b21cd52e2268008a17dd42bb126ef7bcbc3a2224ea4eafe1eadd867da9263f56050a07f37 = Integer(0x67fbf6baae6748f5bcd78a68a7b6519362572fb0fca6ec5ab9ffe389e79920504f0856043d513baf02ff256d9bd42f0f537e117c2bf5ecd1437ebfb9d2d2f33ce9d35a4614e07584018f10734205bd78be87476d73816fa69698825eccd81f7886f81c34a9192e7b08c944ca681f4d876ffab00926f98d4f7454e85f3465c75d14802e6e935590874bbc0ea7f02c171165e7aa40e394b7dba06faf532d38c1984c150324b99d76b0795aed6668a0c67a5bf147a9f6bbde214a6a631c677fb38d427dedd015391b4f54db673173415a74cc421d22632150ffdf6f557b21cd52e2268008a17dd42bb126ef7bcbc3a2224ea4eafe1eadd867da9263f56050a07f37); _sage_const_0x97a1afa14f2281a3314268d2fc55caf106f38c94bdef62fb395854cf83ee8f0fb7127e7ac0de7ae0711e752be6e54943f97ba2e66e9d15f651b8b403505e69fccbbadc9dd6d828abd455635d67a1fe0b877a266025c55f3c5a2599d27df6ef0dccaf1d5958d931337ff43a78f35d5005644a560aca259352180f49c29398d817a11f7cf6097206ff25ed5f2b295a2366606a926d93ac9e17372b61d1319480fde699b97ba725361e89c43973785c4b24d076528cf6035b8a929c07a06d99118d1c78c8e582b566f87ef5736c7e071ce2dbb812b8d06b4db5a586ae8b46e3ad6518486524f37d380f14848b526eed412f0c869ea3b425c0070ec70d80d5f89f17 = Integer(0x97a1afa14f2281a3314268d2fc55caf106f38c94bdef62fb395854cf83ee8f0fb7127e7ac0de7ae0711e752be6e54943f97ba2e66e9d15f651b8b403505e69fccbbadc9dd6d828abd455635d67a1fe0b877a266025c55f3c5a2599d27df6ef0dccaf1d5958d931337ff43a78f35d5005644a560aca259352180f49c29398d817a11f7cf6097206ff25ed5f2b295a2366606a926d93ac9e17372b61d1319480fde699b97ba725361e89c43973785c4b24d076528cf6035b8a929c07a06d99118d1c78c8e582b566f87ef5736c7e071ce2dbb812b8d06b4db5a586ae8b46e3ad6518486524f37d380f14848b526eed412f0c869ea3b425c0070ec70d80d5f89f17)
from Crypto.Util.number import long_to_bytes

n = _sage_const_0xa96e6f96f6aedd5f9f6a169229f11b6fab589bf6361c5268f8217b7fad96708cfbee7857573ac606d7569b44b02afcfcfdd93c21838af933366de22a6116a2a3dee1c0015457c4935991d97014804d3d3e0d2be03ad42f675f20f41ea2afbb70c0e2a79b49789131c2f28fe8214b4506db353a9a8093dc7779ec847c2bea690e653d388e2faff459e24738cd3659d9ede795e0d1f8821fd5b49224cb47ae66f9ae3c58fa66db5ea9f73d7b741939048a242e91224f98daf0641e8a8ff19b58fb8c49b1a5abb059f44249dfd611515115a144cc7c2ca29357af46a9dc1800ae9330778ff1b7a8e45321147453cf17ef3a2111ad33bfeba2b62a047fa6a7af0eef 
e1 = _sage_const_0x10001 
e2 = _sage_const_0x23 
c1 = Mod(_sage_const_0x67fbf6baae6748f5bcd78a68a7b6519362572fb0fca6ec5ab9ffe389e79920504f0856043d513baf02ff256d9bd42f0f537e117c2bf5ecd1437ebfb9d2d2f33ce9d35a4614e07584018f10734205bd78be87476d73816fa69698825eccd81f7886f81c34a9192e7b08c944ca681f4d876ffab00926f98d4f7454e85f3465c75d14802e6e935590874bbc0ea7f02c171165e7aa40e394b7dba06faf532d38c1984c150324b99d76b0795aed6668a0c67a5bf147a9f6bbde214a6a631c677fb38d427dedd015391b4f54db673173415a74cc421d22632150ffdf6f557b21cd52e2268008a17dd42bb126ef7bcbc3a2224ea4eafe1eadd867da9263f56050a07f37 , n)
c2 = Mod(_sage_const_0x97a1afa14f2281a3314268d2fc55caf106f38c94bdef62fb395854cf83ee8f0fb7127e7ac0de7ae0711e752be6e54943f97ba2e66e9d15f651b8b403505e69fccbbadc9dd6d828abd455635d67a1fe0b877a266025c55f3c5a2599d27df6ef0dccaf1d5958d931337ff43a78f35d5005644a560aca259352180f49c29398d817a11f7cf6097206ff25ed5f2b295a2366606a926d93ac9e17372b61d1319480fde699b97ba725361e89c43973785c4b24d076528cf6035b8a929c07a06d99118d1c78c8e582b566f87ef5736c7e071ce2dbb812b8d06b4db5a586ae8b46e3ad6518486524f37d380f14848b526eed412f0c869ea3b425c0070ec70d80d5f89f17 , n)

d, a, b = xgcd(e1, e2)        # calculate a and b

m = c1**a * c2**b
print(long_to_bytes(m))

