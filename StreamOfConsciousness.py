from pwn import xor
from Crypto.Util.number import long_to_bytes
TEXT = [
    '5f7eb00f6c7a858e564aae9ee0',
    '5479a7433f0080961d4cb58bff2a5b2d15d848cc911be92e4cc1', '527eb610050d9a9e1a49fb9fb72442695dfc4c8e', '5165a610050d9e9f1749b7ccb62c5b2647f001c9895c',
    '592bb1582d4181d71a4aa889ff2e432c47ec55c8941ce06b5fd6ec4c0a498927a7e4add3aeb0747035bb5a6344',
    '597fe2532d43ca835647beccab24472715fa54d4d152e53e4a98e11844459c69e0e3bcd3afbe773f25bf5d26',
    '7379bb403842969c455ceedbad7801246ae712d5c841d87a0be7ee585312917a',
    '4763a3446c4ccd991756af95ff38582c59f901d4951bf46b4ed9e10210069566a4af',
    '4463b055290d8f980f56fb9eaa255b205bf20d808d1ee63257d6ef4c0552dd6faff3aa96b5f5390332a8406710a875e1',
    '4763bb102842cd831e40a2ccb82415265bb551c1941cf32250dfa80d0a42dd65b5e8b597afb77e7036b655281ea871e0e92ee4978f',
    '5864b5103c5f82821205ba82bb6b5d2845e558809517a0275298ea0944519562aea1b196e6be7c2424fa54714aae7bb4f866',
    '5e64ee10050a819b5642b4ccb625153d5ab565cf911efe6b5fd6ec4c1043916be0e9bc81e6aa6d2236b35e601ee07bb5e9',
    '592bb1582d4181db566cfc80b36b592646f001c58b17f5324ad0e10203069461e0e9bcd3a2b67c2339fd4d2809af79a5bd25e891db6f',
    '5178e2592a0da4d71e44bfccbe254c6942fc52c8dd06e86b5cdda8050a06896fa5a1ab9aa1b16d717793196b0bae33b4bc',
    '406eb0582d5d9ed71e40fb84be3815245ce652c59952f3235b98fc1e054f9327a1efbdd3afaa393236b9522808b934aef230a7d2e720fb827ee10e7a824b9f6c935f9acf146d12e45dc5',
    '4764b75c280da4d71e44ad89ff2950255cf057c59952f3235bd6a8180c47892789a1ba9cb3b57d7025bf586b02e067b5fe2fa996d531e19e2dac0e6ec7038274975a9fc7017014e50c',
    '4463a71038489f851f47b789ff3f5d205bf201c98e52f3235fcca8180c43dd77a1f2add3a5b8777723fa5b6d4ab47bb2f367e687c461f78f7ee5157bc71998768a45d8',
    '5c64b455600d9d851947ba8eb3320a6961fd44d9dd16e82519cca8070a498a27a8eeaed3a2ab7c3125a319611ee07db3b167e19dc761fd8333e50d61861f9e779918d888556d13ee13a5a39d2bdd215ee9df4a5b710d7d7074c97ac728',
    '592caf10394385960655a2c0ff02152d50e644d28b17a7224a94a8180c43dd61a1f4b587e1aa393d3eb45c244aa261b4bd0eae9f9034fb9e3ffc1171c70a9b75de429ec3556a1ae656c8f59020c4345ee5d400',
    '5464ae5c350d9a9e1a49fb98b7225b2215e149c18952ce6c5398e40905509469a7a1b8d3b5bc7a3f39be19601fb376a1f323a993de25b58236ed15289303926b9b5099d4103932ab5e91a68c65db310ceddd575b700034757e9b6bc1632aa4d02ab56d9a',
    '4463a743290d85980456be9ff36b41215ce601c39c00f5225fdfed4c49069568b7a190d3aab678243fbf196513b371acfb67e09c9035fd9f2dac026995199e789953d68b556d13ee4ac3a79d65c92812a8d9470829457669649b56897562b2ce29fb64d1a597d3d5405512a3e20da0800a34dd1c164243',
    '4763a3446c4ccd9b1951fb83b96b41215cfb46d3dd06ef2a4a98fc040148dd74a5e4b496a2f96d3f77b75c2819af34adfc35ff97dc2dfa832dac0066834b82779f4282c71c771ae95f81f9d82dc9321ba8d34b187d08713c79d56cc06164bac42cb86bdaa7de81945d5457f7fe00e599423cd41a0c0c2441d43c9a264332312fb4fdb6d9ca93005da1e3cfe0ea3f11143f760aa3e45d70dd6c1503eb08e168'
]
prefix = b'crypto{'


def testALL(ciphers, test_key):
    for ctext in ciphers:
        cipher = bytes.fromhex(ctext)
        l = min(len(test_key), len(cipher))
        k = xor(cipher[:l], test_key[:l])
        try:
            te = k.decode('utf8')
            if te.isprintable():
                print(te)
                print('cipher:', ctext)
            else:
                return False
        except:
            return False
    return True


encrypted_flag = ""

key = b''
for ctext in TEXT:
    c = bytes.fromhex(ctext)
    k = xor(c[:len(prefix)], prefix)
    if testALL(TEXT, k):
        encrypted_flag = ctext
        key = k
        break

print("Found some key: ", key, len(key))
print([i for i in key])
print(encrypted_flag)

