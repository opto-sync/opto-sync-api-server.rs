from itertools import product

def admitted(authenticated, tenant_match, expected_revision, current_revision):
    return authenticated and tenant_match and expected_revision == current_revision

for authenticated, tenant_match in product((False, True), repeat=2):
    for expected in range(4):
        for current in range(4):
            ok = admitted(authenticated, tenant_match, expected, current)
            if ok:
                assert expected == current and authenticated and tenant_match
                assert current + 1 > current

assert admitted(True,True,2,2)
assert not admitted(True,True,1,2)
print('formal_wave5_model: ok')