while True:
    prefix = input("Ente prefix: ").encode()
    cipher = bytes.fromhex(input("Ente cipher: "))
    k = xor(cipher[:len(prefix)], prefix)
    testALL(TEXT, k)
    if input("take this key? ") == '1':
        key = k
        print("Found some key: ", key, len(key))

"""
Our? Why our?
cipher: 5f7eb00f6c7a858e564aae9ee0
Dress-making and Millinery
cipher: 5479a7433f0080961d4cb58bff2a5b2d15d848cc911be92e4cc1
But I will show him.
cipher: 527eb610050d9a9e1a49fb9fb72442695dfc4c8e
And I shall ignore it.
cipher: 5165a610050d9e9f1749b7ccb62c5b2647f001c9895c
I shall lose everything and not get
cipher: 592bb1582d4181d71a4aa889ff2e432c47ec55c8941ce06b5fd6ec4c0a498927a7e4add3aeb0747035bb5a6344
It can't be torn out, but it can be
cipher: 597fe2532d43ca835647beccab24472715fa54d4d152e53e4a98e11844459c69e0e3bcd3afbe773f25bf5d26
crypto{k3y57r34m_r3u53_15_f474l}
cipher: 7379bb403842969c455ceedbad7801246ae712d5c841d87a0be7ee585312917a
What a nasty smell this paint had.
cipher: 4763a3446c4ccd991756af95ff38582c59f901d4951bf46b4ed9e10210069566a4af
Three boys running, playing at hors
cipher: 4463b055290d8f980f56fb9eaa255b205bf20d808d1ee63257d6ef4c0552dd6faff3aa96b5f5390332a8406710a875e1
Why do they go on painting and buil
cipher: 4763bb102842cd831e40a2ccb82415265bb551c1941cf32250dfa80d0a42dd65b5e8b597afb77e7036b655281ea871e0e92ee4978f
How proud and happy he'll be when h
cipher: 5864b5103c5f82821205ba82bb6b5d2845e558809517a0275298ea0944519562aea1b196e6be7c2424fa54714aae7bb4f866
No, I'll go in to Dolly and tell he
cipher: 5e64ee10050a819b5642b4ccb625153d5ab565cf911efe6b5fd6ec4c1043916be0e9bc81e6aa6d2236b35e601ee07bb5e9
I shall, I'll lose everything if he
cipher: 592bb1582d4181db566cfc80b36b592646f001c58b17f5324ad0e10203069461e0e9bcd3a2b67c2339fd4d2809af79a5bd25e891db6f
As if I had any wish to be in the r
cipher: 5178e2592a0da4d71e44bfccbe254c6942fc52c8dd06e86b5cdda8050a06896fa5a1ab9aa1b16d717793196b0bae33b4bc
Perhaps he has missed the train and
cipher: 406eb0582d5d9ed71e40fb84be3815245ce652c59952f3235b98fc1e054f9327a1efbdd3afaa393236b9522808b934aef230a7d2e720fb827ee10e7a824b9f6c935f9acf146d12e45dc5
Would I have believed then that I c
cipher: 4764b75c280da4d71e44ad89ff2950255cf057c59952f3235bd6a8180c47892789a1ba9cb3b57d7025bf586b02e067b5fe2fa996d531e19e2dac0e6ec7038274975a9fc7017014e50c
The terrible thing is that the past
cipher: 4463a71038489f851f47b789ff3f5d205bf201c98e52f3235fcca8180c43dd77a1f2add3a5b8777723fa5b6d4ab47bb2f367e687c461f78f7ee5157bc71998768a45d8
Love, probably? They don't know how
cipher: 5c64b455600d9d851947ba8eb3320a6961fd44d9dd16e82519cca8070a498a27a8eeaed3a2ab7c3125a319611ee07db3b167e19dc761fd8333e50d61861f9e779918d888556d13ee13a5a39d2bdd215ee9df4a5b710d7d7074c97ac728
I'm unhappy, I deserve it, the faul
cipher: 592caf10394385960655a2c0ff02152d50e644d28b17a7224a94a8180c43dd61a1f4b587e1aa393d3eb45c244aa261b4bd0eae9f9034fb9e3ffc1171c70a9b75de429ec3556a1ae656c8f59020c4345ee5d400
Dolly will think that I'm leaving a
cipher: 5464ae5c350d9a9e1a49fb98b7225b2215e149c18952ce6c5398e40905509469a7a1b8d3b5bc7a3f39be19601fb376a1f323a993de25b58236ed15289303926b9b5099d4103932ab5e91a68c65db310ceddd575b700034757e9b6bc1632aa4d02ab56d9a
These horses, this carriage - how I
cipher: 4463a743290d85980456be9ff36b41215ce601c39c00f5225fdfed4c49069568b7a190d3aab678243fbf196513b371acfb67e09c9035fd9f2dac026995199e789953d68b556d13ee4ac3a79d65c92812a8d9470829457669649b56897562b2ce29fb64d1a597d3d5405512a3e20da0800a34dd1c164243
What a lot of things that then seem
cipher: 4763a3446c4ccd9b1951fb83b96b41215cfb46d3dd06ef2a4a98fc040148dd74a5e4b496a2f96d3f77b75c2819af34adfc35ff97dc2dfa832dac0066834b82779f4282c71c771ae95f81f9d82dc9321ba8d34b187d08713c79d56cc06164bac42cb86bdaa7de81945d5457f7fe00e599423cd41a0c0c2441d43c9a264332312fb4fdb6d9ca93005da1e3cfe0ea3f11143f760aa3e45d70dd6c1503eb08e168
"""